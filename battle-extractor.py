import json
import cv2
from PIL import Image
from PIL import ImageColor
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from st_dbscan import ST_DBSCAN


colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a','#ffff99', '#b15928']

def cc(v):
    return v / 15000

def plot(data, labels):
    
    for i in range(-1, len(set(labels))):
        if i == -1:
            col = [0, 0, 0, 1]
        else:
            col = colors[i % len(colors)]
        
        clust = data[np.where(labels==i)]
        plt.scatter(clust[:,0], clust[:,1], c=[col], s=1)
    plt.show()

    return None


image = cv2.imread('LoLBaseMap1.png')

f = open('EUW1_5922388644.json')
data = json.load(f)
frames = data["info"]["frames"]

df = pd.DataFrame(columns=['time','x','y'])

factor = 100 

events = []   
for i in range(len(frames)):
    events.append(frames[i]['events'])

max_time = 0 
# looop through champion kills events and add location and time info to df 
for i in range(len(events)):
    for j in range(len(events[i])):
        e = events[i][j]
        if events[i][j]['type'] == "CHAMPION_KILL":
            time = events[i][j]['timestamp'] / 1000                 # convert to sec
            x = cc(events[i][j]['position']['x'])
            y = cc(events[i][j]['position']['y'])
            
            if time > max_time:
                max_time = time

            #print(str(time) + " " + str(x) + " " + str(y))
            
            new_row = {'x':x, 'y':y, 'time':time}
            df = df.append(new_row, ignore_index=True)


# RUN DBSCAN
df['x'] = df['x'].mul(factor)                  # scale up x and y coord to 
df['y'] = df['y'].mul(factor)

#   eps1 = maximum spatial distance
#   eps2 = maximum temporal distance
#   min_samples  = number of samples required 
data = df.loc[:, ['x','y','time']].values

st_dbscan = ST_DBSCAN(eps1 = 15, eps2 = 150, min_samples = 3)
st_dbscan.fit(data) 

#plot(data[:,1:], st_dbscan.labels) 
print("CLUSTER LABELS")
print(st_dbscan.labels)

# normalize time and coords to [0...1]
df['time'] = df['time'].div(max_time)
df['x'] = df['x'].div(factor)                  # scale up x and y coord to 
df['y'] = df['y'].div(factor)

# mark locations on map    
height = image.shape[0]
factor = height / 15000

i = 0
for index, row in df.iterrows():
    x = int((row['x']*15000) * factor)
    y = int((15000 - row['y']*15000) * factor)

    P = (x, y)
    
    color = (0,0,0)
    if st_dbscan.labels[i] >= 0:
        print(st_dbscan.labels[i])    
        color=ImageColor.getcolor(colors[st_dbscan.labels[i]], "RGB")   # BGR
        l = list(color)
        tmp = l[0]
        l[0] = l[2]
        l[2] = tmp
        color = tuple(l)
    
    image = cv2.circle(image, P, radius=7, color=color, thickness=-1)
    image = cv2.circle(image, P, radius=4, color=(255*row['time'], 255*row['time'], 255*row['time']), thickness=-1)
    i+=1

cv2.imshow('image', image)      #show image and wait for keypress
cv2.waitKey(0)