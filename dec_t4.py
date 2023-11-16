import functools
from time import sleep

def retry(attempts=5):
    def _retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                if func(*args, **kwargs):
                    return True
                else:
                    sleep(2 * i)
            raise Exception("Retry Failed with {} attempts".format(attempts))
        return wrapper
    return _retry

@retry(attempts=4)
def some_func(x):
    return False
print(some_func(10))