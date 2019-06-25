"""Visualize dataframe with table.
"""

_monthDict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
_monthDictID = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun',
                7: 'Jul', 8: 'Agu', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Des'}


def pivot(dataframe=None, column=None, month_format=None):
    column = dataframe.columns[0] if not column else column

    pivot_table = dataframe.assign(
        month=dataframe.index.month, day=dataframe.index.day
    ).pivot(
        values=column, columns='month', index='day'
    )

    if month_format:
        if month_format.lower() == 'id':
            pivot_table.columns = pivot_table.columns.map(_monthDictID)
        elif month_format.lower() == 'en':
            pivot_table.columns = pivot_table.columns.map(_monthDict)

    return pivot_table
