# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 13:45:59 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

from itertools import combinations

# read the summary output file of abricate
amr_data = open('C:/Users/gengl/Desktop/allkmsum.tab', 'rt').readlines()
# got headline, genes will have a strip when using resfinder database
headline = [i.split('_')[0] for i in amr_data[0].strip().split('\t')[2:]]

# set a dict, with isolate name as the key and a amr gene list as the value
amr_dict = dict()
# these genes are not included because its conserved or other reasons
gene_need_to_ignore = ['OqxA', 'OqxB', 'fosA']
for line in amr_data[1:]:
    detail = line.strip().split('\t')
    # remove the surfix .fasta
    isolate = detail[0][:-6]
    # remove the duplicate
    amr_info = []
    for i in range(2, len(detail)):
        if detail[i] != '.' and headline[i-2] not in amr_info and headline[i-2] not in gene_need_to_ignore:
            # blaOXY have an extra surfix need to be stripped
            if headline[i-2].startswith('blaOXY'):
                amr_info.append(headline[i-2][:-2])
            else:
                amr_info.append(headline[i-2])
    amr_dict[isolate] = amr_info

# cound combos
all_combos = dict()
single_amr_genome = 0
for value in amr_dict.values():
    if len(value) > 1:
        combos = list(combinations(value, 2))
        for combo in combos:
            if combo not in all_combos:
                all_combos[combo] = 1
            else:
                all_combos[combo] += 1
    else:
        single_amr_genome += 1

# count how many different amrs detected in this study.
pre_lst_unique = list(set(headline))
lst_unique = []
for i in pre_lst_unique:
    if i not in gene_need_to_ignore:
        amr = i
        if amr.startswith('blaOXY'):
            amr = amr[:-2]
        if amr not in lst_unique:
            lst_unique.append(amr)

# class those amrs
amrg_class = {
    'Carbapenemases' : ['blakpc', 'blandm', 'blaimp', 'blavim', 'blaoxa-48', 'blaoxa-162', 'blaoxa-181', 
                        'blaoxa-392'], 
    'Beta-lactam' : ['blatem', 'blashv', 'blactx-m', 'blacarb', 'blacmy', 'blafox', 'bladhy', 'blaoxy', 
                     'blaveb', 'blages', 'blasfo', 'blasim', 'blalap', 'blasco', 'blatla', 'blakluc', 
                     'bladha', 'blaoxa-1', 'blaoxa-2', 'blaoxa-9', 'blaoxa-10', 'blaoxa-101'], 
    'Aminoglycoside' : ['aac', 'aph', 'aad', 'ant', 'rmt', 'arma'], 
    'Tetracycline' : ['tet'], 
    'Sulfonamide' : ['sul'], 
    'Trimethoprim' : ['dfr'], 
    'Chloramphenicol' : ['cat', 'cml', 'flor'], 
    'Quinolone' : ['qnr', 'oqx'], 
    'Macrolide' : ['ere', 'mph', 'msr', 'lnu'], 
    'Fosfomycin' : ['fos'], 
    'Polymyxin' : ['mcr'], 
    'Rifampin' : ['arr'], 
    'Other' : ['bleo', 'tmexc2', 'tmexd2', 'toprj2'], 
    }

# export node sheet
node_sheet = open('C:/Users/gengl/Desktop/node_sheet.csv', 'wt')
header = ['id', 'label', 'category']
node_sheet.write(','.join(header))
node_sheet.write('\n')
for amr in lst_unique:
    category = ''
    for key, value in amrg_class.items():
        for item in value:
            if item in amr.lower():
                category = key
    if category == '':
        print(amr)
    info = [amr, amr, category]
    node_sheet.write(','.join(info))
    node_sheet.write('\n')
node_sheet.close()

# export node sheet
edge_sheet = open('C:/Users/gengl/Desktop/edge_sheet.csv', 'wt')
header = ['source', 'target', 'type', 'weight']
edge_sheet.write(','.join(header))
edge_sheet.write('\n')
for key, value in all_combos.items():
    edge_sheet.write(','.join(key))
    edge_sheet.write(',')
    edge_sheet.write('undirected')
    edge_sheet.write(',')
    edge_sheet.write(str(value))
    edge_sheet.write(',')
    edge_sheet.write('\n')

edge_sheet.close()
