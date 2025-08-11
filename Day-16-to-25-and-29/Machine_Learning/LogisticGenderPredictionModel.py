import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousLogistic(datasetpath):
    df = pd.read_csv(datasetpath)
    print("Dimention of dataframe",df.shape)
    print("Initial data is : ")
    print(df.head())

    # encode gender coloum
    df['Gender'] = df['Gender'].map({'Female':0, 'Male':1})
    print("Encoded data is : ")
    print(df.head())

    # plt.figure(figsize = (8,6))
    # sns.scatterplot(data=df, x = 'Height', y = 'Weight', hue = 'Gender', palette='Set1')
    # plt.title("Marvellous weight height predictor")
    # plt.xlabel("Height")
    # plt.ylabel("Weight")
    # plt.grid(True)
    # plt.show()


    X = df[['Height','Weight']]   # Independant variable
    Y = df['Gender']    # Dependant variable

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train,Y_train)
    Y_predict = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_predict)
    print("Accuracy in : ",accuracy*100)

    Confusion_metrix = confusion_matrix(Y_test, Y_predict)
    print("Confussion matrix = ")
    print(Confusion_metrix)


    report = classification_report(Y_test, Y_predict)
    print("Classification report is : ")
    print(report)


def main():
    MarvellousLogistic("weight-height.csv")

if __name__ == "__main__":
    main()