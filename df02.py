import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print('select')
print(df[df.A > 0])  # select * from df where df.A > 0
print(df[df > 0])  # select all positive values
print('----')
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2['E'].isin(['two', 'four']))  # check all rows if is in conditions
# select * from df where df.E in ('two', 'four')
print(df2[df2['E'].isin(['two', 'four'])])
print('----')
# assign a custom series from a series
s1 = pd.Series([2, 1, 3, 4, 5, 6], index=dates)
df2['F'] = s1  # assign a series as a column into the data frame
df2.at[dates[0], 'A'] = 500  # assign a value by labels
df2.iat[0, 1] = 350  # assign a value by locations
# assign an 1D array as a column into the data frame
df2.loc[:, 'D'] = np.array([5] * len(df2))
print(df2)
print('----')
df3 = df2.copy()
df3.drop(['E'], axis=1, inplace=True) # drop a column by labels/columns
df3[df3 > 0] = -df3 # replace values by locations if is in conditions
print(df3)
