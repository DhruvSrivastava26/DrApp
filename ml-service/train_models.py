import os
import joblib
import pandas as pd
import numpy as np

from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "datasets")
MODEL_DIR = os.path.join(BASE_DIR, "models")

os.makedirs(MODEL_DIR, exist_ok=True)


# ================= DIABETES MODEL =================
def train_diabetes_model():
    diabetes_path = os.path.join(DATASET_DIR, "diabetes.csv")
    diabetes_dataset = pd.read_csv(diabetes_path)

    X = diabetes_dataset.drop("Outcome", axis=1)
    y = diabetes_dataset["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, stratify=y, random_state=2
    )

    classifier = svm.SVC(kernel="linear", probability=True)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    # ===== Metrics =====
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = cm.ravel()

    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    gmean = np.sqrt(sensitivity * specificity)

    y_prob = classifier.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)

    # Save model
    joblib.dump(classifier, os.path.join(MODEL_DIR, "diabetes_model.pkl"))
    joblib.dump(scaler, os.path.join(MODEL_DIR, "diabetes_scaler.pkl"))

    print("Diabetes model trained successfully")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"F1 Score: {f1:.3f}")
    print(f"G-Mean: {gmean:.3f}")
    print(f"AUC: {auc:.3f}")


# ================= HEART MODEL =================
def train_heart_model():
    heart_path = os.path.join(DATASET_DIR, "heart_disease_data.csv")
    heart_data = pd.read_csv(heart_path)

    X = heart_data.drop("target", axis=1)
    y = heart_data["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=2
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # ===== Metrics =====
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    cm = confusion_matrix(y_test, y_pred)
    TN, FP, FN, TP = cm.ravel()

    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    gmean = np.sqrt(sensitivity * specificity)

    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)

    # Save model
    joblib.dump(model, os.path.join(MODEL_DIR, "heart_model.pkl"))

    print("Heart disease model trained successfully")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"F1 Score: {f1:.3f}")
    print(f"G-Mean: {gmean:.3f}")
    print(f"AUC: {auc:.3f}")


# ================= RUN =================
if __name__ == "__main__":
    train_diabetes_model()
    print("-" * 50)
    train_heart_model()
    print("-" * 50)
    print("All models saved in models folder")