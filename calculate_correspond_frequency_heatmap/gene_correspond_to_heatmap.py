# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 10:23:43 2025

@author: Genglin Guo
@e-mail: 2019207025@njau.edu.cn
"""

import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv(sys.argv[-1], sep = '\t')

columns = df.columns
similarity = pd.DataFrame(index=columns, columns=columns)
for col1 in columns:
    for col2 in columns:
        # 计算相同值的行数比例
        same = (df[col1] == df[col2]).mean()
        similarity.loc[col1, col2] = same
        
similarity = similarity.astype(float)

'''全热图
# 绘制热图
plt.figure(figsize=(10, 8))
sns.heatmap(similarity, annot=True, fmt=".2f", cmap='vlag', cbar=True)
plt.show()
'''

# 创建上三角（不含对角线）的布尔掩码
mask_upper = np.triu(np.ones_like(similarity, dtype = bool), k = 1)

# 设置白色背景的颜色映射
white_cmap = ListedColormap(['white'])

# 绘制热图
plt.figure(figsize = (10, 8))
# 下三角显示颜色
sns.heatmap(similarity, mask = ~mask_upper, annot = False, cmap = 'vlag', cbar = True)
# 上三角显示数值（白色背景）
sns.heatmap(similarity, mask = mask_upper, annot = True, fmt = ".2f", 
            cmap = white_cmap, linewidths = 0.5, linecolor = 'gray', cbar = False)

#plt.show()
plt.savefig('relationship.png', dpi = 600)

