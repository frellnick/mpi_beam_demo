from decouple import config
import inspect
from utils.singleton import SingletonType

class Config(metaclass=SingletonType):
    def __init__(self, default=True):
        super().__init__()
        self.DEV = config('DEV', cast=bool)




    def __repr__(self):
        return f"class 'config.Config'\n{self._collect_attrs()}"
    

    ## For Export and Logging
    ## Inspect self and get all non default attributes.
    def _collect_attrs(self) -> list:
        attr = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        return self._to_dict([
            a for a in attr if not(
                a[0].startswith('__') and a[0].endswith('__')
                )
        ])


    def _to_dict(self, keyvals:list) -> dict:
        d = {}
        for kv in keyvals:
            d[kv[0]] = kv[1]
        return d


def get_config(default=True):
    return Config(default)