"""
Loading data using pandas from csv file
"""

import pandas as pd

def main():
    file = "iris.csv"
    dataframe = pd.read_csv(file)

    print(dataframe.head())


if __name__ == "__main__":
    main()