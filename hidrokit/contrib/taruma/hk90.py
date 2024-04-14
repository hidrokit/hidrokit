"""
hk90: calibration
This module provides a calibration function that iterates over a parameter grid 
    and evaluates the performance of a calibrated model using specified metrics.

Functions:
    calibration(
        observed, func, calibration_parameter, func_parameter, 
        metrics, met_names, met_sort, met_min=True, observed_func=None)

For more details, refer to the manual: 
    https://gist.github.com/taruma/906e1577111208291e0725229c7d0a76
"""

from itertools import product
import pandas as pd


def _parameter_grid(parameter):
    # ref: sklearn.model_selection.ParameterGrid
    items = parameter.items()
    keys, values = zip(*items)
    for combination in product(*values):
        grid = dict(zip(keys, combination))
        yield grid


def _best_parameter(results, calibration_parameter):
    key = list(calibration_parameter.keys())
    return dict(zip(key, results.iloc[0][key].values))

# pylint: disable=too-many-arguments, too-many-locals
def calibration(
    observed,
    func,
    calibration_parameter,
    func_parameter,
    metrics,
    met_names,
    met_sort,
    met_min=True,
    observed_func=None,
):
    """
    Perform calibration by iterating over a parameter grid and evaluating the
    performance of the calibrated model using specified metrics.

    Parameters:
        observed (array-like): Observed data for calibration.
        func (callable): Function that represents the model to be calibrated.
        calibration_parameter (dict): Dictionary of calibration parameters and their values.
        func_parameter (dict): Dictionary of additional parameters for the model function.
        metrics (list or tuple): List of metric functions to evaluate the model performance.
        met_names (list): List of names for the metrics.
        met_sort (str): Name of the metric to sort the results by.
        met_min (bool, optional): Whether to sort the results in ascending order of the metric.
        observed_func (callable, optional): Function to preprocess the observed data.

    Returns:
        pandas.DataFrame: DataFrame containing the calibration results, including the
        calibrated parameter values and the evaluation metrics.

    """
    metrics = metrics if isinstance(metrics, (list, tuple)) else [metrics]
    met_names = met_names if isinstance(met_names, (list)) else [met_names]

    param_grid = list(_parameter_grid(calibration_parameter))
    n_param = len(param_grid)
    print(f"N = {n_param}")

    observed = observed_func(observed) if observed_func is not None else observed

    results = []

    print("PROGRESS 0 [-x--xx--x-] 100")
    print("---------> [", end="")

    for i, p in enumerate(param_grid, start=1):
        simulated = func(**p, **func_parameter)
        met_res = [m(simulated, observed) for m in metrics]
        results.append(list(p.values()) + met_res)
        if (i % (n_param // 10)) == 0:
            print("=", end="")
        columns_name = list(p.keys()) + met_names

    print("] DONE")

    results = (
        pd.DataFrame(results, columns=columns_name)
        .sort_values(by=met_sort, ascending=met_min)
        .reset_index(drop=True)
    )

    return results
