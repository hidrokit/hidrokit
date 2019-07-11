"""Module for reading data.
"""


def missing_row(dataframe, date_index=True, date_format='%Y/%m/%d'):
    """Return dictionary of missing values dataframe.

    Return dictionary contains columns name and list of the index
    missing values.

    Parameters
    ----------
    dataframe : DataFrame
        Dataframe
    date_index : bool, optional
        Format index to date_format, by default True
    date_format : str, optional
        String representation of strftime() directive, by default '%Y/%m/%d'

    Returns
    -------
    dict
        Return dictionary of columns name and index of missing values.

    Examples
    --------

    Examples for non-date index:

    >>> A = pd.DataFrame(data=[[1, 3, 4, np.nan, 2, np.nan],
    ...                        [np.nan, 2, 3, np.nan, 1, 4],
    ...                        [2, np.nan, 1, 3, 4, np.nan]],
    ...               columns=['A', 'B', 'C', 'D', 'E', 'F'])
    ... A
        A    B   C    D  E    F
    0  1.0  3.0  4  NaN  2  NaN
    1  NaN  2.0  3  NaN  1  4.0
    2  2.0  NaN  1  3.0  4  NaN
    >>> missing_row(A, date_index=False)
    {'A': [1], 'B': [2], 'C': [], 'D': [0, 1], 'E': [], 'F': [0, 2]}

    Index is timestamp:

    >>> date_index = pd.date_range("20190617", "20190619")
    >>> A.set_index(date_index, inplace=True)
    ... A
                  A    B  C    D  E    F
    2019-06-17  1.0  3.0  4  NaN  2  NaN
    2019-06-18  NaN  2.0  3  NaN  1  4.0
    2019-06-19  2.0  NaN  1  3.0  4  NaN
    >>> missing_row(A, date_format="%m%d")
    {'A': ['0618'],
    'B': ['0619'],
    'C': [],
    'D': ['0617', '0618'],
    'E': [],
    'F': ['0617', '0619']}
    """
    missing_data = {}

    for column in dataframe.columns:

        if date_index:
            mask = dataframe[column].isnull()
            missing_index = dataframe[mask].index.strftime(date_format)
            missing_list = missing_index.values.tolist()
        else:
            mask = dataframe[column].isnull()
            missing_index = dataframe[mask].index
            missing_list = missing_index.values.tolist()

        missing_data[column] = missing_list
    return missing_data
