from settings import get_config

import logging 

import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions 

from utils.load import get_loader


if __name__ == "__main__":
    c = get_config()
    print(c)

    l = get_loader()

    pipeline_options = PipelineOptions()
    # Create Pipeline.
    with beam.Pipeline(options=pipeline_options) as p:
        # Main Pipeline
        result_pc = (
            p
            | "main_pc" >> beam.Create([1,2,3])
            | 'Sum values' >> beam.CombineGlobally(sum)
            | beam.Map(print)
        )
