# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:13:22 2023

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import random

def color_generator():
    digit_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = '#'
    for i in range(6):
        a = random.choice(digit_16)
        color += a
    return color

# made a output.
label = open('C:/Users/86182/Desktop/color_strip.txt', 'wt')

# input the header
header = 'DATASET_COLORSTRIP\nSEPARATOR SPACE\nDATASET_LABEL label1\nCOLOR #ff0000 #00FF00\nCOLOR_BRANCHES 0\nSTRIP_WIDTH 50\nDATA\n\n'
label.write(header)

# 
detail = open('C:/Users/86182/Desktop/k5.txt', 'rt').readlines()
total_group = 0
color_comparison = dict()
for line in detail[1:]:
    line = line.strip().split('\t')
    serotype = line[1]
    if serotype.endswith('?'):
        serotype = serotype[:-1]
    if serotype not in color_comparison:
        color = color_generator()
        color_comparison[serotype] = color
        total_group += 1
    label.write(line[0])
    label.write('\t')
    label.write(color_comparison[serotype])
    label.write('\n')
label.close()


