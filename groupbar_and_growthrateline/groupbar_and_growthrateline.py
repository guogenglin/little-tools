# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 15:18:16 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 14
# 分组列出数据
group1 = [[0.504, 0.580, 0.538], [0.500, 0.546, 0.523], [0.449, 0.488, 0.467]]
group2 = [[0.532, 0.473, 0.511], [0.518, 0.506, 0.527], [0.394, 0.314, 0.394]]
group3 = [[0.576, 0.540, 0.432], [0.424, 0.463, 0.444], [0.295, 0.350, 0.340]]
group4 = [[0.548, 0.518, 0.479], [0.364, 0.400, 0.382], [0.322, 0.326, 0.290]]
data = [group1, group2, group3, group4]

# width of the bars
barWidth = 0.2
 
# calculate the height of bars
bars1, bars2, bars3, bars4 = [], [], [], []
for i in range(len(data)):
    for numbers in eval('group' + str(i + 1)):
        eval('bars' + str(i + 1)).append(round(np.mean(numbers), 3))
 
# calculate the error bars
yer1, yer2, yer3, yer4 = [], [], [], []
for i in range(len(data)):
    for numbers in eval('group' + str(i + 1)):
        eval('yer' + str(i + 1)).append(round(np.std(numbers), 3))

#calculate the growth rate
growth = []
for group in data:
    growth_rate = []
    for i in range(len(group)):
        if i == 0:
            continue
        else:
            growth_rate.append(round(np.mean(group[i]) / np.mean(group[i - 1]) * 100 - 100, 3))
    growth.append(growth_rate)

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
labels = ['CK', '2 mg/kg', '10 mg/kg', '50 mg/kg']

fig, ax1 = plt.subplots(figsize=(10, 8))

# Create group bars
for i in range(len(data)):
    ax1.bar(eval('r' + str(i + 1)), 
            eval('bars' + str(i + 1)), 
            width = barWidth, 
            color = colors[i], 
            edgecolor = 'black', 
            yerr = eval('yer' + str(i + 1)), 
            capsize = 7, 
            label = labels[i])

# Set ax1 params
ax1.set_xlabel('Time (d)')
ax1.set_ylabel('The weight of earthworms (g)')
ax1.tick_params(axis='y')
ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.xticks([r + 1.5 * barWidth for r in range(len(bars1))], ['0', '14', '28'])

# second y axis
ax2 = ax1.twinx()

# The x position of lines
rr1 = np.arange(len(growth[0]))

# Create lines
for i in range(len(data)):
    ax2.plot(rr1 + len(data) * barWidth, 
             growth[i], 
             color = colors[i], 
             marker = 's', 
             linestyle = '--', 
             linewidth = 2, 
             markersize = 8, 
             label = labels[i])

# Set ax2 params
ax2.set_ylabel('Growth Rate (%)', color='black')
ax2.set_yticks([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0])
ax2.tick_params(axis='y')

# legends
lines1, labels1 = ax1.get_legend_handles_labels()
ax1.legend(
    lines1,
    labels1,
    ncol = 2
)

plt.savefig('C:/Users/86182/Desktop/test.png', dpi = 600)
# Show graphic

plt.show()
