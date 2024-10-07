'''
Date: 06.09.2024
Author: Avinash Singh
Title: Read a csv file into a pandas dataframe and create a plot using matplotlib to visualize the relation
between two columns.
'''

#%%

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/avinash/Desktop/Lab_Exp/Mycsv_file.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['Column1'], df['Column2'], color='red', marker='o', label='Line Plot')
plt.title('Line Plot of Column1 vs Column2')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.legend()
plt.grid(True)
plt.show()
