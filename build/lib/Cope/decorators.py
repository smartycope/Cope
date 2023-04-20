from .debugging import getMetaData, beingUsedAsDecorator, debugCount, getContext, printContext
from .constants import HIDE_TODO, DISPLAY_PATH, DISPLAY_FILE, DISPLAY_FUNC
from .misc import CommonResponses
from .colors import coloredOutput, darken


################################### Decorators ###################################
__todoCalls = set()
def todo(featureName=None, enabled=True, blocking=False, limitCalls=True,
         showFunc=True, showFile=True, showPath=False):
    """ Leave reminders for yourself to finish parts of your code.
        Can be manually turned on or off with hideAllTodos(bool).
        Can also be used as a decorator (function, or class) to print a reminder
        and also throw a NotImplemented error on being called/constructed.
    """
    if not __debug__: return

    metadata  = getMetaData(2)
    situation = beingUsedAsDecorator('todo', metadata)
    # First off, if we're limiting calls, check if we've already been called
    uniqueID = (metadata.lineno, metadata.filename)
    if limitCalls and uniqueID in __todoCalls:
        return
    else:
        __todoCalls.add(uniqueID)

    # def decorator(*decoratorArgs, **decoratorKwArgs):
    #     def wrap(func):
    #         def innerWrap(*funcArgs, **funcKwArgs):
    #             return func(*funcArgs, **funcKwArgs)
    #         return innerWrap
    #     return wrap

    def printTodo(disableFunc):
        if not HIDE_TODO and enabled:
            debugCount()
            with coloredOutput(Colors.TODO):
                print(getContext(metadata, True,
                                (showFunc or DISPLAY_FUNC) and not disableFunc,
                                showFile or DISPLAY_FILE,
                                showPath or DISPLAY_PATH), end='')
                # This is coincidental, but it works
                print(f'TODO: {featureName.__name__ if disableFunc else featureName}')
            if blocking:
                raise NotImplementedError()

    # Being used as a function decorator, or we're not sure
    if situation in (1, 3):
        def wrap(func):
            def innerWrap(*funcArgs, **funcKwArgs):
                printTodo(True)
                if blocking:
                    raise NotImplementedError()
                return featureName(*funcArgs, **funcKwArgs)
            return innerWrap
        return wrap

    elif situation == 2:
        def wrap(clas):
            def raiseErr(*_, **kw_):
                raise NotImplementedError()
            printTodo(True)
            if blocking:
                featureName.__init__ = raiseErr
        return featureName
    else:
        printTodo(False)

def confidence(level, interpretAs:int=None):
    if not __debug__: return

    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):
            definiteFailResponses = ()
            possiblyFailResponses = ()
            probablyFailResponses = ()

            def getPrettyLevel():
                if type(level) is str:
                    return f'({level} confident)'
                else:
                    assert(type(level) in (int, float))
                    return f'({level}% confidence)'

            def definiteFail():
                raise UserWarning(f"{func.__name__} is going to fail. {getPrettyLevel()}")

            def probablyFail():
                printContext(3, darken(80, Colors.ALERT), showFunc=False)
                with coloredOutput(Colors.ALERT):
                    print(f"Warning: {func.__name__} will probably fail. {getPrettyLevel()}")

            def possiblyFail():
                printContext(3, darken(80, Colors.CONFIDENCE_WARNING), showFunc=False)
                with coloredOutput(Colors.CONFIDENCE_WARNING):
                    print(f"Warning: {func.__name__} might not work. {getPrettyLevel()}")

            def unknownInput():
                # If we don't understand the input, just give a soft warning (it will display what the input is, anyway)
                possiblyFail()
                return

                if interpretAs is None:
                    raise TypeError(f"I don't recognize {level} as a confidence level.")

                if interpretAs > 100:
                    raise TypeError(f"You can't be {interpretAs}% confident, that's not how it works.")
                elif interpretAs < 0:
                    # replaceLine(f'\n\t\t\t\t\t\t"{level.lower()},', offset=+2)
                    definiteFailResponses += (

                    )
                    definiteFail()
                elif interpretAs < 20:
                    # replaceLine(f'\n\t\t\t\t\t\t"{level.lower()},', offset=+2)
                    probablyFailResponses += (

                    )
                    probablyFail()
                elif interpretAs < 50:
                    # replaceLine(f'\n\t\t\t\t\t\t"{level.lower()},', offset=+2)
                    possiblyFailResponses += (

                    )
                    possiblyFail()

            if type(level) in (int, float):
                # This is a pet-peeve
                if level > 100:
                    raise TypeError(f"You can't be {level}% confident, that's not how it works.")
                elif level < 0:
                    definiteFail()
                elif level < 20:
                    probablyFail()
                elif level < 50:
                    possiblyFail()
            elif type(level) is str:
                _level = level.lower()
                if _level in CommonResponses.NO or _level in CommonResponses.LOW_AMOUNT or _level in probablyFailResponses:
                    probablyFail()
                elif _level in CommonResponses.MAYBE or _level in CommonResponses.SOME_AMOUNT or _level in possiblyFailResponses:
                    possiblyFail()
                elif _level in definiteFailResponses:
                    definiteFail()
                elif _level not in CommonResponses.YES and _level not in CommonResponses.HIGH_AMOUNT and \
                     _level not in CommonResponses.NA  and _level not in CommonResponses.MODERATE_AMOUNT:
                    unknownInput()
            else:
                unknownInput()
            return func(*funcArgs, **funcKwArgs)
        return innerWrap
    return wrap

confident = confidence
untested = confidence(21)
tested = confidence(80)

def depricated(why=''):
    if not __debug__: return

    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):
            printContext(2, darken(80, Colors.DEPRICATED_WARNING))
            with coloredOutput(Colors.DEPRICATED_WARNING):
                print(f"{func.__name__} is Depricated{': ' if len(why) else '.'}{why}")
            return func(*funcArgs, **funcKwArgs)
        return innerWrap
    return wrap

def reprise(obj, *args, **kwargs):
    """ Sets the __repr__ function to the __str__ function of a class.
        Useful for custom classes with overloaded string functions
    """
    obj.__repr__ = obj.__str__
    return obj
