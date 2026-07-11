import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import joblib

# Step 1: Load your dataset
df = pd.read_csv("price_data.csv")

# Step 2: Split into features and target
X = df[["hour", "day", "temperature", "past_usage"]]
y = df["price"]

# Step 3: Preprocessing for categorical column 'day'
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), ["day"])
], remainder="passthrough")

# Step 4: Create pipeline
model = make_pipeline(preprocessor, DecisionTreeRegressor())

# Step 5: Fit the model
model.fit(X, y)

# Step 6: Save the trained model
joblib.dump(model, "price_predictor.pkl")

print("✅ price_predictor.pkl has been saved successfully.")

