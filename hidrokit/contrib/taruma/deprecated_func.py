"""
This module contains deprecated functions.
"""

import warnings
import functools


def deprecated(new_func_name):
    """
    Decorator to mark a function as deprecated.

    Parameters:
    - new_func_name (str): The name of the new function that should be used instead.

    Returns:
    - wrapper (function): The decorated function.

    Example:
    @deprecated("new_function")
    def old_function():
        pass

    The above example will generate a warning when `old_function` is called,
    suggesting to use `new_function` instead.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{func.__name__} is deprecated, use {new_func_name} instead",
                DeprecationWarning,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator
