# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 09:50:18 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

amr_summary = open('C:/Users/86182/Desktop/amrsummary.tab', 'rt').readlines()
amr_file = open('C:/Users/86182/Desktop/amrs.txt', 'wt')
amr_file.write(amr_summary[0])
for line in amr_summary[1:]:
    context = line.strip().split('\t')
    amr_file.write(context[0])
    amr_file.write('\t')
    amr_file.write(context[1])
    amr_file.write('\t')
    for i in context[2:]:
        if i == '.':
            amr_file.write('0')
        else:
            amr_file.write('1')
        amr_file.write('\t')
    amr_file.write('\n')
amr_file.close()

