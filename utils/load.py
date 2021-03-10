"""
Load

Prepare loading mechanism
"""

from settings import get_config

from apache_beam.dataframe.io import read_csv 


config = get_config()

def _raise_not_implemented():
    raise NotImplementedError('Loader Not Defined')

loaders = {
    'DEV': read_csv,
    'STAGING': _raise_not_implemented,
    'PRODUCTION': _raise_not_implemented
}



def get_loader(config=config):
    return loaders[config.ENVIRONMENT]

