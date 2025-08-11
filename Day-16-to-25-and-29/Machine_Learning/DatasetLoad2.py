"""
Loading data using scikit-learn library
"""
from sklearn.datasets import load_iris

def main():
    dataset = load_iris()       # load sample dataset
    Line = "-"*30
    
    print(Line)

    for i in range(len(dataset.target)):
        print("ID %d, Features %s, Label : %s"%(i, dataset.data[i], dataset.target[i]))

    print(Line)
if __name__ == "__main__":
    main()