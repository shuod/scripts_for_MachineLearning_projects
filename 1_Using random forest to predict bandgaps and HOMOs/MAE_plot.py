# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:24:16 2019

@author: Odysseus
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#load the data
MAE_plot_data_HOMO = pd.read_excel("MAE_result.xlsx",sheet_name="HOMO")
MAE_plot_data_Bandgap= pd.read_excel("MAE_result.xlsx",sheet_name="Bandgap")


# set width of bar
barWidth = 0.25
 
# set height of bar
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Make the plot1
plt.bar(r1, MAE_plot_data_HOMO['MAE_before'], color='#7f6d5f', width=barWidth, edgecolor='white', label='HOMO MAE before linear scaling')
plt.bar(r2, MAE_plot_data_HOMO['MAE_after'], color='#557f2d', width=barWidth, edgecolor='white', label='HOMO MAE after linear scaling')

plt.xlabel('Method', fontweight='bold')
plt.ylabel('Mean Absolute Error (eV)', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['B3LYP', 'HSE06', 'PBE0', 'Morgan', 'RDKit'])

# Create legend & Show graphic
plt.legend()
plt.show()



# Make the plot2
plt.cla()
plt.bar(r1, MAE_plot_data_Bandgap['MAE_before'], color='#7f6d5f', width=barWidth, edgecolor='white', label='Bandgap MAE before linear scaling')
plt.bar(r2, MAE_plot_data_Bandgap['MAE_after'], color='#557f2d', width=barWidth, edgecolor='white', label='Bandgap MAE after linear scaling')

plt.xlabel('Method', fontweight='bold')
plt.ylabel('Mean Absolute Error (eV)', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['B3LYP', 'HSE06', 'PBE0', 'Morgan', 'RDKit'])

# Create legend & Show graphic
plt.legend()
plt.show()

