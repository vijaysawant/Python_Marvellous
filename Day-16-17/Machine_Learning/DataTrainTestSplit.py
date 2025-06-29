"""
Loading data and spliting
"""
import pandas as pd
from sklearn.model_selection import train_test_split

def main():

    # Read csv in Data frame
    df = pd.read_csv('iris.csv')
    print("Dataset loaded successfully")

    print(df['variety'])

    # encode target dataset
    df['variety'] = df['variety'].map({'Setosa' : 0, 'Versicolor' : 1, 'Virginica' : 2})
    
    X = df.drop('variety', axis='columns')
    Y = df['variety']

    # split dataset in 80% by 20% percent => fnid 20% => 20/100 = 0.2
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2)

    print("Dimention of X_train : ",X_train.shape)  # (120,4)   => A
    print("Dimention of X_test : ",X_test.shape)    # (30,4)    => C
    print("Dimention of Y_train : ",Y_train.shape)  # (120,)    => B
    print("Dimention of Y_test : ",Y_test.shape)    # (30,)     => D


if __name__ == "__main__":
    main()