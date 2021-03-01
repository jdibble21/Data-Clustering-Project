import pandas as pd
pd.set_option('display.max_rows', None)
import numpy as np
import math

class ClusterData():
    def __init__(self,df1,df2):
        self.dataframe = pd.read_csv("cs455_homework3_dataset_dibble.csv")
        self.normalizedDataFrame1 = self.dataframe[df1]
        self.normalizedDataFrame2 = self.dataframe[df2]
        self.k = self.getKValue()

    def normalize(self,df):
        # Normalize values in both dataframes (0 - 100)
        df1 = self.normalizedDataFrame1
        df1 = ((df1-df1.min())/(df1.max()-df1.min()))*100
        self.normalizedDataFrame1 = df1

        df2 = self.normalizedDataFrame2
        df2 = ((df2-df2.min())/(df2.max()-df2.min()))*100
        self.normalizedDataFrame2 = df2

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

clusterMapping = ClusterData('white_rating','black_rating')
