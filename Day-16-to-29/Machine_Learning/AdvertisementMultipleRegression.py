import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def MarvellousAdevertise(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset sample is : ")
    print(df.head())

    # Data cleaning (Clean first coloumn which is not require)
    print("Clean the dataset")
    df.drop(columns = ['Unnamed: 0'], inplace = True)

    print("Updated Dataset is : ")
    print(df.head())

    print("Missing values in each column", df.isnull().sum())
    print("Statistical summary : ")
    print(df.describe())

    print("Correlation Matrix")
    print(df.corr())

def main():
    MarvellousAdevertise("Advertising.csv")

if __name__ == "__main__":
    main()