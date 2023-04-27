from pathlib import Path
from typing import Union, SupportsInt

class _ConfigSingleton:
    # Override the debug parameters and display the file/function for each debug call
    #   (useful for finding debug calls you left laying around and forgot about)
    display_file = True
    display_func = True
    display_path = False
    root_dir = None

    _debug_count = 0
    verbosity = 1

    hide_todo = False

config = _ConfigSingleton()
