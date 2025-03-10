import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

PROJECT_PATH = r"M:\SEM 6 COURSES\BI\ADR_Prediction\ADR_Prediction"

# Load feature data
X = pd.read_csv(os.path.join(PROJECT_PATH, "data", "X_features.csv"))
y = pd.read_csv(os.path.join(PROJECT_PATH, "data", "y_labels.csv")).values.ravel()  # Convert to 1D array

# Split into training & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save trained model
import joblib
joblib.dump(model, os.path.join(PROJECT_PATH, "models", "adr_model.pkl"))

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
# Example usage:
# python src/train.py
