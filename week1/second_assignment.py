import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

df_can = pd.ExcelFile('Canada.xlsx')
df_can = df_can.parse('Canada by Citizenship', skiprows=20, skip_footer=2)

#Droping unnecessary columns
#axis = 0 dropping rows axis = 1 dropping columns
df_can.drop(['Type','Coverage','AREA','REG','DEV'], axis = 1, inplace = True)

#Renaming columns
df_can.rename(columns = {'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace = True)

#Adding total column
df_can['Total'] = df_can.sum(axis = 1)

df_can.columns = list(map(str, df_can.columns))

#Setting index
df_can.set_index('Country', inplace=True)

years = list(map(str, range(1980,2014)))

plt.style.use(['ggplot'])

df_can.sort_values(['Total'], ascending=False, inplace=True)

df_canada = df_can
df_canada.drop(['Total'], axis=0, inplace=True)

df_top5 = df_canada.head()

df_top5 = df_top5[years].transpose()

df_top5.index = df_top5.index.map(int)

#df_top5.plot(kind='area', alpha=0.5, stacked=False, figsize=(20,10))
# ax = df_top5.plot(kind='area', alpha=0.35, figsize=(20, 10))

# ax.set_title('Immigration Trend of Top 5 Countries')
# ax.set_ylabel('Number of Immigrants')
# ax.set_xlabel('Years')

# #plt.title('Immigrants from top five nations')
# plt.show()

df_low5 = df_canada.tail(5)
df_low5 = df_low5[years].transpose()
df_low5.index = df_low5.index.map(int)
# df_low5.plot(kind='area', stacked=False, alpha=0.45, figsize=(20,10))

# plt.title("Least 5 immigrants")
# plt.xlabel("Years")
# plt.ylabel("Number of immigrants")

ax = df_low5.plot(kind='area', stacked=False, alpha=0.55, figsize=(20,10))

ax.set_title("Least 5 immigrants")
ax.set_xlabel('Years')
ax.set_ylabel('Number of immigrants')

plt.show()