"""Test for .prep.timeseries module
"""

from hidrokit.prep import timeseries
import numpy as np
import pandas as pd
from numpy.testing import assert_equal
from pandas.testing import assert_index_equal

# =======
# Private
# =======


def test__timestep_single():
    # Transpose to save spaces
    array_single = np.array(
        [10, 20, 30, 40, 50, 60, 70]
    )

    array = np.array(
        [
            [10],
            [20],
            [30],
            [40],
            [50],
            [60],
            [70]
        ]
    )

    array_result = np.array(
        [
            [30, 20, 10],
            [40, 30, 20],
            [50, 40, 30],
            [60, 50, 40],
            [70, 60, 50]
        ]
    )

    func = timeseries._timestep_single
    assert_equal(array_result, func(array))
    assert_equal(array_result, func(array_single))


def test__timestep_multi():
    array = np.array(
        [
            [10, 13, 15],
            [20, 23, 25],
            [30, 33, 35],
            [40, 43, 45],
            [50, 53, 55],
            [60, 63, 65],
            [70, 73, 76]
        ]
    )

    # No argument
    array_result_1 = np.array(
        [
            [30, 20, 10, 33, 23, 13, 35, 25, 15],
            [40, 30, 20, 43, 33, 23, 45, 35, 25],
            [50, 40, 30, 53, 43, 33, 55, 45, 35],
            [60, 50, 40, 63, 53, 43, 65, 55, 45],
            [70, 60, 50, 73, 63, 53, 76, 65, 55]
        ]
    )

    # Argument: index=[0, 2]
    array_result_2 = np.array(
        [
            [30, 20, 10, 33, 35, 25, 15],
            [40, 30, 20, 43, 45, 35, 25],
            [50, 40, 30, 53, 55, 45, 35],
            [60, 50, 40, 63, 65, 55, 45],
            [70, 60, 50, 73, 76, 65, 55]
        ]
    )

    # Argument: timesteps=4, keep_first=False
    array_result_3 = np.array(
        [
            [50, 40, 30, 20, 53, 43, 33, 23, 55, 45, 35, 25],
            [60, 50, 40, 30, 63, 53, 43, 33, 65, 55, 45, 35],
            [70, 60, 50, 40, 73, 63, 53, 43, 76, 65, 55, 45]
        ]
    )

    func = timeseries._timestep_multi
    assert_equal(array_result_1, func(array))
    assert_equal(array_result_2, func(array, index=[0, 2]))
    assert_equal(array_result_3, func(array, timesteps=4, keep_first=False))

# ======
# Public
# ======


def test_timestep_table():
    dataframe = pd.DataFrame(
        columns=['A', 'B', 'C'],
        data=np.array(
            [
                [10, 13, 15],
                [20, 23, 25],
                [30, 33, 35],
                [40, 43, 45],
                [50, 53, 55],
                [60, 63, 65],
                [70, 73, 76]
            ]
        )
    )

    # Argument: None
    dataframe_result_1 = pd.DataFrame(
        columns=['A_tmin0', 'A_tmin1', 'A_tmin2', 'B_tmin0', 'B_tmin1',
                 'B_tmin2', 'C_tmin0', 'C_tmin1', 'C_tmin2'],
        data=np.array(
            [
                [30, 20, 10, 33, 23, 13, 35, 25, 15],
                [40, 30, 20, 43, 33, 23, 45, 35, 25],
                [50, 40, 30, 53, 43, 33, 55, 45, 35],
                [60, 50, 40, 63, 53, 43, 65, 55, 45],
                [70, 60, 50, 73, 63, 53, 76, 65, 55]
            ]
        )
    )

    # Argument: columns=['A', 'C']
    dataframe_result_2 = pd.DataFrame(
        columns=['A_tmin0', 'A_tmin1', 'A_tmin2', 'B',
                 'C_tmin0', 'C_tmin1', 'C_tmin2'],
        data=np.array(
            [
                [30, 20, 10, 33, 35, 25, 15],
                [40, 30, 20, 43, 45, 35, 25],
                [50, 40, 30, 53, 55, 45, 35],
                [60, 50, 40, 63, 65, 55, 45],
                [70, 60, 50, 73, 76, 65, 55]
            ]
        )
    )

    # Argument: timesteps=4, keep_first=False
    dataframe_result_3 = pd.DataFrame(
        columns=['A_tmin1', 'A_tmin2', 'A_tmin3', 'A_tmin4',
                 'B_tmin1', 'B_tmin2', 'B_tmin3', 'B_tmin4',
                 'C_tmin1', 'C_tmin2', 'C_tmin3', 'C_tmin4'],
        data=np.array(
            [
                [50, 40, 30, 20, 53, 43, 33, 23, 55, 45, 35, 25],
                [60, 50, 40, 30, 63, 53, 43, 33, 65, 55, 45, 35],
                [70, 60, 50, 40, 73, 63, 53, 43, 76, 65, 55, 45]
            ]
        )
    )

    func = timeseries.timestep_table

    assert_equal(
        dataframe_result_1.values,
        func(dataframe).values
    )
    assert_index_equal(
        dataframe_result_1.columns,
        func(dataframe).columns
    )

    assert_equal(
        dataframe_result_2.values,
        func(dataframe, columns=['A', 'C']).values
    )
    assert_index_equal(
        dataframe_result_2.columns,
        func(dataframe, columns=['A', 'C']).columns
    )

    assert_equal(
        dataframe_result_3.values,
        func(dataframe, timesteps=4, keep_first=False).values
    )
    assert_index_equal(
        dataframe_result_3.columns,
        func(dataframe, timesteps=4, keep_first=False).columns
    )
