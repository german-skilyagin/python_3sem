import functools
import random

from typing import List

def reverse_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        else:
            return None
    return wrapper

@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year():
    return 1957.

print(get_university_name(),get_university_founding_year(),sep="\n")