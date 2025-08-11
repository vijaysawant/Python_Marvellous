#Support Vector Matrics
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousCancerDetection():
    cancer = load_breast_cancer()
    X = cancer.data
    Y = cancer.target

    data = pd.DataFrame(X, columns=cancer.feature_names)
    data['target'] = Y

    print(data.shape)
    # find out the target names from data frame
    print("Classes : ",dict(zip(cancer.target_names, [0,1])))

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    # Support Vector Classifier
    model = SVC(kernel='linear', C=1)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Accuracy : ",accuracy_score(Y_test, Y_pred))
    print("Confussion matrics : \n",confusion_matrix(Y_test, Y_pred))


def main():

    MarvellousCancerDetection()

if __name__ == "__main__":
    main()