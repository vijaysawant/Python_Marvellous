import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def MarvellousHeadBrainLinear(Datapath):
    Line = "*"*50
    df = pd.read_csv(Datapath)

    print(Line)
    print("First few records of dataset are : ")
    print(Line)
    print(df.head())
    print(Line)

    print("Statistical information of the dataset : ")
    print(Line)
    print(df.describe())    # Print statistical data of our case study
    print(Line)
    print()
    x = df[['Head Size(cm^3)']]
    y = df[['Brain Weight(grams)']]
    print("Independant variables are 'Head size'")
    print("Dependent variables are 'Brain Weight'")

    print("Total records in dataset : ",x.shape)

    # Split the data
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
    print("Dimentions of Training dataset : ",x_train.shape)
    print("Dimentions of Testing dataset : ",x_test.shape)

    # Train the model
    model = LinearRegression()
    model.fit(x_train, y_train)

    y_predict = model.predict(x_test)

    #mean squared error
    mse = mean_squared_error(y_test, y_predict)
    
    #root mean squared error
    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, y_predict)

    # Visual representation
    print("Visual representation")
    plt.figure(figsize=(8,5))   # frame size in inches 8x5
    plt.scatter(x_test, y_test, color = 'blue', label = 'Actual')
    plt.plot(x_test.values.flatten(), y_predict, color = 'red', linewidth = 2, label = "Regression Line")
    plt.xlabel('Head Size(cm^3)')
    plt.ylabel('Brain Weight(grams)')
    plt.title("Marvellous Head Brain Regression")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\nResult of Case study")
    print("Slope of line (m) : ",model.coef_[0])
    print("Intercept (c) : ", model.intercept_)
    print("Mean Squared Error is : ", mse)
    print("Root Mean Squared Error is : ", rmse)
    print("R Square value : ", r2)
def main():
    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")

if __name__ == "__main__":
    main()