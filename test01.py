import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)

df = pd.DataFrame()

print(df)

df2 = pd.DataFrame({'A': 1.,
                    # 'B': pd.Timestamp('20130102'),
                    # 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    # 'D': np.array([3] * 4, dtype='int32'),
                    # 'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

print(df2)