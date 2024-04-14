"""
hk102: upsampling.py

This module provides a function for upsampling a given DataFrame to a specified frequency.

The main function in this module is `upsampling()`, 
    which takes a DataFrame as input and returns the upsampled DataFrame.

For more information, refer to the manual:
    https://gist.github.com/taruma/96c321175ecac3e51350ef4c94f3d7d4
"""

import pandas as pd
from hidrokit.contrib.taruma.utils import handle_deprecated_params


# ref: https://stackoverflow.com/q/29612705/4886384
# pylint: disable=too-many-arguments
def upsampling(
    dataframe,
    freq="D",
    fill_method="ffill",
    use_interpolation=False,
    interpolation_method="linear",
    interpolation_args=None,
    reindex=False,
    **kwargs
):
    """
    Upsamples a given DataFrame to a specified frequency.

    Parameters:
        dataframe (DataFrame): The input DataFrame to be upsampled.
        freq (str, optional): The frequency to upsample to.
            Defaults to "D" (daily).
        fill_method (str, optional): The method to fill missing values.
            Defaults to "ffill" (forward fill).
        use_interpolation (bool, optional): Whether to use interpolation for filling missing values.
            Defaults to False.
        interpolation_method (str, optional): The interpolation method to use. Defaults to "linear".
        interpolation_args (dict, optional): Additional keyword arguments for 
            the interpolation method.
            Defaults to an empty dictionary.
        reindex (bool, optional): Whether to return the upsampled DataFrame without
            filling missing values.
            Defaults to False.
        **kwargs: Additional keyword arguments for backward compatibility.

    Returns:
        DataFrame: The upsampled DataFrame.

    Deprecated Parameters:
        df (DataFrame): Deprecated parameter for `dataframe`. 
            Use `dataframe` instead.
        use_inter (bool): Deprecated parameter for `use_interpolation`. 
            Use `use_interpolation` instead.
        inter_method (str): Deprecated parameter for `interpolation_method`. 
            Use `interpolation_method` instead.
        inter_keys (dict): Deprecated parameter for `interpolation_args`. 
            Use `interpolation_args` instead.

    """
    # backward compatibility
    dataframe = handle_deprecated_params(kwargs, "df", "dataframe") or dataframe
    use_interpolation = (
        handle_deprecated_params(kwargs, "use_inter", "use_interpolation")
        or use_interpolation
    )
    interpolation_method = (
        handle_deprecated_params(kwargs, "inter_method", "interpolation_method")
        or interpolation_method
    )
    interpolation_args = (
        handle_deprecated_params(kwargs, "inter_keys", "interpolation_args")
        or interpolation_args
    )

    interpolation_args = {} if interpolation_args is None else interpolation_args

    start = dataframe.index.min() - pd.DateOffset(day=1)
    end = dataframe.index.max() - pd.DateOffset(day=31)
    date = pd.date_range(start, end, freq=freq)

    upsampled_dataframe = dataframe.reindex(date)

    if reindex:
        return upsampled_dataframe

    if use_interpolation:
        return upsampled_dataframe.interpolate(
            method=interpolation_method, **interpolation_args
        )

    return upsampled_dataframe.fillna(method=fill_method)
