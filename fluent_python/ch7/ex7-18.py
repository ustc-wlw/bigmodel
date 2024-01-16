'''
functools 标准库中的装饰器: lru_cache、wraps、singledispatch
'''

import time
import functools

def clock(func:callable):
    ## copy func attributes to clocked function
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join([repr(arg) for arg in args])
        print('[%0.8fs] %s(%s) --> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__=='__main__':
    print('result is ', fibonacci(6))