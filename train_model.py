import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("train.csv")

# Drop high-missing-value columns
df = df.drop(columns=["Alley", "PoolQC", "Fence", "MiscFeature"], errors='ignore')

# Fill missing values
df = df.fillna(df.median(numeric_only=True))

# Features and target
X = df[["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath"]]
y = df["SalePrice"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
