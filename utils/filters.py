# filters.py


import apache_beam as beam
from assets.mapping import colmap


def filter_mapped_columns(source_columns:list, keep_columns:list) -> list:
    """Return list of columns available for mapping from source list.

    Parameters
    __________
    source_columns : list
        list of columns [str] from source
    keep_columns : list
        list of columns [str] to keep

    Returns
    _______
    list
        a list of columns representing the intersection of keep and source columns
    """

    return list(
        set(source_columns).intersection(set(keep_columns))
    )



class SubsetMapped(beam.DoFn):
    def __init__(self, colmap=colmap):
        self.keep_columns = list(colmap.keys())

    def process(self, row:dict):
        rcols = list(row.keys())
        mapped_columns = filter_mapped_columns(rcols, self.keep_columns)
        yield {k: row[k] for k in mapped_columns}