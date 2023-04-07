# Field-Methods-T-test
Here is my T-test code for Spring 2023 Field Methods. This code runs an independent t-test for nitrate, phospate, ammonium, electrical conductivity, and temperature in Celsius.
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import scipy.stats as stats
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('C:/Users/Delaney/Documents/Quality_Beaver_Meadows_Data_Template.csv')
df.info()


# In[3]:


stats.ttest_ind(df['PO4_mgL'][df['Site_Location'] == 'Upper'],
                df['PO4_mgL'][df['Site_Location'] == 'Lower'])


# In[4]:


stats.ttest_ind(df['NOx_mgL'][df['Site_Location'] == 'Upper'],
                df['NOx_mgL'][df['Site_Location'] == 'Lower'])


# In[5]:


stats.ttest_ind(df['NH4'][df['Site_Location'] == 'Upper'],
                df['NH4'][df['Site_Location'] == 'Lower'])


# In[6]:


stats.ttest_ind(df['EC'][df['Site_Location'] == 'Upper'],
                df['EC'][df['Site_Location'] == 'Lower'])


# In[7]:


stats.ttest_ind(df['Temp _C'][df['Site_Location'] == 'Upper'],
                df['Temp _C'][df['Site_Location'] == 'Lower'])


# In[8]:


sampling_difference1 = df['PO4_mgL'][df['Site_Location'] == 'Upper'].values -                        df['PO4_mgL'][df['Site_Location'] == 'Lower'].values
                      
sampling_difference2 = df['NOx_mgL'][df['Site_Location'] == 'Upper'].values -                        df['NOx_mgL'][df['Site_Location'] == 'Lower'].values
                     
sampling_difference3 = df['NH4'][df['Site_Location'] == 'Upper'].values -                        df['NH4'][df['Site_Location'] == 'Lower'].values
                      
sampling_difference4 = df['EC'][df['Site_Location'] == 'Upper'].values -                        df['EC'][df['Site_Location'] == 'Lower'].values
                     
sampling_difference5 = df['Temp _C'][df['Site_Location'] == 'Upper'].values -                        df['Temp _C'][df['Site_Location'] == 'Lower'].values


# In[9]:


fig = plt.figure(figsize= (20, 10))
ax = fig.add_subplot(111)
normality_plot, stat = stats.probplot(sampling_difference1, plot= plt, rvalue= True)
ax.set_title("Probability plot of PO4_mgL", fontsize= 20)
ax.set


# In[10]:


fig = plt.figure(figsize= (20, 10))
ax = fig.add_subplot(111)
normality_plot, stat = stats.probplot(sampling_difference2, plot= plt, rvalue= True)
ax.set_title("Probability plot of NOx_mgL", fontsize= 20)
ax.set


# In[11]:


fig = plt.figure(figsize= (20, 10))
ax = fig.add_subplot(111)
normality_plot, stat = stats.probplot(sampling_difference3, plot= plt, rvalue= True)
ax.set_title("Probability plot of NH4", fontsize= 20)
ax.set


# In[12]:


fig = plt.figure(figsize= (20, 10))
ax = fig.add_subplot(111)
normality_plot, stat = stats.probplot(sampling_difference4, plot= plt, rvalue= True)
ax.set_title("Probability plot of EC", fontsize= 20)
ax.set


# In[13]:


fig = plt.figure(figsize= (20, 10))
ax = fig.add_subplot(111)
normality_plot, stat = stats.probplot(sampling_difference5, plot= plt, rvalue= True)
ax.set_title("Probability plot of Temp_C", fontsize= 20)
ax.set
