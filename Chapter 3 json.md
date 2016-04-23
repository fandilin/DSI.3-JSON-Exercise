

```python
import pandas as pd
import json
from pandas.io.json import json_normalize
```


```python
projects = pd.read_json('world_bank_projects.json')
projects["countryshortname"].value_counts().head(10)
```
####These are the 10 countries with the most projects.




    Indonesia             19
    China                 19
    Vietnam               17
    India                 16
    Yemen, Republic of    13
    Morocco               12
    Nepal                 12
    Bangladesh            12
    Africa                11
    Mozambique            11
    Name: countryshortname, dtype: int64




```python
data = json.load(open('world_bank_projects.json'))
themes = json_normalize(data,'mjtheme_namecode')
themes.groupby('code').describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>name</th>
    </tr>
    <tr>
      <th>code</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">1</th>
      <th>count</th>
      <td>38</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Economic management</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>33</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">10</th>
      <th>count</th>
      <td>216</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Rural development</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>202</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">11</th>
      <th>count</th>
      <td>250</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Environment and natural resources management</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>223</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">2</th>
      <th>count</th>
      <td>199</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Public sector governance</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>184</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">3</th>
      <th>count</th>
      <td>15</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Rule of law</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>12</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">4</th>
      <th>count</th>
      <td>146</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Financial and private sector development</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>130</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">5</th>
      <th>count</th>
      <td>77</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Trade and integration</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>72</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">6</th>
      <th>count</th>
      <td>168</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Social protection and risk management</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">7</th>
      <th>count</th>
      <td>130</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Social dev/gender/inclusion</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>119</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">8</th>
      <th>count</th>
      <td>210</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Human development</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>197</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">9</th>
      <th>count</th>
      <td>50</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>2</td>
    </tr>
    <tr>
      <th>top</th>
      <td>Urban development</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>47</td>
    </tr>
  </tbody>
</table>
</div>




```python
themes['name'].value_counts()
```
####These are the project themes in order of project counts, with missing theme names counted as a seperate theme. "Rule of law" is the theme with the fewest projects.




    Environment and natural resources management    223
    Rural development                               202
    Human development                               197
    Public sector governance                        184
    Social protection and risk management           158
    Financial and private sector development        130
                                                    122
    Social dev/gender/inclusion                     119
    Trade and integration                            72
    Urban development                                47
    Economic management                              33
    Rule of law                                      12
    Name: name, dtype: int64




```python
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
```


```python
filled = pd.concat([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]).sort_index()
filled['name'].value_counts()
```
####These are the project themes in order of project counts. "Rule of law" is still the theme with fewest projects.




    Environment and natural resources management    250
    Rural development                               216
    Human development                               210
    Public sector governance                        199
    Social protection and risk management           168
    Financial and private sector development        146
    Social dev/gender/inclusion                     130
    Trade and integration                            77
    Urban development                                50
    Economic management                              38
    Rule of law                                      15
    Name: name, dtype: int64


