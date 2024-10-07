'''
Date: 06.09.2024
Author: Avinash Singh
Title: Write a python script to generate a line plot and a scatter plot using MatplotLib with plot titles, labels and
legends. For the same data, generate a bar chart (for categorical values) and histogram to visualize the data
distribution.
'''

#%%

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 8, 12, 20]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))


ax1, ax2, ax3, ax4 = axes.flat


ax1.plot(x, y1, label='Sine')
ax1.plot(x, y2, label='Cosine')
ax1.set_title('Line Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.legend()


ax2.scatter(x, y1, label='Sine')
ax2.scatter(x, y2, label='Cosine')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.legend()


ax3.bar(categories, values)
ax3.set_title('Bar Chart')
ax3.set_xlabel('Category')
ax3.set_ylabel('Value')


ax4.hist(values, bins=5)
ax4.set_title('Histogram')
ax4.set_xlabel('Value')
ax4.set_ylabel('Frequency')


plt.subplots_adjust(wspace=0.4, hspace=0.4)


plt.show()
