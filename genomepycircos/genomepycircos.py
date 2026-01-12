# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:09:56 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import pycircos
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

# ---------- 参数 ----------
fasta = 'C:/Users/gengl/Desktop/23K892.fasta'
gff = "C:/Users/gengl/Desktop/23K892.gff3"
eggnog = "C:/Users/gengl/Desktop/emapper.annotations.tsv"
window_size = 2000


# ---------- 1. 读取序列 ----------
record = next(SeqIO.parse(fasta, "fasta"))
seq = str(record.seq)
seq_len = len(seq)
arc_id = record.id

# ---------- 2. 计算 GC content & GC skew ----------
gc_content = []
gc_skew = []

for i in range(0, seq_len, window_size):
    window = seq[i:i+window_size]
    g = window.count('G') + window.count('g')
    c = window.count('C') + window.count('c')
    gc = (g + c) / len(window) if len(window) > 0 else 0
    skew = (g - c) / (g + c) if (g + c) > 0 else 0
    gc_content.append(gc)
    gc_skew.append(skew)

average = sum(gc_content) / len(gc_content)

positions = np.arange(0, seq_len, window_size)

# ---------- 3. 读取 GFF 注释 ----------
genes = dict()
with open(gff) as file:
    for line in file:
        if not line.startswith("#") and "\tCDS\t" in line:
            parts = line.strip().split("\t")
            start, end, strand = int(parts[3]), int(parts[4]), parts[6]
            attr = parts[8].strip().split(';')
            prid = attr[0][7:]
            genes[prid] = {"start": start, "end": end, "strand": strand}

cog_colors = {
    'C': '#1F77B4',  # 蓝 Blue
    'D': '#FF7F0E',  # 橙 Orange
    'E': '#2CA02C',  # 绿 Green
    'F': '#D62728',  # 红 Red
    'G': '#BFD3E6',  # 石灰 Lime
    'J': '#9467BD',  # 紫 Purple
    'H': '#8C564B',  # 棕 Brown
    'I': '#E377C2',  # 粉 Pink
    'K': '#BCBD22',  # 橄榄 Olive
    'L': '#17BECF',  # 青 Cyan
    'M': '#6BAED6',  # 湖蓝 Sky Blue
    'N': '#74C476',  # 草绿 Light Green
    'O': '#FFD92F',  # 金黄 Gold
    'P': '#E6550D',  # 暗橙 Brick
    'Q': '#3182BD',  # 深蓝 Deep Teal
    'S': '#DD3497',  # 紫红 Magenta
    'T': '#BFD3E6',  # 浅灰蓝 Lime
    'U': '#9ECAE1',  # 薄荷 Mint
    'V': '#FB6A4A',  # 桃红 Coral
}

cog_group = []
with open(eggnog) as file:
    for line in file:
        if not line.startswith("#"):
            parts = line.strip().split('\t')
            prid = ('_').join(parts[0].split('_')[3:5])
            cog = parts[6]
            if cog != '-':
                genes[prid]['cog'] = cog[0]
                genes[prid]['color'] =cog_colors[cog[0]]
                if cog[0] not in cog_group:
                    cog_group.append(cog[0])


# ---------- 4. 创建圈图 ----------
Garc = pycircos.Garc
Gcircle = pycircos.Gcircle
circle = Gcircle(figsize = (6, 6))   # create the circle object


arc = Garc(arc_id = arc_id, size = seq_len, interspace = 0, raxis_range=(300, 300))
circle.add_garc(arc)
circle.set_garcs(0,360)   # the start and end location of the circle

# ---------- 5. 添加 GC skew ----------
skew_position = []
new_skew = []

for i in range(len(gc_skew)):
    current = gc_skew[i]
    next_val = gc_skew[(i + 1) % len(gc_skew)] # make it a circle
    skew_position.append(int(positions[i]))
    new_skew.append(current)
    if current * next_val < 0:
        mid_pos = (int(positions[i]) + int(positions[(i + 1) % len(positions)])) / 2
        skew_position.append(mid_pos)
        new_skew.append(0)

  
