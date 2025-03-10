import pandas as pd
import os

PROJECT_PATH = r"M:\SEM 6 COURSES\BI\ADR_Prediction\ADR_Prediction"

def generate_features():
    """Generate ML-ready features from FAERS and SIDER datasets."""
    
    # Load preprocessed FAERS data
    faers_df = pd.read_csv(os.path.join(PROJECT_PATH, "data", "processed_faers.csv"))

    # Convert categorical variables to numerical
    faers_df["sex"] = faers_df["sex"].map({"M": 0, "F": 1, "UNKNOWN": -1})

    # One-hot encode drug routes
    faers_df = pd.get_dummies(faers_df, columns=["route"], drop_first=True)

    # Feature selection
    features = ["age", "wt", "sex"] + [col for col in faers_df.columns if col.startswith("route_")]
    
    X = faers_df[features]
    y = faers_df["pt"]  # Side effects (reaction)

    # Save feature-engineered dataset
    X.to_csv(os.path.join(PROJECT_PATH, "data", "X_features.csv"), index=False)
    y.to_csv(os.path.join(PROJECT_PATH, "data", "y_labels.csv"), index=False)

    print("Feature engineering completed.")

# Run feature engineering
if __name__ == "__main__":
    generate_features()
