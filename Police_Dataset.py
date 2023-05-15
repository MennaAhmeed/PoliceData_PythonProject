#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


data=pd.read_csv(r'C:\Users\Dell\Downloads\Police Data.csv')


# In[22]:


data


# In[23]:


#Q. 1) Instruction ( For Data Cleaning ) - Remove the column that only contains missing values.


# In[24]:


data.isnull().sum()


# In[26]:


data.drop(columns='country_name',inplace=True)  #answer


# In[27]:


data


# In[28]:


#Q. 2) Question ( Based on Filtering + Value Counts ) - For Speeding , were Men or Women stopped more often ? 


# In[29]:


data[data.violation=='Speeding'].driver_gender.value_counts()  #answer


# In[30]:


#Q. 3) Question ( Groupby ) - Does gender affect who gets searched during a stop ?


# In[31]:


data.groupby('driver_gender').search_conducted.sum()   #answer


# In[32]:


data.search_conducted.value_counts()


# In[33]:


#Q. 4) Question ( mapping + data-type casting ) - What is the mean stop_duration ?


# In[34]:


data['stop_duration'].value_counts()


# In[35]:


data['stop_duration']= data['stop_duration'].map({'0-15 Min' :7.5,'16-30 Min ':24,'30+ Min':45})  #answer


# In[36]:


data


# In[37]:


data['stop_duration'].mean()  #answer


# In[38]:


#Q. 5) Question ( Groupby , Describe ) - Compare the age distributions for each violation.


# In[40]:


data.groupby('violation').driver_age.describe()   #answer


# In[ ]:




