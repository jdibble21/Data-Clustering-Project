import pandas as pd
import numpy as np

class ClusterData():
    def __init__(self):
        self.dataframe = pd.read_csv("cs455_homework3_dataset_dibble.csv")