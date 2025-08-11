"""
2. Print descriptive statistics using .describle()

data = {
'Name': ['Amit', 'Sagar','Pooja'],
'Math': [85,90,78],
'Science': [92,88,80],
'English': [75,85,82]
}

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
    print("Output of Describe method : ")
    print(dataframe.describe())


if __name__ == "__main__":
    main()