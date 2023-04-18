from .colors import Colors
from .constants import LOG_LEVEL
from enum import Enum

class LogLevel(Enum):
    NONE = 0
    LOGGING = 1
    WARNINGS = 2
    ERRORS = 3


def log(message, levelReq=LogLevel.LOGGING, color=Colors.LOG_COLOR):
    if not __debug__: return
    if LOG_LEVEL >= levelReq.value:
        printContext(2)
        with coloredOutput(color):
            print(message)

def warn(message):
    if not __debug__: return
    log(message, color=Colors.WARN)
warning = warn

def unreachableState(message=''):
    if not __debug__: return
    if len(message):
        warn(f'Unreachable State Reached: {message}')
    else:
        warn('Unreachable State Reached!')
unreachable = unreachableState
