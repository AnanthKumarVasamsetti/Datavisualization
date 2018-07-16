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
#Check for null values
vals = dict(df_can.isnull().sum())
for attr in vals.keys():
    if vals[attr] > 0:
        print(attr)

#Setting index
df_can.set_index('Country', inplace=True)


#Changing all columns to string
df_can.columns = list(map(str, df_can.columns))

years = list(map(str,range(1980, 2014)))

Asian_immigrants = df_can['Continent'] == 'Asia'


#Using ggplot style
plt.style.use(['ggplot'])

#Immigrants from Haiti
haiti = df_can.loc['Haiti', years]

haiti.index = haiti.index.map(int)

#Getting dataset for China and India from 1980 to 2013

df_ic = df_can.loc[['India', 'China'], years]


df_ic = df_ic.transpose()

df_ic.index = df_ic.index.map(int)

df_ic.plot(kind = 'line')

plt.title('Immigrants from India and China Year 1980-2013')
plt.xlabel('Years')
plt.ylabel('Number of immigrants')
plt.show()