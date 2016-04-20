import pandas as pd
import json
from pandas.io.json import json_normalize

projects = pd.read_json('world_bank_projects.json')
projects["countryshortname"].value_counts().head(10)
#These are the 10 countries with the most projects.
#Indonesia             19
#China                 19
#Vietnam               17
#India                 16
#Yemen, Republic of    13
#Morocco               12
#Nepal                 12
#Bangladesh            12
#Africa                11
#Mozambique            11

data = json.load(open('world_bank_projects.json'))
themes = json_normalize(data,'mjtheme_namecode')
themes.groupby('code').describe()

themes['name'].value_counts()
#The theme names in order of project counts. There are 122 project theme codes missing a corresponding name. "Rule of law" is the least popular theme.
#Environment and natural resources management    223
#Rural development                               202
#Human development                               197
#Public sector governance                        184
#Social protection and risk management           158
#Financial and private sector development        130
#                                                122
#Social dev/gender/inclusion                     119
#Trade and integration                            72
#Urban development                                47
#Economic management                              33
#Rule of law                                      12

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

filled = pd.concat([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]).sort_index()
filled

filled['name'].value_counts()
#These are the theme names in order of project counts with missing names filled in. "Rule of law" is still the least popular theme.
#Environment and natural resources management    250
#Rural development                               216
#Human development                               210
#Public sector governance                        199
#Social protection and risk management           168
#Financial and private sector development        146
#Social dev/gender/inclusion                     130
#Trade and integration                            77
#Urban development                                50
#Economic management                              38
#Rule of law                                      15
