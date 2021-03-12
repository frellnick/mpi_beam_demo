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
from utils.standardize import (
    StandardizeSubset
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
                    | 'ParseCSV' >> beam.Map(csv_coder)
                    | 'StandardizeSubset' >> beam.ParDo(
                        StandardizeSubset(schema))
                    )

        else:
            # The input is BigQuery table name(s)
            schema = None
            query = make_standard_sql(self._handle)
            return (pipeline
                    | 'ReadFromBigQuery' >> beam.io.Read(
                        beam.io.BigQuerySource(query=query, use_standard_sql=True)
                    | 'StandardizeSubset' >> beam.ParDo(
                        StandardizeSubset(schema))
                    )




def run_preprocess(pipeline, handle):
    # Ready handle for read elements
    if config.ENVIRONMENT == 'DEV':
        handle = os.path.join(config.LOCAL_FILE_DIR, handle)

    r = _ReadData(handle)
    rd = r.expand(pipeline)

    return rd
    