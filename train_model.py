from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
DATA_PATH = DATA_DIR / "customer_churn.csv"
MODEL_PATH = DATA_DIR / "churn_model.joblib"


def create_demo_data(rows: int = 1200) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    contract = rng.choice(["Month-to-month", "One year", "Two year"], rows, p=[0.55, 0.25, 0.20])
    tenure = rng.integers(1, 73, rows)
    monthly_charges = rng.normal(72, 25, rows).clip(20, 150).round(2)
    support_calls = rng.poisson(2, rows).clip(0, 10)
    has_internet = rng.choice(["Yes", "No"], rows, p=[0.85, 0.15])

    risk = (
        (contract == "Month-to-month") * 1.2
        + (tenure < 12) * 0.9
        + (monthly_charges > 90) * 0.5
        + (support_calls >= 4) * 0.8
        + (has_internet == "Yes") * 0.2
        + rng.normal(0, 0.7, rows)
    )
    churn = (risk > 1.8).astype(int)

    return pd.DataFrame(
        {
            "tenure_months": tenure,
            "monthly_charges": monthly_charges,
            "support_calls": support_calls,
            "contract": contract,
            "has_internet": has_internet,
            "churn": churn,
        }
    )


def train() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    if DATA_PATH.exists():
        data = pd.read_csv(DATA_PATH)
    else:
        data = create_demo_data()
        data.to_csv(DATA_PATH, index=False)

    features = ["tenure_months", "monthly_charges", "support_calls", "contract", "has_internet"]
    target = "churn"
    numeric_features = ["tenure_months", "monthly_charges", "support_calls"]
    categorical_features = ["contract", "has_internet"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numeric_features),
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ]
    )
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    x_train, x_test, y_train, y_test = train_test_split(
        data[features], data[target], test_size=0.2, random_state=42, stratify=data[target]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
    print(classification_report(y_test, predictions, zero_division=0))


if __name__ == "__main__":
    train()
