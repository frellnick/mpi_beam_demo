from settings import get_config

import argparse
import logging
import os

import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions 
from apache_beam.dataframe.convert import to_dataframe, to_pcollection

from assets.mapping import *
from utils.load import get_loader
from utils.filters import filter_mapped_columns
from utils.dataframe_transforms.standardize import StandardizeTransformer

import pandas as pd

c = get_config()


def run(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='usbe_students.csv',
        help='Input file or table to process.'
    )
    parser.add_argument(
        '--output',
        dest='output',
        default='usbe_students_mapped.csv',
        help='Output file to write results to.'
    )

    known_args, pipeline_args = parser.parse_known_args(argv)

    # Local imports to avoid pickling unnecessary libraries
    l = get_loader()


    # Create Pipeline.
    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        #########################
        # Creating the DataView #
        #########################

        # Load Source Table
        source_table = p | l(os.path.join(c.LOCAL_FILE_DIR, known_args.input))

        # Create subset view
        filtered_columns = filter_mapped_columns(
                            list(source_table.columns), list(colmap.keys())
                            )
        df = source_table[filtered_columns]
        
        # TODO: Standardize Subset
        t = StandardizeTransformer(filtered_columns)
        df = df.apply(t)
        # TODO: Dedup Subset

        
        
        
    


if __name__ == "__main__":
    logging.basicConfig()
    run()

        