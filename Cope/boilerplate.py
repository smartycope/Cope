decorator = """
    def decorator(*decoratorArgs, **decoratorKwArgs):
        def wrap(func):
            def innerWrap(*funcArgs, **funcKwArgs):
                return func(*funcArgs, **funcKwArgs)
            return innerWrap
        return wrap
    """
