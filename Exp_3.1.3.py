'''
Date: 06.09.2024
Author: Avinash Singh
Title: Write a python script to create a DataFrame from a dictionary of lists. Inspect the data frame by printing
the first 5 rows, compute the summary statistics and check for missing values. Select specific columns from
the dataframe by filtering rows based on one condition and using boolean indexing.
'''

#%%

import numpy as np
import pandas as pd

# Creating a DataFrame using Dictionary
student = { 'roll' : [1, 2,3,4,5, 6],
            'name' : ['Ram', 'Shyam', 'Mohan', 'Satya', 'Gopi', 'Sonu'],
            'age' : [14, 15, 13, np.nan, 15, 16],
            'mark' : [85, 24, 67,90, 87, 55]
    }
df = pd.DataFrame(student)
print("Student Dataframe: \n {}".format(df))

print('Top 5 rows :\n {}'.format(df.head()))

summary_stat = df.describe()
print("\nSummary Statistics:")
print(summary_stat)

missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

filter_df = df[df['mark'] > 80]
select_rec = filter_df[['roll', 'name', 'mark']]
print('Students with more than 80 marks: \n{}'.format(select_rec))
