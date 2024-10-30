import inspect


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    info['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    info['module'] = inspect.getmodule(obj)
    return info


number_info = introspection_info(42)
print(number_info)
