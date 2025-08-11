"""
Supervised ML > Regression > Linear regression algorithm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    x = [1,2,3,4,5]
    y = [3,4,2,4,5]

    print("Values of Independant variables : ",x)
    print("Values of Dpendant variables : ",y)

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    print("X_MENA is : ",mean_x)
    print("Y_MENA is : ",mean_y)

    n = len(x)

    numerator = 0
    denominator = 0

    # Y = mX + C
    for i in range(n):
        numerator = numerator + (x[i] - mean_x)*(y[i] - mean_y)
        denominator = denominator + (x[i] - mean_x)**2

    m = numerator / denominator
    print("Slope of line ie m is : ",m)

    C = mean_y - (m * mean_x)
    print("Y intercept of line is : ", C)

    x_graph = np.linspace(1,6,n)
    y_predicited = C + m * x_graph

    plt.plot(x_graph,y_predicited, color = "g", label = "Regression Line")
    plt.scatter(x,y, color = "r", label = "Scatter plot")

    plt.xlabel("X : Independant variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()