from enum import Enum

from dbapihelper.connection import Connection
from dbapihelper.exceptions import (
    DataError,
    DatabaseError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    Warning,
)


__all__ = [
    'apilevel',
    'threadsafety',
    'paramstyle',
    'connect',
    'DataError',
    'DatabaseError',
    'Error',
    'IntegrityError',
    'InterfaceError',
    'InternalError',
    'NotSupportedError',
    'OperationalError',
    'ProgrammingError',
    'Warning',
    'Type',
]


apilevel = '2.0'
# Threads may share the module and connections
threadsafety = 2
paramstyle = 'pyformat'


def connect(self, *args, **kwargs):
    return Connection(*args, **kwargs)


class Type(Enum):
    STRING = 'string'
    NUMBER = 'number'
    BOOLEAN = 'boolean'
