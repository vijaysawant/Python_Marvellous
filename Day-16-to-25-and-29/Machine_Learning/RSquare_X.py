from sklearn.metrics import mean_squared_error, r2_score

def main():
    y_actual = [100,200,300,400,500]
    y_predict = [150,150,350,350,550]

    r2 = r2_score(y_actual, y_predict)

    print("Actual values : ", y_actual)
    print("Predicted values : ", y_predict)
    print("R2 value : ",r2)


if __name__ == "__main__":
    main()