#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Read in json with all 2000 laureates from our public API

import requests
url = "https://api.nobelprize.org/2.0/laureates?nobelPrizeYear=2000"
response = requests.get(url)
json = response.json()

# Print the names of all laureates who are persons (have a knownName)

for laureate in json['laureates']:
    if 'knownName' in laureate:
        print ( laureate['knownName']['en'] )


# In[ ]:




