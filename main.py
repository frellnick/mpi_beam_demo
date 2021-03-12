from settings import get_config

import argparse
import logging
import os

import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions 
from apache_beam.dataframe.convert import to_dataframe, to_pcollection

from pipelines.preprocess import run_preprocess

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


    # Create Pipeline.
    with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
        
        ##########################
        # Load / Preprocess Data #
        ##########################
        sdata = run_preprocess(p, known_args.input)
        _ = (
            sdata
            | beam.Map(print))


        #########################
        # Creating the DataView #
        #########################


        
        
    


if __name__ == "__main__":
    logging.basicConfig()
    run()

        