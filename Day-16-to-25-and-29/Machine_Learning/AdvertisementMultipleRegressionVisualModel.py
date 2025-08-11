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

    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(), annot = True, cmap="coolwarm")
    plt.title("Marvellous Correlation Heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of Features", y = 1.02)
    plt.show()

    x = df[['TV', 'radio', 'newspaper']]
    y = df[['sales']]

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    MSE = metrics.mean_squared_error(y_test, y_predict)
    RMSE = np.sqrt(MSE)
    r2 = metrics.r2_score(y_test, y_predict)

    print("Mean Squared Error is : ", MSE)
    print("Root Mean Squared Error is : ", RMSE)
    print("R Square value : ", r2)

    print("Model Coefficient are : ")
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} : {coef}")
    
    """
    Model Coefficient are : 
    TV : [0.04472952 0.18919505 0.00276111]
    """
    
    print("Y Intercept is : ",model.intercept_)

    plt.figure(figsize=(8,5))
    plt.scatter(y_test, y_predict, color = 'blue')
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sale")
    plt.title("Marvellous Advertisement")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdevertise("Advertising.csv")

if __name__ == "__main__":
    main()