'''
Benchmarking pandas order vs algos.kth_smallest
'''

import pandas as pd

s = pd.Series(np.random.randint(100000, size=100000))
def fast_order(x, n):
    v = pd.algos.kth_smallest(x.values.astype(float), n)
    return x[x<=v]

s.order().head(10)
fast_order(s, 10).order()
'''

%timeit s.order().head(10)
%timeit fast_order(s, 10).order()

10 loops, best of 3: 61.4 ms per loop
100 loops, best of 3: 13.8 ms per loop

'''
