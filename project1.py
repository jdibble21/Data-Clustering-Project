import pandas as pd
pd.set_option('display.max_rows', None)
import math
import matplotlib.pyplot as plt
from random import randrange

# normalized values are x,y coordinates 
#1: choose random centroids x and y 0-100
#2: Assign each point to cluster such that distance(p,clusteri) is the shortest (find cluster that is shortest distance to given point)
#3: recompute each centroid and reassign points, (repeat until the newly computed centroids are identical to old centroid)

def createPoints(dfX,dfY):
    #Build array of x and y values for cluster points
    points = []
    for i in range(0,len(dfX)):
        points.append([dfX[i],dfY[i]])
    return points

def chooseInitCentroids(k):
    centroids = []
    for i in range(0,k):
        centroids.append([randrange(101),randrange(101)])
    return centroids

def get_X(P):
    r = []
    for x in P:
        r.append(x[0])
    return r


def get_Y(P):
    r = []
    for x in P:
        r.append(x[1])
    return r


def getKValue():
    kVal = 0
    while (True):
        kVal = int(input("Enter an integer 2 or 3 for the k value: "))
        if(kVal > 1 and kVal < 4):
            break
        print("ERROR: k value must be an integer 2 or 4")
    return kVal


def normalize(df):
    # Normalize values in dataframe (0 - 100), cast to integers
    normalizedDF = ((df-df.min())/(df.max()-df.min()))*100
    normalizedDF = normalizedDF.astype(int)
    return normalizedDF
    

def distance(p, q):
    return int(math.fabs(p[0] - q[0]) + math.fabs(p[1]-q[1]))


def SSE(center, cluster):
    sum = 0
    for p in cluster:
        d = distance(center, p)
        sum = sum + d * d
    return sum

dataFrame = pd.read_csv("cs455_homework3_dataset_dibble.csv")
normXDataFrame = normalize(dataFrame['white_rating'])
normYDataFrame = normalize(dataFrame['black_rating'])
kNum = getKValue()
points = createPoints(normXDataFrame,normYDataFrame)
initCentroids = chooseInitCentroids(kNum)

# Output the points with the inital centroids
X = get_X(points)
Y = get_Y(points)
plt.ylim([0,105])
plt.xlim([0,105])
plt.scatter(X,Y)
for i in range(0,kNum):
    X = initCentroids[i][0]
    Y = initCentroids[i][1]
    plt.ylim([0,105])
    plt.xlim([0,105])
    plt.scatter(X,Y, color="red")
plt.title("Initial Centroids")
plt.show()

# Assign points to each cluster by distance
clusters = []
if(kNum == 2):
    cluster_1 = []
    cluster_2 = []
    for i in range(len(points)):
        if (distance(points[i], initCentroids[0]) < distance(points[i], initCentroids[1])):
            cluster_1.append(i)
        else:
            cluster_2.append(i)
    clusters = [cluster_1,cluster_2]
if(kNum == 3):
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    for i in range(len(points)):
        if (distance(points[i], initCentroids[0]) < distance(points[i], initCentroids[1])):
            cluster_1.append(i)
        elif(distance(points[i],initCentroids[1]) < distance(points[i], initCentroids[2])):
            cluster_2.append(i)
        else:
            cluster_3.append(i)
    clusters = [cluster_1,cluster_2,cluster_3]

# Visualize clusters
colorDict = {
    0:"green",
    1:"red",
    2:"blue"
}
for i in range(0,len(clusters)):
    cluster_points = []
    for x in clusters[i]:
        cluster_points.append(points[x])
    X = get_X(cluster_points)
    Y = get_Y(cluster_points)
    plt.ylim([0,105])
    plt.xlim([0,105])
    plt.scatter(X, Y, color=colorDict[i])
plt.title("Initial Clustering Result")
plt.show()

# Get Initial SSE
print("\n\nInitial SSE values: ")
for i in range(0,len(clusters)):
    cluster_points = []
    for x in clusters[i]:
        cluster_points.append(points[x])
    print(SSE(initCentroids[i],cluster_points))

# Recompute centroids
