from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()
    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, test_size=0.5)
    model = tree.DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    prediction = model.predict(X_test)

    Accuracy = accuracy_score(prediction, Y_test)
    return Accuracy

def main():
    result = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of Decision Tree Classifier = ",result*100)

if __name__ == "__main__":
    main()