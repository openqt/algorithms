# coding=utf-8
import functools


def print_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print '>>>', ret
        return ret
    return wrapper
