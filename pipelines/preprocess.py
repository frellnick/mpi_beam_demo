"""Sample Preprocessing Runner."""


import os
import subprocess

import apache_beam as beam

from settings import get_config
from utils.load import (
    make_schema_from_csv,
    make_csv_coder, 
    make_standard_sql
)
from utils.filters import (
    SubsetMapped
)


config = get_config()


def _default_project():
    get_project = [
        'gcloud', 'config', 'list', 'project', '--format=value(core.project)'
    ]

    with open(os.devnull, 'w') as dev_null:
        return subprocess.check_output(get_project, stderr=dev_null).strip()


class _ReadData(beam.PTransform):
    """Wrapper for reading from either CSV files or from BigQuery"""

    def __init__(self, handle, mode=None):
        self._handle = handle 
        self._mode = mode


    def expand(self, pipeline):
        if self._handle.endswith('.csv'):
            # The input is CSV file(s).
            schema = make_schema_from_csv(self._handle)
            csv_coder = make_csv_coder(schema)
            return (pipeline
                    | 'ReadFromText' >> beam.io.ReadFromText(
                        self._handle,
                        skip_header_lines=1
                        )
                    | 'ParseCSV' >> beam.Map(csv_coder))

        else:
            # The input is BigQuery table name(s)
            query = make_standard_sql(self._handle)
            return (pipeline
                    | 'ReadFromBigQuery' >> beam.io.Read(
                        beam.io.BigQuerySource(query=query, use_standard_sql=True)
                    ))



class _StandardizeData(beam.PTransform):
    """Wrapper for standardizing data elements"""

    def __init__(self, mode=None):
        self._mode = mode 

    def clean_subset(self, collection:beam.PCollection):
        return (
            collection
            | 'SubsetRow' >> beam.ParDo(SubsetMapped())
        )




def run_preprocess(pipeline, handle):
    # Ready handle for read elements
    if config.ENVIRONMENT == 'DEV':
        handle = os.path.join(config.LOCAL_FILE_DIR, handle)

    r = _ReadData(handle)
    s = _StandardizeData()
    return r.expand(pipeline), s.clean_subset(r)
    