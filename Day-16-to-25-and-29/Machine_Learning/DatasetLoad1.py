"""
Loading data using scikit-learn library
"""
from sklearn.datasets import load_iris

def main():
    dataset = load_iris()       # load sample dataset
    print("Independant (Features) variable names are : ")
    print(dataset.feature_names)

    print("Dependant (Labels or targets) variable names are : ")
    print(dataset.target_names)
if __name__ == "__main__":
    main()


"""
Output:

Independant (Features) variable names are : 
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Dependant (Labels or targets) variable names are : 
['setosa' 'versicolor' 'virginica']
"""