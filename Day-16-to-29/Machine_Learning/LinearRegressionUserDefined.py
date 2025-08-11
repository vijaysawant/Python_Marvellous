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

    XSum = 0
    YSum = 0

    for i in range(len(x)):
        XSum = XSum + x[i]
        YSum = YSum + y[i]

    mean_x = XSum / len(x)
    mean_y = YSum / len(y)

    print("X_MENA is : ",mean_x)
    print("Y_MENA is : ",mean_y)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()