#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm


# In[ ]:


data = pd.read_csv('/content/drive/MyDrive/compressed_dataset.csv.zip',compression='zip',index_col=False)
data["date_time"] = pd.to_datetime(data['timestamp'], unit="ms")
data['day'] = pd.to_datetime(data['date_time'].dt.strftime('%Y-%m-%d'))
data['weekday'] = data['day'].dt.day_of_week
data.head()


# In[3]:


df = pd.DataFrame({'engagement':data['engagement'], 'event_id':data['event_id'], 'viewer_id':data['viewer_id'], 'country_id':data['country_id'],'weekday':data['weekday'],'timestamp':data['timestamp']})
df.head()


# In[4]:


events = df['event_id'].drop_duplicates().tolist()
number_of_viewers = []
for event in tqdm(events):
  number_of_viewers.append(df.loc[data['event_id'] == event]['viewer_id'].drop_duplicates().count())

event_viewers = dict(zip(events,number_of_viewers))
df['Number_Of_Viewers'] = df['event_id'].map(event_viewers)
df.head()


# In[5]:


events = df['event_id'].drop_duplicates().tolist()
duration = []
for event in tqdm(events):
  l = df.loc[df['event_id'] == event]['timestamp'].tolist()
  l.sort()
  duration.append(l[-1] - l[0])
event_duration = dict(zip(events,duration))
df['Event_Duration'] = df['event_id'].map(event_duration)
df.head()


# In[39]:


temp = df[['viewer_id','timestamp', 'event_id']].groupby('viewer_id')
df.retention = 0
groups = temp.groups.keys()
for group in tqdm(groups):
  events = temp.get_group(group)[['timestamp','event_id']].groupby('event_id')
  keys = events.groups.keys()
  for key in keys:
    min_max = events.get_group(key).agg({'timestamp':['min','max']})
    min = min_max.iat[0,0]
    max = min_max.iat[1,0]
    df.loc[(df.viewer_id == group) & (df.event_id == key),'retention'] = max - min 


# In[8]:


sns.set(rc={'figure.figsize':(20,10)})
sns.heatmap(df.corr(),annot = True)

