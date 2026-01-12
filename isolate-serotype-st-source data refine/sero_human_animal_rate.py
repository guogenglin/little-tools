# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:07:00 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

# open the input file
sero_human_animal_file = open('C:/Users/86182/Desktop/sero_human_animal.txt', 'rt').readlines()
# open the output file
sero_human_animal_rate = open('C:/Users/86182/Desktop/sero_human_animal_rate.txt', 'wt')
# iterate the input file
for line in sero_human_animal_file:
    # seperate every line by tab to a table
    context = line.strip().split('\t')
    # count the total number of isolate
    count = eval(context[1]) + eval(context[2])
    # set a threshold to avoid the bias
    if count < 2:
        continue
    else:
        # write the result to output
        sero_human_animal_rate.write(context[0])
        sero_human_animal_rate.write('\t')
        # calculate the rate
        sero_human_animal_rate.write(str(round(eval(context[1])/count,2)))
        sero_human_animal_rate.write('\t')
        sero_human_animal_rate.write(str(round(eval(context[2])/count,2)))
        sero_human_animal_rate.write('\n')
# close the output files
sero_human_animal_rate.close()



