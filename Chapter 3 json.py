
# coding: utf-8

# In[1]:

import pandas as pd
import json
from pandas.io.json import json_normalize


# In[2]:

projects = pd.read_json('world_bank_projects.json')
projects["countryshortname"].value_counts().head(10)


# In[3]:

data = json.load(open('world_bank_projects.json'))
themes = json_normalize(data,'mjtheme_namecode')
themes.groupby('code').describe()


# In[4]:

themes['name'].value_counts()


# In[5]:

t1 = themes[themes['code']=='1'].replace({'name':''},{'name':'Economic management'})
t2 = themes[themes['code']=='2'].replace({'name':''},{'name':'Public sector governance'})
t3 = themes[themes['code']=='3'].replace({'name':''},{'name':'Rule of law'})
t4 = themes[themes['code']=='4'].replace({'name':''},{'name':'Financial and private sector development'})
t5 = themes[themes['code']=='5'].replace({'name':''},{'name':'Trade and integration'})
t6 = themes[themes['code']=='6'].replace({'name':''},{'name':'Social protection and risk management'})
t7 = themes[themes['code']=='7'].replace({'name':''},{'name':'Social dev/gender/inclusion'})
t8 = themes[themes['code']=='8'].replace({'name':''},{'name':'Human development'})
t9 = themes[themes['code']=='9'].replace({'name':''},{'name':'Urban development'})
t10 = themes[themes['code']=='10'].replace({'name':''},{'name':'Rural development'})
t11 = themes[themes['code']=='11'].replace({'name':''},{'name':'Environment and natural resources management'})


# In[6]:

filled = pd.concat([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]).sort_index()
filled


# In[7]:

filled['name'].value_counts()

