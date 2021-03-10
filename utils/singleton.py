"""
Singleton

SingletonType Class for inheriting singleton design metaclass.

Inherit with:

from ..singleton import SingletonType
class MyClass(metaclass=SingletonType)
"""

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

