"""
Loading data and spliting
"""

import pandas as pd

def main():

    # Read csv in Data frame
    df = pd.read_csv('iris.csv')
    print("Dataset loaded successfully")
    print("Diamention of dataset is: ",df.shape)

    print(df['variety'])
    # print("-"*30)
    # print(df['sepal.length'].head())

    # encode target dataset
    df['variety'] = df['variety'].map({'Setosa' : 0, 'Versicolor' : 1, 'Virginica' : 2})
    print(df['variety'])

    # X = df.drop('variety', axis=1)  # axis parameter => 1 means column and 0 means row OR use below line
    X = df.drop('variety', axis='columns')
    Y = df['variety']

    print("Independant variable dimention: ", X.shape)
    print("Dependant variable dimention : ", Y.shape)


if __name__ == "__main__":
    main()