#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def rolldice(x):
    dice_tray=()
    for i in range(x):
        dice_tray=dice_tray+(np.random.randint(1,7),)
    return dice_tray

def order_dict(x):
    keys=list(x.keys())
    keys.sort()
    sorted_dict = {}
    for i in keys:
        sorted_dict[i]=x[i]
    return sorted_dict

def countdice(x):
    count = {}
    for i in x:
        if i in count.keys():
            count[i]=count[i]+1
        else:
            count[i]=1
    sorted_count=order_dict(count)
    return sorted_count
        
dice_set=rolldice(10000)
dice_count=countdice(dice_set)
#print(dice_set)
print(dice_count)


# In[62]:


print('a'>'b','b'>'a')


# In[ ]:




