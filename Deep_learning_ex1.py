#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import pandas as pd
import zipfile
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('/content/drive/MyDrive/compressed_dataset.csv.zip',compression='zip',index_col=False)
data["date_time"] = pd.to_datetime(data['timestamp'], unit="ms")
data['day'] = pd.to_datetime(data['date_time'].dt.strftime('%Y-%m-%d'))
data['weekday'] = data['day'].dt.day_of_week
data.head()


# In[ ]:


customers = data['customer_id'].drop_duplicates().tolist()
for customer in customers:
   data.loc[data['customer_id']== customer].sort_values(by='date_time')[['engagement','date_time']].plot(x = "date_time", y = "engagement", title = (customer), xlabel = ("date_time"), ylabel = ("engagement")) 


# In[ ]:


data2 = data.groupby(['customer_id' , 'day'], as_index=False).agg({'engagement': ['mean','std']})
data2.columns = ['customer_id', 'day','engagement_mean','engagement_std']

customers = data2['customer_id'].drop_duplicates().tolist()
for customer in customers:
    data2.loc[data2['customer_id']== customer].sort_values(by='day')[['engagement_mean','day']].plot(x = "day", y = "engagement_mean", title = (customer), xlabel = ("day"), ylabel = ("engagement_mean"))
    data2.loc[data2['customer_id']== customer].sort_values(by='day')[['engagement_std','day']].plot(x = "day", y = "engagement_std", title = (customer), xlabel = ("day"), ylabel = ("engagement_std"))


# In[ ]:


countries = data['country_id'].drop_duplicates().tolist()
for country in countries:
   data.loc[data['country_id']== country].sort_values(by='date_time')[['engagement','date_time']].plot(x = "date_time", y = "engagement", title = (country), xlabel = ("date_time"), ylabel = ("engagement")) 


# In[ ]:


data2 = data.groupby(['country_id' , 'day'], as_index=False).agg({'engagement': ['mean','std']})
data2.columns = ['country_id', 'day','engagement_mean','engagement_std']

countries = data2['country_id'].drop_duplicates().tolist()
for country in countries:
    data2.loc[data2['country_id']== country].sort_values(by='day')[['engagement_mean','day']].plot(x = "day", y = "engagement_mean", title = (country), xlabel = ("day"), ylabel = ("engagement_mean"))
    data2.loc[data2['country_id']== country].sort_values(by='day')[['engagement_std','day']].plot(x = "day", y = "engagement_std", title = (country), xlabel = ("day"), ylabel = ("engagement_std"))


# In[ ]:


cities = data['city_id'].drop_duplicates().tolist()
for city in cities:
   data.loc[data['city_id']== city].sort_values(by='date_time')[['engagement','date_time']].plot(x = "date_time", y = "engagement", title = (city), xlabel = ("date_time"), ylabel = ("engagement"))


# In[ ]:


data2 = data.groupby(['city_id' , 'day'], as_index=False).agg({'engagement': ['mean','std']})
data2.columns = ['city_id', 'day','engagement_mean','engagement_std']

cities = data2['city_id'].drop_duplicates().tolist()
for city in countries:
    data2.loc[data2['city_id']== city].sort_values(by='day')[['engagement_mean','day']].plot(x = "day", y = "engagement_mean", title = (city), xlabel = ("day"), ylabel = ("engagement_mean"))
    data2.loc[data2['city_id']== city].sort_values(by='day')[['engagement_std','day']].plot(x = "day", y = "engagement_std", title = (city), xlabel = ("day"), ylabel = ("engagement_std"))

