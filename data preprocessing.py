#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Aim : Data preprocessing
# Name: Pragati Bindod
# Roll no:15


# In[24]:


import numpy as np
import pandas as pd
import os
import statistics


# In[3]:


data=pd.read_csv("C:\\Users\\PRAGATI BINDOD\\Downloads\\archive (1).zip")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.size


# In[8]:


data.describe()


# In[9]:


data.ndim


# In[10]:


data.info()


# In[11]:


data.shape


# In[12]:


#check the missing value by record
data.isna()


# In[13]:


#check missing value by column
data.isna().any()


# In[14]:


#check the number of missing value
data.isna().sum()


# In[18]:


data=data.dropna()


# In[19]:


#to fill missing value by mean value
data["Age"].fillna(29.699118)


# In[20]:


data.isna()


# In[21]:


data.isna().sum()


# In[22]:


data.shape


# In[ ]:





# In[ ]:




