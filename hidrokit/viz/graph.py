"""Visualize dataframe with graph/plot.
"""

import matplotlib.pyplot as plt


def subplots(dataframe, ncols=3, nrows=5, figsize=None):
    """Plot all numeric column in one figure with datetime index.

    Parameters
    ----------
    dataframe : DataFrame
        DataFrame consist of numeric column only.
    ncols : int, optional
        Number of column subplots, by default 3
    nrows : int, optional
        Number of row subplots, by default 5
    figsize : tuple of int, optional
        Figure size, by default None
    """
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize,
                             sharex=True)

    index = 0
    column_name = dataframe.columns

    for row in range(nrows):
        for col in range(ncols):
            if ncols == 1:
                position = (row)
            else:
                position = (row, col)

            dataframe[column_name[index]].plot(ax=axes[position])
            axes[position].set_title(column_name[index],
                                     loc='right' if ncols == 1 else 'center')

            if index < len(column_name) - 1:
                index += 1
            else:
                break

    plt.tight_layout()

    return fig, axes
