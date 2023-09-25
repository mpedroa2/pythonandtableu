#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 18:58:10 2023

@author: michaelpedro
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:04:24 2023

@author: michaelpedro
"""

import pandas as pd
 
# file_name = pd.read_csv('file.csv') <-- format of read_csv
 

data = pd.read_csv('transaction.csv') 

data = pd.read_csv('transaction.csv', sep=';')


#summary of the data
data.info() 

#Working with calculations

#Defining Variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6


#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem


ProfitPerTransaction = NumberofItemsPurchased*ProfitPerItem
CostPerTransaction = NumberofItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased*SellingPricePerItem

#CostPerTransaction Cloumn Calculation

#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']


CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberofItemsPurchased

#adding a new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] )/data['CostPerTransaction']

data['Markup'] = ( data['ProfitPerTransaction'] )/data['CostPerTransaction']


#Rounding Markup


roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

#Combining Data fields 

my_name = 'Mike' + 'Pedro'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = data['Day']+'-'


#checking columns data type
print(data['Day'].dtype)

#Change Columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5] #last 5 rows

data.head(5)  #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2]  #brings in 4 row, 2nd column


#using split to split client keywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand =True)

#creating new columns for the split columns for the Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]


#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')


#using the lower function to change items to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset 

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')


#dropping columns 

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)


#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)


