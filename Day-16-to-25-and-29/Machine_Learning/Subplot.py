from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    iris = load_iris()

    x = iris.data
    y = iris.target

    fig = plt.figure(figsize=(8,6))     # mention size of figure
    
    ax = fig.add_subplot(111, projection='3d')  # final axises

    ax.scatter(x[:,2], x[:,3], x[:,0], c=y, cmap='viridis', edgecolors='k')

    ax.set_xlabel('Petal length')
    ax.set_ylabel('Petal width')
    ax.set_zlabel('Sepal length')

    plt.title("Marvellous 3D visualization for IRIS")

    plt.show()

if __name__ == "__main__":
    main()