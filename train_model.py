import pandas as pd 
from sklearn.linear_model import LinearRegression
import joblib
df=pd.read_csv("energy_data.csv")
X=df[['light','ac','fan','geyser','tv']]
y=df['total_energy']
model=LinearRegression()
model.fit(X,y)
joblib.dump(model,"energy_model.pk1")
print("✅ Model trained and saved as energy_model.pkl")
