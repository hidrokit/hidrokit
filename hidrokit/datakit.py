"""Toolkit for data exploration.
"""


def dict_null_data(dataset, date=True, date_format='%Y/%m/%d'):
    """Retrieve information of null rows inside DataFrame.

    Return dictionary contains columns name and list of the index
    null row. Index can be customized if index is
    pd.Timestamp object.

    Parameters
    ----------
    dataset : DataFrame
        DataFrame contains some null values
    date : bool, optional
        Set True if index is pd.Timestamp object, by default
        True
    date_format : str, optional
        Format index to strftime() style, by default '%Y/%m/%d'

    Returns
    -------
    dict
        Dictionary contains columns name and list of strings the null row.

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
    >>> dict_null_data(A, date=False)
    {'A': [1], 'B': [2], 'C': [], 'D': [0, 1], 'E': [], 'F': [0, 2]}

    Using date-index:

    >>> date_index = pd.date_range("20190617", "20190619")
    >>> A.set_index(date_index, inplace=True)
    ... A
                  A    B  C    D  E    F    
    2019-06-17  1.0  3.0  4  NaN  2  NaN
    2019-06-18  NaN  2.0  3  NaN  1  4.0
    2019-06-19  2.0  NaN  1  3.0  4  NaN
    >>> dict_null_data(A, date=True, date_format="%m%d")
    {'A': ['0618'],
    'B': ['0619'],
    'C': [],
    'D': ['0617', '0618'],
    'E': [],
    'F': ['0617', '0619']}    
    """
    loss_row = {}

    for column in dataset.columns:
        if date:
            idx_null = dataset[dataset[column].isnull()].index.strftime(
                date_format).values.tolist()
        else:
            idx_null = dataset[dataset[column].isnull()].index.values.tolist()
        loss_row[column] = idx_null

    return loss_row
