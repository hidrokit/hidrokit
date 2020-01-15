"""manual:
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


def calibration(observed, func, calibration_parameter, func_parameter,
                metrics, met_names, met_sort, met_min=True,
                observed_func=None):

    metrics = metrics if isinstance(metrics, (list, tuple)) else [metrics]
    met_names = (met_names if isinstance(met_names, (list))
                 else [met_names])

    param_grid = list(_parameter_grid(calibration_parameter))
    n_param = len(param_grid)
    print('N = {}'.format(n_param))

    observed = (
        observed_func(observed) if observed_func is not None else observed
    )

    results = []

    print('PROGRESS 0 [-x--xx--x-] 100')
    print('---------> [', end='')

    for i, p in enumerate(param_grid, start=1):
        simulated = func(**p, **func_parameter)
        met_res = [m(simulated, observed) for m in metrics]
        results.append(
            list(p.values()) + met_res
        )
        if (i % (n_param // 10)) == 0:
            print('=', end='')

    print('] DONE')

    columns_name = list(p.keys()) + met_names

    results = (pd.DataFrame(results, columns=columns_name)
                 .sort_values(by=met_sort, ascending=met_min)
                 .reset_index(drop=True))

    return results
