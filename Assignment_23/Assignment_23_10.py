"""
10. Drop the 'English' column from original DataFrame.

data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
        }
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
        }
    df = pd.DataFrame(data)
    print(df)
    df_new = df.drop(columns=['English'])
    print(df_new)

if __name__ == "__main__":
    main()