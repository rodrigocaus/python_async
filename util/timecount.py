import asyncio
import sys
import functools
import time


def exectime(func):
    """Function decorator that reports
    execution time
    """
    def eprint(*args):
        print(*args, sep=' ', flush=True, file=sys.stderr)

    @functools.wraps(func)
    async def aiowrap(*args, **kwargs):
        eprint("Running function:", func.__name__)
        start = time.time()
        result = await func(*args, **kwargs)
        eprint(func.__name__, 'execution time:', time.time() - start, 'sec')
        return result

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        eprint("Running function:", func.__name__)
        start = time.time()
        result = func(*args, **kwargs)
        eprint(func.__name__, 'execution time:', time.time() - start, 'sec')
        return result

    if asyncio.iscoroutinefunction(func):
        return aiowrap
    elif callable(func):
        return wrap

    raise ValueError('{} must be a callable. Received: {}'.format(
        func.__name__, func.__class__.__name__
    ))
