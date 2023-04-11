#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries below
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt


# In[2]:


pwd


# In[3]:


#load csv data using pandas
df = pd.read_csv('C:/Users/Delaney/Documents/Beaver Meadows Data Template.csv')
df


# In[4]:


# filter by upper and lower dam
upper = df[df['Site_Location'] == 'Upper']
lower = df[df['Site_Location'] == 'Lower']
#filter by the pool, side channel, below confluence, and main channel
Upper_Below_Con = upper[upper['Site_Information'] == 'Below Confluence']
Upper_Main_Chan = upper[upper['Site_Information'] == 'Main Channel']
Upper_Pool = upper[upper['Site_Information'] == 'Pool']
Upper_Side_Chan = upper[upper['Site_Information'] == 'Side Channel']

Lower_Below_Con = lower[lower['Site_Information'] == 'Below Confluence']
Lower_Main_Chan = lower[lower['Site_Information'] == 'Main Channel']
Lower_Pool = lower[lower['Site_Information'] == 'Pool']
Lower_Side_Chan = lower[lower['Site_Information'] == 'Side Channel']


# In[5]:


#upper pool, side channel, and main channel with Temp_C, EC, PO4_mgL, NOx_mgL, and NH4

#upper features with temp
Upper_Temp_Below_Con = Upper_Below_Con[['Temp _C']]
Upper_Temp_Main_Chan = Upper_Main_Chan[['Temp _C']]
Upper_Temp_Side_Chan = Upper_Side_Chan[['Temp _C']]
Upper_Temp_Pool = Upper_Pool[['Temp _C']]

#upper features and EC
Upper_EC_Below_Con = Upper_Below_Con[['EC']]
Upper_EC_Main_Chan = Upper_Main_Chan[['EC']]
Upper_EC_Side_Chan = Upper_Side_Chan[['EC']]
Upper_EC_Pool = Upper_Pool[['EC']]

#upper features and PO4_mgL
Upper_PO4_Below_Con = Upper_Below_Con[['PO4_mgL']]
Upper_PO4_Main_Chan = Upper_Main_Chan[['PO4_mgL']]
Upper_PO4_Side_Chan = Upper_Side_Chan[['PO4_mgL']]
Upper_PO4_Pool = Upper_Pool[['PO4_mgL']]

#upper features and NOx_mgL
Upper_NOx_Below_Con = Upper_Below_Con[['NOx_mgL']]
Upper_NOx_Main_Chan = Upper_Main_Chan[['NOx_mgL']]
Upper_NOx_Side_Chan = Upper_Side_Chan[['NOx_mgL']]
Upper_NOx_Pool = Upper_Pool[['NOx_mgL']]

#upper features and NH4
Upper_NH4_Below_Con = Upper_Below_Con[['NH4']]
Upper_NH4_Main_Chan = Upper_Main_Chan[['NH4']]
Upper_NH4_Side_Chan = Upper_Side_Chan[['NH4']]
Upper_NH4_Pool = Upper_Pool[['NH4']]


# In[6]:


#lower pool, side channel, and main channel with Temp_C, EC, PO4_mgL, NOx_mgL, and NH4
#lower features with temp
Lower_Temp_Below_Con = Lower_Below_Con[['Temp _C']]
Lower_Temp_Main_Chan = Lower_Main_Chan[['Temp _C']]
Lower_Temp_Side_Chan = Lower_Side_Chan[['Temp _C']]
Lower_Temp_Pool = Lower_Pool[['Temp _C']]

#lower features and EC
Lower_EC_Below_Con = Lower_Below_Con[['EC']]
Lower_EC_Main_Chan = Lower_Main_Chan[['EC']]
Lower_EC_Side_Chan = Lower_Side_Chan[['EC']]
Lower_EC_Pool = Lower_Pool[['EC']]

#lower features and PO4_mgL
Lower_PO4_Below_Con = Lower_Below_Con[['PO4_mgL']]
Lower_PO4_Main_Chan = Lower_Main_Chan[['PO4_mgL']]
Lower_PO4_Side_Chan = Lower_Side_Chan[['PO4_mgL']]
Lower_PO4_Pool = Lower_Pool[['PO4_mgL']]

#lower features and NOx_mgL
Lower_NOx_Below_Con = Lower_Below_Con[['NOx_mgL']]
Lower_NOx_Main_Chan = Lower_Main_Chan[['NOx_mgL']]
Lower_NOx_Side_Chan = Lower_Side_Chan[['NOx_mgL']]
Lower_NOx_Pool = Lower_Pool[['NOx_mgL']]

#lower features and NH4
Lower_NH4_Below_Con = Lower_Below_Con[['NH4']]
Lower_NH4_Main_Chan = Lower_Main_Chan[['NH4']]
Lower_NH4_Side_Chan = Lower_Side_Chan[['NH4']]
Lower_NH4_Pool = Lower_Pool[['NH4']]


# In[7]:


#run independent ttest for upper and lower feature and measurement
stats.ttest_ind(Upper_PO4_Below_Con,
               Lower_PO4_Below_Con)


# In[8]:


stats.ttest_ind(Upper_NOx_Below_Con,
               Lower_NOx_Below_Con)


# In[9]:


stats.ttest_ind(Upper_NH4_Below_Con,
               Lower_NH4_Below_Con)


# In[10]:


stats.ttest_ind(Upper_Temp_Below_Con,
               Lower_Temp_Below_Con)


# In[11]:


stats.ttest_ind(Upper_EC_Below_Con,
               Lower_EC_Below_Con)


# In[12]:


stats.ttest_ind(Upper_PO4_Main_Chan,
               Lower_PO4_Main_Chan)


# In[13]:


stats.ttest_ind(Upper_NOx_Main_Chan,
               Lower_NOx_Main_Chan)


# In[14]:


stats.ttest_ind(Upper_NH4_Main_Chan,
               Lower_NH4_Main_Chan)


# In[15]:


stats.ttest_ind(Upper_Temp_Main_Chan,
               Lower_Temp_Main_Chan)


# In[16]:


stats.ttest_ind(Upper_EC_Main_Chan,
               Lower_EC_Main_Chan)


# In[17]:


stats.ttest_ind(Upper_PO4_Side_Chan,
               Lower_PO4_Side_Chan)


# In[18]:


stats.ttest_ind(Upper_NOx_Side_Chan,
               Lower_NOx_Side_Chan)


# In[19]:


stats.ttest_ind(Upper_NH4_Side_Chan,
               Lower_NH4_Side_Chan)


# In[20]:


stats.ttest_ind(Upper_Temp_Side_Chan,
               Lower_Temp_Side_Chan)


# In[21]:


stats.ttest_ind(Upper_EC_Side_Chan,
               Lower_EC_Side_Chan)


# In[22]:


stats.ttest_ind(Upper_PO4_Pool,
               Lower_PO4_Pool)


# In[23]:


stats.ttest_ind(Upper_NOx_Pool,
               Lower_NOx_Pool)


# In[24]:


stats.ttest_ind(Upper_NH4_Pool,
               Lower_NH4_Pool)


# In[25]:


stats.ttest_ind(Upper_Temp_Pool,
               Lower_Temp_Pool)


# In[26]:


stats.ttest_ind(Upper_EC_Pool,
               Lower_EC_Pool)

