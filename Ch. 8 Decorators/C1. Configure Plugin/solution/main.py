def configure_plugin_decorator(func):
    def wrapper(*args):
        result = func(**dict(args))
        return result

    return wrapper
