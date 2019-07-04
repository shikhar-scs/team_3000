# coding utf-8
from scipy.cluster.hierarchy import linkage, fcluster
import pandas as pd
import numpy as np
import math
import sys
import csv
import random

if __name__ == "__main__":
    lat = sys.argv[1]
    lon = sys.argv[2]

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

    cen = str(lat) + "," + str(lon)

    rand_x = [float(random.randrange(200, 500)) / 100 for i in range(0, 6)]
    rand_y = [float(random.randrange(200, 500)) / 100 for i in range(0, 6)]

    r_earth = 3958.8
    pi = 3.14

    coords = []

    for i in range(0, 6):
        new_latitude = float(lat) + (rand_x[i] / r_earth) * (180 / pi)
        new_longitude = float(lon) + (rand_y[i] / r_earth) * (180 / pi) / math.cos(float(lat )* pi / 180)
        coords.append([new_latitude, new_longitude])

    print(cen + "$$" + str(dic[1]) + "$$" + str(coords))


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
