"""
Load

Prepare loading mechanism
"""

from settings import get_config
from assets.mapping import is_mapped

from apache_beam.io.textio import ReadFromText

import csv
from collections import OrderedDict


def make_schema_from_csv(handle):
    # Read first row and split into column headers
    with open(handle, newline='') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        h = next(r)

    s = OrderedDict()
    for i,x in enumerate(h):
        s[x] = i

    return s


def make_csv_coder(schema):
    # Return string parser for CSV data
    def _parser(element):
        return csv.reader([element], delimiter=',')
    
    def _marshal_into_schema(columns, schema):
        res = {}
        for i, k in enumerate(schema.keys()):
            # Rename k
            std, err = is_mapped(k)
            if not err:
                res[std] = columns[i]
            else:
                res[k] = columns[i]
        return res

    def _coder(element):
        columns = list(_parser(element))[0]
        return _marshal_into_schema(columns, schema)
    
    return _coder

        
def make_standard_sql(handle):
    # Query table data from BigQuery
    pass


