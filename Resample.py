#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def random_sample(x,y,n):
    import numpy as np
    np.random.seed(42)
    resample_x = []; resample_y =[]
    import random
    t = np.arange(1,len(x),1)
    nx= random.sample(list(t), n)
    for i in nx:
        resample_x.append(x[i])
        resample_y.append(y[i])
    return (resample_x, resample_y)
    

