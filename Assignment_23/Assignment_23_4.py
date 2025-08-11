"""
4. Display students who scored more than 85 in Science.

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
    
    df = pd.DataFrame(data)
    print("Students who scored more than 85 in science")
    print(df[df['Science'] > 85])


if __name__ == "__main__":
    main()