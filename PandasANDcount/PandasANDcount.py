#-------------------------------------------------------------------------------
# Name:        Pandas operations test
# Author:      Pratap Vardhan
# Created:     02-02-2014
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd

import time
x1=[];x2=[];

t_xlen = range(1,2*10**4,10**2)
for xlen in t_xlen:
    tb = pd.DataFrame(np.random.randint(0,5,size=(xlen,2)),columns=['w1','w2'])
    t0=time.time()
    v1 = len(tb[(tb['w1']>0) & (tb['w2']>0)]) # type1
    t1=time.time()
    v2 = int(sum((tb['w1']>0) & (tb['w2']>0))) # type2
    #v2 = (sum((tb['w1']>0) & (tb['w2']>0))) # same as type2
    #v2 = int(((tb['w1']>0) & (tb['w2']>0)).sum()) # as slow as type1
    t2=time.time()
    x1.append(t1-t0)
    x2.append(t2-t1)

import matplotlib.pyplot as plt
plt.plot(t_xlen, x1,'b',label='1nd Method')
plt.plot(t_xlen, x2,'r',label='2nd Method')
plt.xlabel('Length of DataFrame')
plt.ylabel('Time (in sec)')
plt.title('Pandas DataFrame - Count on AND operation')
plt.legend(loc='upper left')
plt.show()