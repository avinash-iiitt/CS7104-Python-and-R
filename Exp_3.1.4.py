'''
Date: 06.09.2024
Author: Avinash Singh
Title: Write a python script to handle missing data by filling missing values with mean or median of the column.
Also, demonstrate how to drop rows with missing data.
'''

#%%

import pandas as pd
import numpy as np


student = { 'roll' : [1, 2,3,4,5, 6],
            'name' : ['Ram', 'Shyam', 'Mohan', 'Satya', 'Gopi', 'Sonu'],
            'age' : [14, 15, 13, np.nan, 15, 16],
            'mark' : [85, 24, 67,90, 87, np.nan]
    }

df = pd.DataFrame(student)


print("Original DataFrame:")
print(df)

newdf = df.copy()
age_mean = newdf['age'].mean()
newdf['age'] = newdf['age'].fillna(age_mean)

mark_median = newdf['mark'].median()
newdf['mark'] = newdf['mark'].fillna(mark_median)


print("\nDataFrame with filled missing values:")
print(newdf)

df_dropped = df.dropna()

print("\nDataFrame with dropped rows:")
print(df_dropped)
