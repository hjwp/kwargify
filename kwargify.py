import inspect


def kwargify(*args, **kwargs):
    caller_locals = inspect.stack()[1].frame.f_locals
    caller_globals = inspect.stack()[1].frame.f_globals
    for name, local in caller_locals.items():
        try:
            kwargs[name] = next(a for a in args if a is local)
        except StopIteration:
            pass
    for name, globl in caller_globals.items():
        try:
            kwargs[name] = next(a for a in args if a is globl)
        except StopIteration:
            pass
    return kwargs
