from sklearn.cluster import KMeans
import numpy as np
import math
points=np.array([[-2,-1],[-2, +1],[-2, +2],[-1, -1],[+1, -1],[+1, +1],[+1, +2],[+2, +1]])
init_cluster=np.array([[1,1],[-2,1],[-1,-1]])
for i in points:
    mindist = None
    for j in init_cluster: 
        dist = math.sqrt(abs(i[0]-j[0])**2+abs(i[1]-j[1])**2)
        print(dist)
c1=(points[4]+points[5]+points[6]+points[7])/4
c3=(points[0]+points[3])/2
c2=(points[1]+points[2])/2
init_cluster = np.array([c1,c2,c3])
print(init_cluster)
for i in points:
    mindist = None
    for j in init_cluster: 
        dist = math.sqrt(abs(i[0]-j[0])**2+abs(i[1]-j[1])**2)
        print(dist)