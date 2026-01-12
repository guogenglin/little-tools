# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:11:36 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import pandas as pd

# Input
df = pd.read_csv('C:/Users/86182/Desktop/input.txt', sep = '\t')

# Process
sero_count = df['Serotype'].value_counts()
st_count = df['ST'].value_counts()
sero_st_filter = df.drop_duplicates(subset=['Serotype', 'ST'], keep = 'first')
sero_st = sero_st_filter.groupby('Serotype')['ST'].apply(lambda x : '\t'.join(x))
sero_host = pd.crosstab(df['Serotype'], df['Source'])
sero_host_freq = pd.crosstab(df['Serotype'], df['Source'], normalize="index").map(lambda x: round(x, 2))
filtered_sero_host_freq = sero_host_freq[sero_host.sum(axis=1) >= 2]

# Output
sero_count.to_csv('C:/Users/86182/Desktop/sero.txt', sep = '\t', index = True)
st_count.to_csv('C:/Users/86182/Desktop/st.txt', sep = '\t', index = True)
sero_st.to_csv('C:/Users/86182/Desktop/sero_st.txt', sep = '\t', index = True)
sero_host.to_csv('C:/Users/86182/Desktop/sero_host.txt', sep = '\t', index = True)
filtered_sero_host_freq.to_csv('C:/Users/86182/Desktop/sero_host_freq.txt', sep = '\t', index = True)

