# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:34:10 2025

@author: Genglin Guo
@e-mail: 2019207025.njau.edu.cn
"""

# open the input file
info_file = open('C:/Users/86182/Desktop/info.txt', 'rt').readlines()
# set all dict
sero_count = dict()
sero_st = dict()
st_count = dict()
sero_human_animal = dict()
# iterate the input file
for line in info_file:
    # seperate every line by tab to a table
    context = line.strip().split('\t')
    # count isolate number of every serotype
    if not context[0] in sero_count:
        sero_count[context[0]] = 1
    else:
        sero_count[context[0]] += 1
    # find how many st identified within a serotype
    if not context[0] in sero_st:
        sero_st[context[0]] = []
    if not context[1] in sero_st[context[0]]:
        sero_st[context[0]].append(context[1])
    # count isolate number of every st
    if not context[1] in st_count:
        st_count[context[1]] = 1
    else:
        st_count[context[1]] += 1
    # set a table with 2 chr as the value, the first is human and the second is animal
    if not context[0] in sero_human_animal:
        sero_human_animal[context[0]] = [0, 0]
    if context[2] == 'human':
        sero_human_animal[context[0]][0] += 1
    else:
        sero_human_animal[context[0]][1] += 1
# open output file
sero_count_file = open('C:/Users/86182/Desktop/sero_count.txt', 'wt')
sero_st_file = open('C:/Users/86182/Desktop/sero_st.txt', 'wt')
st_count_file = open('C:/Users/86182/Desktop/st_count.txt', 'wt')
sero_human_animal_file = open('C:/Users/86182/Desktop/sero_human_animal.txt', 'wt')
# write sero_count to output
for serotype, number in sero_count.items():
    sero_count_file.write(serotype)
    sero_count_file.write('\t')
    sero_count_file.write(str(number))
    sero_count_file.write('\n')
# write sero_st to output
for serotype, sts in sero_st.items():
    sero_st_file.write(serotype)
    for st in sts:
        sero_st_file.write('\t')
        sero_st_file.write(st)
    sero_st_file.write('\n')
# write st_count to output
for st, number in st_count.items():
    st_count_file.write(st)
    st_count_file.write('\t')
    st_count_file.write(str(number))
    st_count_file.write('\n')
# write sero_human_animal to output
for serotype, numbers in sero_human_animal.items():
    sero_human_animal_file.write(serotype)
    for number in numbers:
        sero_human_animal_file.write('\t')
        sero_human_animal_file.write(str(number))
    sero_human_animal_file.write('\n')
# close all output files
sero_count_file.close()
sero_st_file.close()
st_count_file.close()
sero_human_animal_file.close()
