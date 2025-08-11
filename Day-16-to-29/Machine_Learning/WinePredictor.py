import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix


def WinePredictor(Datapath):
    df = pd.read_csv(Datapath)
    print("Dataset loaded successfully")
    print(df.head())
    print(df.shape)

    # drop null value
    df.dropna(inplace=True)

    x = df.drop(columns=['Class'])
    y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size=0.2, random_state=42)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    accuracy = accuracy_score(y_test,y_predict)

    print("Accuracy score is : ", accuracy*100)




def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()