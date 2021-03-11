# filters.py


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