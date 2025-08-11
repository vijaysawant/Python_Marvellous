"""
Enseble hetrogenious voting
"""
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    dataframe = pd.read_csv("diabetes.csv")

    X = dataframe.drop(columns=['Outcome'])
    Y = dataframe['Outcome']
    
    scaler = StandardScaler()
    X_Scaled = scaler.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X_Scaled, Y, test_size=0.2, random_state=42)

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=8)
    knn_clf = KNeighborsClassifier(n_neighbors=3)
    voting_clf = VotingClassifier(
        estimators=[
            ('lr',log_clf),
            ('dt', dt_clf),
            ('knn', knn_clf)
        ],
        voting='hard'
        )

    voting_clf.fit(X_train,Y_train)
    y_predict = voting_clf.predict(X_test)
    print("Accuracy score")
    print(accuracy_score(Y_test, y_predict) * 100)

if __name__ == "__main__":
    main()