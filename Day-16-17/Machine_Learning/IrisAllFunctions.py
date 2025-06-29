import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(file_path = 'iris.csv'):
    data_frame = pd.read_csv(file_path)
    print("Dataset gets loaded in memory successfully")
    return data_frame

def GetInformation(data_frame):
    print("\nInformation about loaded dataset is : ")
    print("Shape of dataset : ",data_frame.shape)
    print("Columns : ",data_frame.columns)
    print("Missing values : \n",data_frame.isnull().sum())


def EncodeData(data_frame):
    data_frame['variety'] = data_frame['variety'].map({'Setosa':0, 'Versicolor':1, 'Virginica':2})
    return data_frame


def split_feature_target(data_frame):
    X = data_frame.drop('variety', axis = 1)
    Y = data_frame['variety']
    return X,Y

def split(X,Y,testSize=0.2):
    return train_test_split(X,Y,test_size=testSize)


def main():
    data = load_data("iris.csv")
    print(data.head())
    GetInformation(data_frame=data)

    print("\nData after encoding")
    data = EncodeData(data_frame=data)
    print(data.head())

    print("Spliting Features and Labels")
    Independant, Dependant = split_feature_target(data)
    print(Independant.head())
    print(Dependant.head())

    print("Split data")
    X_train, X_test, Y_train, Y_test = split(Independant, Dependant, 0.3)
    print(X_train.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_test.shape)

if __name__ == "__main__":
    main()