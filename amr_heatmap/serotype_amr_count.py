# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:05:51 2025

@author: Genglin Guo
@e-mail: 2019207025.njau.edu.cn
"""

#open serotype file (two column, isolate : serotype) and amr file (isolate, amr_information)
serotype_file = open('C:/Users/86182/Desktop/info.txt', 'rt').readlines()
amr_file = open('C:/Users/86182/Desktop/amrsummary.tab', 'rt').readlines()
# set a dict, isolate : serotype
serotype_dict = dict()
for line in serotype_file[1:]:
    context = line.strip().split('\t')
    serotype_dict[context[0]] = context[1]
# number count dict, serotype : amr
serotype_amr = dict()
# count the total number of amr
amr_number = len(amr_file[0].strip().split('\t')) - 2
# first, set all amr count as 0
for serotype in serotype_dict.values():
    serotype_amr[serotype] = []
    for i in range(amr_number):
        serotype_amr[serotype].append(0)
# if there is a positive, add the number to the dict.value table
for line in amr_file[1:]:
    context = line.strip().split('\t')
    serotype = serotype_dict[context[0]]
    context = context[2:]
    for i in range(amr_number):
        if not context[i] == '.':
            serotype_amr[serotype][i] += 1
# set the output file
output_number = open('C:/Users/86182/Desktop/sero_amr_number.txt', 'wt')
output_rate = open('C:/Users/86182/Desktop/sero_amr_rate.txt', 'wt')
# write the head line
output_number.write('Isolate')
output_number.write('\t')
output_rate.write('Isolate')
output_rate.write('\t')
for i in amr_file[0].strip().split('\t')[2:]:
    output_number.write(i)
    output_number.write('\t')
    output_rate.write(i)
    output_rate.write('\t')
output_number.write('\n')
output_rate.write('\n')
# count the number of isolate for each serotype, this is a prepare for counting the rate
serotype_count = dict()
for i in serotype_dict.values():
    if not i in serotype_count:
        serotype_count[i] = 1
    else:
        serotype_count[i] += 1
# write the result to output
for serotype, amr_profile in serotype_amr.items():
    if serotype_count[serotype] <= 1:
        continue
    else:
        output_number.write(serotype)
        output_number.write('\t')
        output_rate.write(serotype)
        output_rate.write('\t')
        for amr in amr_profile:
            output_number.write(str(amr))
            output_number.write('\t')
            output_rate.write(str(round(amr/serotype_count[serotype], 2)))
            output_rate.write('\t')
        output_number.write('\n')
        output_rate.write('\n')
output_number.close()
output_rate.close()
