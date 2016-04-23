
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import numpy as np
from importlib import reload


# In[2]:

get_ipython().magic('matplotlib inline')
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
for i in range(100): 
    if i%2==0:
         y[i]=.2+np.sin(-np.pi+(2*np.pi)/100*i)
    else: 
        y[i]=-.2+np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[3]:

get_ipython().magic('matplotlib inline')
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
for i in range(100): 
    if i%3==0:
         y[i]=.2+np.sin(-np.pi+(2*np.pi)/100*i)
    else: 
        y[i]=-.2+np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[5]:

get_ipython().magic('matplotlib inline')
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
for i in range(100): 
    if i%7==0:
         y[i]=.2+np.sin(-np.pi+(2*np.pi)/100*i)
    else: 
        y[i]=np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[7]:




# In[16]:


get_ipython().magic('matplotlib inline')
fib=np.array([1,2,3,5,8,13,21,34,55,89])
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
for i in range(100): 
    for j in range(len(fib)): 
        if i==fib[j]:
            y[i]=.5+np.sin(-np.pi+(2*np.pi)/100*i)
            y[i-1]=.3+np.sin(-np.pi+(2*np.pi)/100*i)
            
    else: 
        y[i]=np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[19]:

get_ipython().magic('matplotlib inline')
fib2=np.array([1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21])
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
count=0
for i in range(100): 
    if i%2==0:
        y[i]=.1*fib2[count]+np.sin(-np.pi+(2*np.pi)/100*i)
        count+=1
    else: 
        y[i]=np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[20]:

get_ipython().magic('matplotlib inline')
fib2=np.array([1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21,1,2,3,5,8,13,21])
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
count=0
for i in range(100): 
    if i%2==0:
        y[i]=(-1)**count*.1*fib2[count]+np.sin(-np.pi+(2*np.pi)/100*i)
        count+=1
    else: 
        y[i]=np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[25]:

get_ipython().magic('matplotlib inline')
fib2=np.array([1,2,3,5,8,13,21,-1,-2,-3,-5,-8,-13,-21,1,2,3,5,8,13,21,-1,-2,-3,-5,-8,-13,-21,1,2,3,5,8,13,21,-1,-2,-3,-5,-8,-13,-21,1,2,3,5,8,13,21,-1,-2,-3,-5,-8,-13,-21,1,2,3,5,8,13,21,-1,-2,-3,-5,-8,-13,-21])
x=np.linspace(-np.pi,np.pi,100)
y=np.zeros(100)
count=0
for i in range(100): 
    if i%2==0:
        y[i]=.05*fib2[count]+np.sin(-np.pi+(2*np.pi)/100*i)
        count+=1
    else: 
        y[i]=np.sin(-np.pi+(2*np.pi)/100*i)
plt.plot(x,np.sin(x))
plt.plot(x,y)


# In[ ]:



