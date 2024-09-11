#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)
# ### ROSARIO, Clifford James
# ### 2ECE-C
# 
# #### PROBLEM 2

# In[1]:


import pandas as pd
Cars=pd.read_csv("cars.csv")
Cars


# #### Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

# In[2]:


Cars.iloc[1::2]


# #### Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[3]:


Cars.loc[Cars['Model']=='Mazda RX4']


# #### How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# 

# In[4]:


Cars.loc[Cars['Model']=='Camaro Z28',['Model','cyl']]


# #### Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[5]:


Cars.loc[(Cars['Model'] == 'Mazda RX4 Wag')|(Cars['Model'] == 'Ford Pantera L')|(Cars['Model'] == 'Honda Civic'), ['Model','cyl', 'gear']]

