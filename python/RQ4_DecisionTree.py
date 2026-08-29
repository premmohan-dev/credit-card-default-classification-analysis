# Purpose:
# Build a decision tree classification model to predict whether a customer
# will default on their next credit card payment.

# Research Question 4
# Can a decision tree model predict whether a customer will default on their next payment?

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Data
df = xl("A1:X30001", headers=True)

# Create Predictor and Target Variables
X = df.drop(columns=["default payment next month"])
y = df["default payment next month"]

# Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Build Decision Tree Model
model = DecisionTreeClassifier(
    random_state=42,
    max_depth=3
)

model.fit(X_train, y_train)

# Generate Predictions
y_pred = model.predict(X_test)

# Evaluate Model Performance
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Decision Tree Visualization
plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No Default", "Default"],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Decision Tree for Credit Card Default Prediction")

plt.show()
