import os

import argparse
import mlflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

if "MLFLOW_TRACKING_URI" not in os.environ:
    os.environ["MLFLOW_ALLOW_FILE_STORE"] = "true"
    mlflow.set_tracking_uri("file:./mlruns")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--C", type=float, default=1.0)
    args = parser.parse_args()

    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.log_param("C", args.C)

    model = LogisticRegression(C=args.C, max_iter=200)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    mlflow.log_metric("accuracy", acc)
    print(f"Accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
