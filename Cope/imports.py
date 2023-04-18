from typing import Union
import importlib

################################### Import Utilities ###################################
def ensureImported(package:str, specificModules=[], _as=None,
                fatal:bool=False, printWarning:Union[str, bool]=True,
                _globals=globals(), _locals=locals(), level=0
                ) -> "(Union[package, (packages,)], worked)":
    if type(specificModules) is str:
        specificModules = [specificModules]
    try:
        _temp = __import__(package, _globals, _locals, specificModules, level)
    except ImportError:
        if type(printWarning) is str:
            print(printWarning)
        elif printWarning:
            if len(specificModules):
                print(f'Can\'t import {tuple(specificModules)} from {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
            else:
                print(f'Can\'t import {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
        if fatal:
            raise ImportError(package)
        return False
    else:
        if len(specificModules):
            for i in specificModules[:-1]:
                globals()[i] = _temp.__getattribute__(i)
            globals()[_as if _as else specificModules[-1]] = _temp.__getattribute__(specificModules[-1])
        else:
            globals()[_as if _as else package] = _temp
        return True

# todo
def checkImport(package:str, specificModules=[], _as=None,
                fatal:bool=False, printWarning:Union[str, bool]=True,
                _globals=globals(), _locals=locals(), level=0
                ) -> "(Union[package, (packages,)], worked)":
    # todo()
    return
    if type(specificModules) is str:
        specificModules = [specificModules]
    try:
        _temp = __import__(package, _globals, _locals, specificModules, level)
    except ImportError:
        if type(printWarning) is str:
            print(printWarning)
        elif printWarning:
            if len(specificModules):
                print(f'Can\'t import {tuple(specificModules)} from {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
            else:
                print(f'Can\'t import {package}. Have you installed the associated pip package? (try "pip install {pacakge}")')
        if fatal:
            raise ImportError(package)
        return False
    else:
        if len(specificModules):
            for i in specificModules[:-1]:
                globals()[i] = _temp.__getattribute__(i)
            globals()[_as if _as else specificModules[-1]] = _temp.__getattribute__(specificModules[-1])
        else:
            globals()[_as if _as else package] = _temp
        return True

def dependsOnPackage(package:str, specificModules=[], _as=None,
                fatal:bool=True, printWarning:Union[str, bool]=True,
                _globals=globals(), _locals=locals(), level=0):
    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):
            if ensureImported(package, specificModules, _as, fatal,
                           printWarning, globals, locals, level):
                return func(*funcArgs, **funcKwArgs)
            else:
                return None
        return innerWrap
    return wrap

def importpath(path, name, moduleName):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    # This is kinda ugly and nasty, but it works. For now.
    globals()[moduleName] = importlib.import_module(name, moduleName).__getattribute__(moduleName)
