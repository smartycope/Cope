from pathlib import Path
from typing import Union, SupportsInt

ENABLE_TESTING = True

# This is because I write a lot of C/C++ code
true, false = True, False

_debugCount = 0

# Override the debug parameters and display the file/function for each debug call
#   (useful for finding debug calls you left laying around and forgot about)
DISPLAY_FILE = False
DISPLAY_PATH = False
DISPLAY_FUNC = False
DISPLAY_LINK = False
HIDE_TODO    = False
# FORCE_TODO_LINK = False

#* Convenience commonly used paths. ROOT can be set by the setRoot() or markRoot() functions
#! These are broken
# DIR  = dirname(__file__)
DIR  = None
# ROOT = dirname(DIR) if basename(DIR) in ('src', 'source') else DIR
ROOT = None  #dirname(DIR) if basename(DIR) in ('src', 'source') else DIR
HOME = str(Path.home())

# Yes, this is not strictly accurate.
MAX_INT_SIZE = 2147483645

VERBOSE = True
DEBUG_LEVEL = LOG_LEVEL = 0


number = Union[int, float, SupportsInt]
HIDE_TODO = False


def displayAllFiles(to=True):
    global DISPLAY_FILE
    DISPLAY_FILE = to

def displayAllPaths(to=True):
    global DISPLAY_PATH
    DISPLAY_PATH = to

def displayAllFuncs(to=True):
    global DISPLAY_FUNC
    DISPLAY_FUNC = to

def displayAllLinks(to=True):
    global DISPLAY_LINK
    DISPLAY_LINK = to

def hideAllTodos(to=True):
    global HIDE_TODO
    HIDE_TODO = to

def setRoot(path):
    global ROOT
    ROOT = path

def markRoot(relative='.'):
    global ROOT
    ROOT = join(dirname(stack()[1].filename), relative)
    print(ROOT)

def setVerbose(to=True):
    global VERBOSE
    VERBOSE = to

def verbose():
    global VERBOSE
    return VERBOSE

def setLogLevel(to):
    global LOG_LEVEL
    LOG_LEVEL = to
