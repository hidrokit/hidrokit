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
                FutureWarning,
            )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def handle_deprecated_params(kwargs, old_param, new_param):
    """
    Handle deprecated parameters by issuing a warning and returning the value of the old parameter.

    Args:
        kwargs (dict): A dictionary of keyword arguments.
        old_param (str): The name of the deprecated parameter.
        new_param (str): The name of the new parameter to use instead.

    Returns:
        The value of the old parameter if it exists in the kwargs dictionary, otherwise None.
    """
    if old_param in kwargs:
        warnings.warn(
            f"The `{old_param}` parameter is deprecated. Please use `{new_param}` instead.",
            FutureWarning,
        )
        return kwargs[old_param]
    return None
