#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime
import pandas as pd
import zipfile
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore', '.*do not.*', )


# In[3]:


with zipfile.ZipFile("/content/drive/MyDrive/Colab Notebooks/compressed_dataset.csv.zip") as z:
    with z.open("compressed_dataset.csv") as f:
      df = pd.read_csv(f)


# In[4]:


df["date_time"] = pd.to_datetime(df['timestamp'], unit="ms")
df['day'] = pd.to_datetime(df['date_time'].dt.strftime('%Y-%m-%d'))
df.head()


# In[ ]:


customers = df['customer_id'].drop_duplicates().tolist()
for customer in customers:
   df.loc[df['customer_id']== customer].sort_values(by='date_time')[['qoe','date_time']].plot(x = "date_time", y = "qoe", title = (customer), xlabel = ("date_time"), ylabel = ("qoe")) 


# In[28]:


df2 = df.groupby(['customer_id' , 'day'], as_index=False).agg({'qoe': ['mean','std']})
df2.columns = ['customer_id', 'day','qoe_mean','qoe_std']

customers = df2['customer_id'].drop_duplicates().tolist()
for customer in customers:
    df2.loc[df2['customer_id']== customer].sort_values(by='day')[['qoe_mean','day']].plot(x = "day", y = "qoe_mean", title = (customer), xlabel = ("day"), ylabel = ("qoe_mean"))
    df2.loc[df2['customer_id']== customer].sort_values(by='day')[['qoe_std','day']].plot(x = "day", y = "qoe_std", title = (customer), xlabel = ("day"), ylabel = ("qoe_std"))


# In[ ]:


countries = df['country_id'].drop_duplicates().tolist()
for country in countries:
   df.loc[df['country_id']== country].sort_values(by='date_time')[['qoe','date_time']].plot(x = "date_time", y = "qoe", title = (country), xlabel = ("date_time"), ylabel = ("qoe")) 


# In[29]:


df2 = df.groupby(['country_id' , 'day'], as_index=False).agg({'qoe': ['mean','std']})
df2.columns = ['country_id', 'day','qoe_mean','qoe_std']

countries = df2['country_id'].drop_duplicates().tolist()
for country in countries:
    df2.loc[df2['country_id']== country].sort_values(by='day')[['qoe_mean','day']].plot(x = "day", y = "qoe_mean", title = (country), xlabel = ("day"), ylabel = ("qoe_mean"))
    df2.loc[df2['country_id']== country].sort_values(by='day')[['qoe_std','day']].plot(x = "day", y = "qoe_std", title = (country), xlabel = ("day"), ylabel = ("qoe_std"))


# In[ ]:


cities = df['city_id'].drop_duplicates().tolist()
for city in cities:
   df.loc[df['city_id']== city].sort_values(by='date_time')[['qoe','date_time']].plot(x = "date_time", y = "qoe", title = (city), xlabel = ("date_time"), ylabel = ("qoe"))


# In[31]:


df2 = df.groupby(['city_id' , 'day'], as_index=False).agg({'qoe': ['mean','std']})
df2.columns = ['city_id', 'day','qoe_mean','qoe_std']

cities = df2['city_id'].drop_duplicates().tolist()
for city in countries:
    df2.loc[df2['city_id']== city].sort_values(by='day')[['qoe_mean','day']].plot(x = "day", y = "qoe_mean", title = (city), xlabel = ("day"), ylabel = ("qoe_mean"))
    df2.loc[df2['city_id']== city].sort_values(by='day')[['qoe_std','day']].plot(x = "day", y = "qoe_std", title = (city), xlabel = ("day"), ylabel = ("qoe_std"))


# # New Section
