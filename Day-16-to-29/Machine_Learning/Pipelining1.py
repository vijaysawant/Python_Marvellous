from pathlib import Path
import joblib
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Configuration details
ARTIFACTS = Path("artifacts_sample")
ARTIFACTS.mkdir(exist_ok=True)
MODEL_PATH = ARTIFACTS / "iris_pipeline.joblib"
TEST_SIZE = 0.2
RANDOM_STATE = 42

def main():
    iris = load_iris()
    
    X = iris.data
    Y = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=TEST_SIZE, random_state=RANDOM_STATE)
    pipe = Pipeline([
        ("scalar", StandardScaler()),
        ("clf",LogisticRegression(max_iter=1000))
    ])
    
    pipe.fit(X_train, Y_train)
    Y_pred = pipe.predict(X_test)

    print("Accuracy Score : ",accuracy_score(Y_test, Y_pred))

if __name__ == "__main__":
    main()