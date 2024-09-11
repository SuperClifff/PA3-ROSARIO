#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3: PYTHON DATA ANALYSIS (PANDAS)
# ### ROSARIO, Clifford James
# ### 2ECE-C
# 
# #### PROBLEM 1
# #### Load the corresponding .csv file into a data frame named cars using pandas

# In[1]:


import pandas as pd 
Cars=pd.read_csv("cars.csv")
Cars


# Type *Markdown* and LaTeX:  𝛼2

# In[2]:


Cars.head(6)


# In[3]:


Cars.tail()

