# 1. Series is a kind of data struct for index a series of data.

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8]) # create a series with ascending order.
s1 = pd.Series([2, 1, 3, 4, 5, 6], index=s)  # create a custom series order by a defined series.
print(s, s1)
