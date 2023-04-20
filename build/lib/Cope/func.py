class FunctionCall:
    """ A helpful class that represents an as-yet uncalled function call with parameters """
    def __init__(self, func=lambda: None, args=(), kwargs={}):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def call(self, *args, override_args=False, **kwargs):
        return self.__call__(*args, override_args, **kwargs)

    def __call__(self, *args, override_args=False, **kwargs):
        """ If you specify parameters and don't explicitly set override_args to True,
            then the given parameters are ignored and the previously set parameters are used.
        """
        if override_args:
            return self.func(*args, **kwargs)
        else:
            return self.func(*self.args, **self.kwargs)

class Signal:
    """ A custom Signal implementation. Connect with the connect() function """
    def __init__(self, *args, **kwargs):
        self.viableArgsCount = len(args)
        self.viableKwargs = kwargs.keys()
        self.funcs = []
        self.call = self.__call__

    def connect(self, func):
        self.funcs.append(FunctionCall(func))

    def emit(self, *args, **kwargs):
        self.__call__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        for f in self.funcs:
            # Verify that the parameters are valid
            if len(args) != self.viableArgsCount:
                raise TypeError("Signal emitted with incorrect number of parameters")
            for i in kwargs.keys():
                if i not in self.viableKwargs:
                    raise TypeError("Signal emitted with invalid keyword argument")
            f(*args, override_args=True, **kwargs)
