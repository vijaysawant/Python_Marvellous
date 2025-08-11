"""
7. Create a bar plot of student names vs total marks.

data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
        }
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar','Pooja'],
        'Math': [85,90,78],
        'Science': [92,88,80],
        'English': [75,85,82]
        }
    
    df = pd.DataFrame(data)
    df['Total'] = df['Math'] + df['Science'] + df['English']
    
    plt.bar(df['Name'], df['Total'])
    plt.xlabel("Students name")
    plt.ylabel("Total marks")
    plt.title("Bar plot")
    plt.show()

if __name__ == "__main__":
    main()