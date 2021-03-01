import pandas as pd
import numpy as np
import math

class ClusterData():
    def __init__(self,df1,df2):
        self.dataframe = pd.read_csv("cs455_homework3_dataset_dibble.csv")
        self.numericDataFrame1 = self.dataframe[df1]
        self.numericDataFrame2 = self.dataframe[df2]
        self.k = self.getKValue()

    def normalize():
        pass
    def getKValue():
        kVal = 0
        while kVal < 1 and kVal > 5:
            kVal = int(input("Enter an integer between 2 and 4 for the k value: "))
            if(kVal < 1 and kVal > 5):
                print("ERROR: k value must be an integer between 2 and 4")
