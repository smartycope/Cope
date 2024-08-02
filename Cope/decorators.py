"""
Miscellaneous decorators that can be useful
"""

from .debugging import get_metadata, called_as_decorator, print_debug_count, get_context
from .util import percentage
from warnings import warn
_todoCalls = set()
hide_todo = False


class EpistemologicalWarning(UserWarning):
    """ This is a joke/pet peeve of mine for people who say they're 100% confident in something """
    pass

def todo(feature:str=None, enabled:bool=True, blocking:bool=False, limit:bool=True):
    # Can be manually turned on or off with hideAllTodos(bool).
    """ Leave reminders for yourself to finish parts of your code.
        Can also be used as a decorator (for functions or classes) to print a reminder and optionally
        throw a NotImplemented error on being called/constructed.
        Parameters:
            enabled: enable or disable printed warnings
            blocking: raise an error, instead of just warning you
            limit: if called multiple times, and this is true, only print once
    """

    if not __debug__:
        return

    metadata = get_metadata(2)
    situation = called_as_decorator('todo', metadata)
    # First off, if we're limiting calls, check if we've already been called
    uniqueID = (metadata.lineno, metadata.filename)
    if limit and uniqueID in _todoCalls:
        return
    else:
        _todoCalls.add(uniqueID)

    def printTodo(disableFunc):
        if not hide_todo and enabled:
            print_debug_count()
            print(get_context(metadata, path=True, func=False if disableFunc else None), end='', style=color)
             # This is coincidental, but it works
            print(f'TODO: {feature.__name__ if disableFunc else feature}')
            if blocking:
                raise NotImplementedError(feature)

    # Being used as a function decorator, or we're not sure
    if situation in (1, 3):
        def wrap(func):
            def innerWrap(*funcArgs, **funcKwArgs):
                printTodo(True)
                if blocking:
                    raise NotImplementedError(feature)
                return feature(*funcArgs, **funcKwArgs)
            return innerWrap
        return wrap

    elif situation == 2:
        def wrap(clas):
            def raiseErr(*_, **kw_):
                raise NotImplementedError(feature)
            printTodo(True)
            if blocking:
                feature.__init__ = raiseErr
        return feature
    else:
        printTodo(False)

def confidence(level:float):
    """ A decorator useful for communicating the confidence in a function. Useful for writing quick-and-dirty APIs.
        Not meant to be used in a production environment.

        `level` is given as a percentage (as a float or an int, both work), and that is the "percent confident" you are
        that the function/class will work as intended.

        * If `level` < 95% (P < .05), a warning is printed that the function may not work.
        * If `level` < 50%, a UserWarning is raised indicating the function will probably not work.
        * If `level` < 10%, an Exception is raised indicating the function will almost certainly not work.

        To disable the warnings, you can pass `_warn=False` to the function when calling it. If `level` == 0, however,
        it will still print a warning anyway.

        NOTE:
            * Does nothing if __debug__ is not True
            * Don't put 100%, unless the function is mathematically proven
    """
    level = percentage(level) * 100

    # This is a pet-peeve
    if level > 100:
        raise ValueError(f"You can't be {level}% confident, that's not how it works.")

    def wrap(func):
        def inner_wrap(*args, _warn=True, **kwargs):
            if __debug__:
                # Definite Failure
                if level <= 0:
                    if _warn:
                        raise Exception(f"{func.__name__} will not work as intended. ({level}% confidence)")
                    else:
                        warn(f"{func.__name__} will not work as intended. ({level}% confidence)")
                if level < 5 and _warn:
                    raise Exception(f"{func.__name__} will almost certainly not work as intended. ({level}% confidence)")
                # Likely Failure
                elif level < 50 and _warn:
                    raise UserWarning(f"{func.__name__} will probably not work as intended. ({level}% confidence)")
                # Possible Failure
                elif level < 95 and _warn:
                    warn(f"{func.__name__} may not work as intended. ({level}% confidence)")

            return func(*args, **kwargs)
        return inner_wrap
    return wrap

untested = confidence(51)
tested = works  = confidence(96)
