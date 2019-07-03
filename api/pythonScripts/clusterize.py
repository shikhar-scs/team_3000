# coding utf-8
from scipy.cluster.hierarchy import linkage, fcluster
import pandas as pd
import numpy as np
import math
import csv

coords = pd.read_csv('api/csvFiles/finalCoords.csv')

matrix = np.zeros((coords.shape[0],coords.shape[0]))

for i_index, i_row in coords.iterrows():
    for j_index, j_row in coords.iterrows():
        i_x = i_row[0] - math.floor(i_row[0])
        i_y = i_row[1] - math.floor(i_row[1])
        j_x = j_row[0] - math.floor(j_row[0])
        j_y = j_row[1] - math.floor(j_row[1])
        matrix[i_index][j_index] = math.sqrt(pow((i_x-i_y), 2) + pow((j_x-j_y), 2))

# main line
Z = linkage(matrix, 'ward')  # single complete average median centroid weighted

# alter this to change size of clusters
max_d = 0.3
cluster = fcluster(Z, max_d, criterion='distance').tolist()

dic = {}
for i in range(min(cluster), max(cluster) + 1):
   dic[i] = []
for i in range(len(coords)):
   dic[cluster[i]].append([coords.iloc[i, 0], coords.iloc[i, 1]])
print(dic[3])



#
# cluster_csv = []
#
# for i in range(1, max(clusters)+2):
#     cluster_csv.append([i,[]])
#
# for i in range(0, len(clusters)):
#     cluster_csv[int(clusters[i])][1].append(coords.iloc[[i]])
#
# with open('api/csvFiles/k.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(cluster_csv)
