#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm


# In[ ]:


data = pd.read_csv('/content/drive/MyDrive/compressed_dataset.csv.zip',compression='zip',index_col=False)


# In[ ]:


data["date_time"] = pd.to_datetime(data['timestamp'], unit="ms")
data['day'] = pd.to_datetime(data['date_time'].dt.strftime('%Y-%m-%d'))
data['weekday'] = data['day'].dt.day_of_week


# In[ ]:


data['viewer_type']=data['viewer_type'].astype('category').cat.codes


# In[ ]:


cols = ['engagement','viewer_id','event_id','customer_id','timestamp','country_id','city_id','viewer_type','qoe']
df = data[cols]


# In[ ]:


sns.set(rc={'figure.figsize':(20,10)})
sns.heatmap(df.corr(),annot = True)

