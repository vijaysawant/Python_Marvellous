"""
1. Create a DataFrame for student marks and print basic information like shape, columns, and data types

data = {
'Name': ['Amit', 'Sagar','Pooja'],
'Math': [85,90,78],
'Science': [92,88,80],
'English': [75,85,82]
}

Note: Consider the same dataset for this as well as next assignment.
"""
import pandas as pd


def main():
    data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
        }
    dataframe = pd.DataFrame(data)
    print("Shape : ", dataframe.shape)
    print("Columns : ", dataframe.columns)
    print("Datatypes: ")
    print(dataframe.dtypes)
    
if __name__ == "__main__":
    main()