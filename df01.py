# 1. DataFrame is a kind of data struct for keep 2D dataset by Series.
# 2. If some column data is missed in a row, DataFrame may complete it if possible.

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8, 'a', 'b'])

df = pd.DataFrame({'A': s,
                   'B': 1.,
                   'C': False,
                   'D': pd.Timestamp('20130102'),
                   'E': 23,
                   'F': 'foo'})
print('all')
print(df)
print('head')
print(df.head())  # default: first 5 rows
print('tail')
print(df.tail())  # default: last 5 rows
print('index')
print(df.index)
print('columns')
print(df.columns)
print('to_numpy')
print(df.to_numpy())  # convert DataFrame to be a 2D array.
print('describe')
print(df.describe())  # statistics about number columns
print('sort')
print(df.sort_index(ascending=False))  # sort by reversed index
print(df.sort_values(by='E'))  # sort by a column
print('select')
print(df['D'])  # select a column
print(df[2:4])  # select rows by range
print(df.loc[s[2]])  # select a row by index value
print(df.loc[s[1:3], ['A', 'B']])  # select some columns from a range of rows
print(df.loc[s[2], 'A'], df.at[s[2], 'A'])  # get a value by its location
print(df.iloc[3])  # select a row by index
print(df.iloc[3, 1:3])  # select a slice
print(df.iloc[2, 1], df.iat[2, 1])  # get a value by its index location
