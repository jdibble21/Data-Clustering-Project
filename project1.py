import pandas as pd
pd.set_option('display.max_rows', None)
import math
import matplotlib.pyplot as plt

# normalized values are x,y coordinates 
#1: choose random centroids x and y 0-100
#2: Assign each point to cluster such that distance(p,clusteri) is the shortest (find cluster that is shortest distance to given point)
#3: recompute each centroid and reassign points, (repeat until the newly computed centroids are identical to old centroid)

class ClusterData():
    def __init__(self,df1,df2):
        self.df1Name = df1
        self.df2Name = df2
        self.dataframe = pd.read_csv("cs455_homework3_dataset_dibble.csv")
        self.normalizedDataFrame1 = self.dataframe[df1]
        self.normalizedDataFrame2 = self.dataframe[df2]
        self.points = []
        self.centroids = {}
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

