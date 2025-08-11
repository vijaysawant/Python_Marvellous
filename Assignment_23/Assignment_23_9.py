"""
9. Create a DataFrame with missing values and fill them with column mean.

data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [np.nan,90,78],
        'Science': [92,np.nan,80],
        }
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [np.nan,90,78],
        'Science': [92,np.nan,80],
        }
    df = pd.DataFrame(data)
    print(df)
    df.fillna(df.mean(numeric_only=True), inplace=True)

    print(df)

if __name__ == "__main__":
    main()