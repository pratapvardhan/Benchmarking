'''
Benchmarking pandas empty vs len nv len on index for empty dataframe
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10000, 4), columns=list('ABCD'))

def empty(df):
    if df.empty:
        a=0
    else:
        a=1
    return a

def lenz(df):
    if len(df)==0:
        a=0
    else:
        a=1
    return a

def lenzi(df):
    if len(df.index)==0:
        a=0
    else:
        a=1
    return a

'''
%timeit empty(df)
%timeit lenz(df)
%timeit lenzi(df)

10000 loops, best of 3: 13.9 µs per loop
100000 loops, best of 3: 2.34 µs per loop
1000000 loops, best of 3: 695 ns per loop

len on index seems to be the best
'''
