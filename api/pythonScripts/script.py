# coding utf-8
import pandas as pd
import math
import random
import csv
import os
import numpy as np

# df = pd.read_csv('api/csvFiles/OrdersList1562157417583.csv', error_bad_lines=False)
# df.dropna()
# df = df[["Order#", "City", "State", "Zipcode"]]
# df = df.groupby("Zipcode").agg(lambda x: list(x))
#
# # print(df)
# df.to_csv('groups.csv')


# df = pd.read_csv('api/csvFiles/groups.csv', error_bad_lines=False)
zipcode = pd.read_csv('api/csvFiles/LatitudeLongitude.csv')


# l = df[["State"]]
# print(l)

# k = [len(str(l.iloc[i,:]).split(','))-1 for i in range(0, len(l))]
# df["count"] = k

# df.to_csv('groupss.csv')

clusters = pd.read_csv('api/csvFiles/zipcode_groups.csv')

r = random.randint(1, 20)
cno = clusters.iloc[r,:]["Zipcode"]
offers = clusters.iloc[r,:]["Order#"].split(",")

lat = 0
long = 0

# print(type(cno))
# print(type(zipcode.iloc[0,:]))

for index, row in zipcode.iterrows():
    if cno == row['ZIP']:
        lat=row['LAT']
        long=row['LNG']

rand_x = [float(random.randrange(200, 500))/100 for i in range(0,len(offers))]
rand_y = [float(random.randrange(200, 500))/100 for i in range(0,len(offers))]

r_earth = 3958.8
pi = 3.14

coords = []

for i in range(0,len(offers)):
    new_latitude  = lat  + (rand_x[i] / r_earth) * (180 / pi)
    new_longitude = long + (rand_y[i] / r_earth) * (180 / pi) / math.cos(lat * pi/180)
    coords.append([new_latitude,new_longitude])

with open('api/csvFiles/finalCoords.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(coords)

os.system("python3 api/pythonScripts/clusterize.py " + str(lat) + " " + str(long))
