from __future__ import unicode_literals

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.lexers import SqlLexer
from pygments.styles import get_style_by_name
from tabulate import tabulate


def loop(
        cursor,
        reserved=None,
        history_file=None,
        raise_=False,
        *args,
        **kwargs):
    lexer = PygmentsLexer(SqlLexer)
    completer = WordCompleter(reserved, ignore_case=True)
    style = style_from_pygments_cls(get_style_by_name('manni'))
    history = FileHistory(history_file) if history_file else None

    while True:
        try:
            query = prompt(
                'sql> ', lexer=lexer, completer=completer,
                style=style, history=history)
        except (EOFError, KeyboardInterrupt):
            break  # Control-D pressed.

        # run query
        query = query.strip('; ').replace('%', '%%')
        if query:
            try:
                result = cursor.execute(query, *args, **kwargs)
            except Exception as e:
                if raise_:
                    raise
                print(e)
                continue

            columns = [t[0] for t in cursor.description or []]
            print(tabulate(result, headers=columns))

    print('See ya!')
