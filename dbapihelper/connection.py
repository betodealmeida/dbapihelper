from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from dbapihelper.cursor import Cursor
from dbapihelper.exceptions import Error
from dbapihelper.utils import check_closed


class Connection(object):

    cursor_class = Cursor

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.closed = False
        self.cursors = []

    @check_closed
    def close(self):
        """Close the connection now."""
        self.closed = True
        for cursor in self.cursors:
            try:
                cursor.close()
            except Error:
                pass  # already closed

    @check_closed
    def commit(self):
        """Commit any pending transaction to the database."""
        pass

    @check_closed
    def cursor(self):
        cursor = self.cursor_class(*self.args, **self.kwargs)
        self.cursors.append(cursor)
        return cursor

    @check_closed
    def execute(self, operation, parameters=None, *args, **kwargs):
        cursor = self.cursor()
        return cursor.execute(operation, parameters, *args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.commit()
        self.close()
