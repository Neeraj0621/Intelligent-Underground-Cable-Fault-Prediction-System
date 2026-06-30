import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Generate reproducible random data
np.random.seed(42)

rows = 1000

voltage = np.random.randint(210, 250, rows)
current = np.random.uniform(5, 100, rows).round(2)
resistance = np.random.uniform(0.5, 20, rows).round(2)
temperature = np.random.randint(20, 90, rows)
cable_length = np.random.randint(100, 5000, rows)
fault_distance = np.random.randint(0, 5000, rows)

fault_type = np.random.choice(
    ["Open Circuit", "Short Circuit", "Insulation Failure"],
    rows
)

# Simple rule for generating labels
score = (
    (temperature > 65).astype(int) +
    (current > 80).astype(int) +
    (resistance > 15).astype(int) +
    (voltage < 220).astype(int) +
    (fault_distance > cable_length * 0.8).astype(int)
)

fault = (score >= 2).astype(int)
df = pd.DataFrame({
    "Voltage": voltage,
    "Current": current,
    "Resistance": resistance,
    "Temperature": temperature,
    "Cable_Length": cable_length,
    "Fault_Distance": fault_distance,
    "Fault_Type": fault_type,
    "Fault": fault
})

# Save dataset
df.to_csv("dataset/cable_fault_dataset.csv", index=False)

# Convert text values into numbers
df["Fault_Type"] = df["Fault_Type"].map({
    "Open Circuit": 0,
    "Short Circuit": 1,
    "Insulation Failure": 2
})

# Features
X = df.drop("Fault", axis=1)

# Target
y = df["Fault"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy*100:.2f}%")

# Save trained model
joblib.dump(model, "model/cable_fault_model.pkl")

print("Model saved successfully!")
print("Dataset created successfully!")