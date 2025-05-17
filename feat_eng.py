import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# Load dataset
df = pd.read_csv("cleaned_data.csv")  # Replace with your actual file name

# Extract Wind Speed and Wind Direction
df = df[['Wind_Speed', 'Wind_Direction']].dropna()

# Display first few rows
print(df.head())


plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Wind_Direction'], y=df['Wind_Speed'])
plt.xlabel("Wind Direction (Degrees)")
plt.ylabel("Wind Speed")
plt.title("Wind Speed vs Wind Direction")
plt.show()



# Transform data for polynomial regression
poly = PolynomialFeatures(degree=3)  # Adjust degree based on visualization
X_poly = poly.fit_transform(df[['Wind_Direction']])

# Fit model
model = LinearRegression()
model.fit(X_poly, df['Wind_Speed'])

# Predict and plot
X_pred = np.linspace(df['Wind_Direction'].min(), df['Wind_Direction'].max(), 100).reshape(-1, 1)
y_pred = model.predict(poly.transform(X_pred))

plt.scatter(df['Wind_Direction'], df['Wind_Speed'], label="Actual Data")
plt.plot(X_pred, y_pred, color='red', label="Polynomial Fit")
plt.xlabel("Wind Direction")
plt.ylabel("Wind Speed")
plt.legend()
plt.title("Polynomial Regression: Wind Speed vs Wind Direction")
plt.show()
