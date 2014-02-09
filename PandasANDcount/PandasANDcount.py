#-------------------------------------------------------------------------------
# Name:        Pandas operations test
# Author:      Pratap Vardhan
# Created:     02-11-2013
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd

import time
x1=[];x2=[];

t_xlen = range(1,2*10**4,10**2)
for xlen in t_xlen:
    tb = pd.DataFrame(np.random.randint(0,5,size=(xlen,2)),columns=['w1','w2'])
    t0=time.time()
    v1 = len(tb[(tb['w1']>0) & (tb['w2']>0)]) # Type1
    t1=time.time()
    v2 = int(sum((tb['w1']>0) & (tb['w2']>0))) # Type2
    #v2 = (sum((tb['w1']>0) & (tb['w2']>0))) # same as Type2
    #v2 = int(((tb['w1']>0) & (tb['w2']>0)).sum()) # as slow as Type1
    t2=time.time()
    x1.append(t1-t0)
    x2.append(t2-t1)

import matplotlib.pyplot as plt
plt.plot(t_xlen, x1,'b',label='Type-1 Method')
plt.plot(t_xlen, x2,'r',label='Type-2 Method')
plt.xlabel('Length of DataFrame')
plt.ylabel('Time (in sec)')
plt.title('Pandas DataFrame - Count on AND operation')
plt.legend(loc='upper left')
#plt.show()
plt.savefig('PandasANDCount.png')
