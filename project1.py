import pandas as pd
pd.set_option('display.max_rows', None)
import math
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class ClusterData():
    def __init__(self,df1,df2):
        self.df1Name = df1
        self.df2Name = df2
        self.dataframe = pd.read_csv("cs455_homework3_dataset_dibble.csv")
        self.normalizedDataFrame1 = self.dataframe[df1]
        self.normalizedDataFrame2 = self.dataframe[df2]
        self.combinedDataFrame = []
        self.k = self.getKValue()

    def normalize(self):
        # Normalize values in both dataframes (0 - 100), cast to integers
        df1 = self.normalizedDataFrame1
        df1 = ((df1-df1.min())/(df1.max()-df1.min()))*100
        df1 = df1.astype(int)
        self.normalizedDataFrame1 = df1

        df2 = self.normalizedDataFrame2
        df2 = ((df2-df2.min())/(df2.max()-df2.min()))*100
        df2 = df2.astype(int)
        self.normalizedDataFrame2 = df2

        # Combine dataframes into single 2 column frame
        self.combinedDataFrame = pd.concat([df1,df2], join='outer',axis=1)

    def getKValue(self):
        kVal = 0
        while (True):
            kVal = int(input("Enter an integer between 2 and 4 for the k value: "))
            if(kVal > 1 and kVal < 5):
                break
            print("ERROR: k value must be an integer between 2 and 4")
        return kVal

    def distance(self,p, q):
        return int(math.fabs(p[0] - q[0]) + math.fabs(p[1]-q[1]))

    def SSE(self,center, cluster):
        sum = 0
        for p in cluster:
            d = self.distance(center, p)
            sum = sum + d * d
        return sum

cMap = ClusterData('white_rating','black_rating')
cMap.normalize()

kmeans = KMeans(n_clusters=cMap.k).fit(cMap.combinedDataFrame)
centroids = kmeans.cluster_centers_
print("CENTROID COORDINATES:",centroids)
print("\nSee matplotlib graph output...")

plt.scatter(cMap.combinedDataFrame[cMap.df1Name],cMap.combinedDataFrame[cMap.df2Name],  s=50, alpha=0.5)
plt.scatter(centroids[:, 0],centroids[:, 1], c='red',s=50)
plt.title('Clustering with '+str(cMap.k)+' Centroids')
plt.suptitle('CS455 Project 1 K-Means Clustering Output', fontsize=16)
plt.show()


