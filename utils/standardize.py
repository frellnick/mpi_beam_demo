"""
Standardization classes

Compose dynamic standardizer and yield callable DoFn
"""


import apache_beam as beam


from utils.compose import composite_function
from assets.mapping import is_mapped

from utils.standard_transforms.standardization_transforms import transform_classes

class StandardizeTransformer():

    def __init__(self, fields:list):
        self.fields = fields 
        self.transform = self._compose(fields)


    def _compose(self, fields:list):
        functions = []
        for field in fields:
            sfield, err = is_mapped(field)
            if not err:
                print('Found mapped field', sfield)
                functions.append(transform_classes[sfield]())
        return composite_function(*functions)


    def __call__(self, x):
        return self.transform(x)



class StandardizeSubset(beam.DoFn):
    def __init__(self, columns):
        self._standardizer = StandardizeTransformer(columns)

    def process(self, element):
        yield self._standardizer(element)