vmin, vmax = min(gc_skew), max(gc_skew)
color_mark = 0
color_list = ['#4CAF50', '#FFB6C1']
if new_skew[0] < 0 or (new_skew[0] == 0 and new_skew[1] < 0):
    color_index = 1
for i in range(len(new_skew) - 1):
    if i > 0 and isinstance(new_skew[i], int) and new_skew[i] == 0:
        color_mark += 1
    elif isinstance(new_skew[i], float) and new_skew[i] == 0:
        if new_skew[i - 1] * new_skew[i + 1] < 0:
            color_mark += 1
    gc_skew_pos = [new_skew[i], new_skew[i + 1]]
    skew_posit = np.array([skew_position[i], skew_position[i + 1]])
    circle.lineplot(arc_id, # name of the arc
                    data = gc_skew_pos, # specific number of every breakpoint
                    positions = skew_posit, # x axis of the breakpoint
                    rlim=[vmin - 0.05*abs(vmin), # scale the y axis
                          vmax + 0.05*abs(vmax)], # scale the y axis
                    raxis_range = (230, 370),
                    linecolor = color_list[color_mark%2], 
                    spine = False)
            
# circle.figure

# ---------- 6. 添加 GC content ----------
# 可以嵌套在上一节的循环里，这里为了方便演示，分开写
content_position = []
new_content = []

for i in range(len(gc_content)):
    current = gc_content[i]
    next_val = gc_content[(i + 1) % len(gc_content)] # make it a circle
    content_position.append(int(positions[i]))
    new_content.append(current)
    if (current - average) * (next_val - average) < 0:
        mid_pos = (int(positions[i]) + int(positions[(i + 1) % len(positions)])) / 2
        content_position.append(mid_pos)
        new_content.append(average)

vmin, vmax = min(gc_content), max(gc_content)
color_mark = 0
color_list = ['#2E7D32', '#C62828']
if new_content[0] < average or (new_content[0] == average and new_content[1] < average):
    color_index = 1
for i in range(len(new_content) - 1):
    if i > 0 and new_content[i] == average:
        color_mark += 1
    gc_content_pos = [new_content[i], new_content[i + 1]]
    content_posit = np.array([content_position[i], content_position[i + 1]])
    circle.lineplot(arc_id, # name of the arc
                    data = gc_content_pos, # specific number of every breakpoint
                    positions = content_posit, # x axis of the breakpoint
                    rlim=[vmin - 0.05*abs(vmin), # scale the y axis
                          vmax + 0.05*abs(vmax)], # scale the y axis
                    raxis_range = (370, 510),
                    linecolor = color_list[color_mark % 2], 
                    spine = False)

# circle.figure

# ---------- 7. 添加正链基因 ----------

pos_gene = {prid: info for prid, info in genes.items() if info['strand'] == '+' and info.get('cog')}
neg_gene = {prid: info for prid, info in genes.items() if info['strand'] == '-' and info.get('cog')}

circle.barplot(arc_id,   # every chr
               data = [1]*len(pos_gene),   # 
               positions = [info["start"] for info in pos_gene.values()],   # the position
               width = [info["end"] - info["start"] for info in pos_gene.values()],   # the length of the colored arc
               raxis_range = [510,580],    # location of ticks of these arcs, radius
               facecolor = [info["color"] for info in pos_gene.values()])   # the color you want

circle.barplot(arc_id,   # every chr
               data = [1]*len(neg_gene),   # 
               positions = [info["start"] for info in neg_gene.values()],   # the position
               width = [info["end"] - info["start"] for info in neg_gene.values()],   # the length of the colored arc
               raxis_range = [580,650],    # location of ticks of these arcs, radius
               facecolor = [info["color"] for info in neg_gene.values()])   # the color you want
plt.text(0, 0, f'{arc_id}\n{seq_len} bp', fontsize=12, ha='center', va='center',  fontname='Times New Roman', color='black')

circle.figure
circle.figure.savefig('C:/Users/gengl/Desktop/circle.svg')


