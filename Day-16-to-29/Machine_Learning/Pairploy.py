import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    file = "iris.csv"
    dataframe = pd.read_csv(file)

    sns.pairplot(dataframe, hue='variety')
    plt.show()


if __name__ == "__main__":
    main()