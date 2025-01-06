# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
file = r"D:\Orinson Projects\Task 2\Rooms.xlsx" 
dataset = pd.read_excel(file)
print("Entire Dataset:-\n")
print(dataset)

# Extract features (X) and target variable (y)
X = dataset["Members"].values.reshape(-1, 1)
y = dataset["Rate"].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the metrics
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2) Score: {r2}")

# 1. Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Data Points")
plt.xlabel("Members")
plt.ylabel("Rate")
plt.title("Scatter Plot: Members & Price")
plt.legend()
plt.grid()
plt.show()

# 2. Regression line plot
plt.figure(figsize=(10, 6))
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")
plt.xlabel("Members")
plt.ylabel("Rate")
plt.title("Regression Line: Members & Price")
plt.legend()
plt.grid()
plt.show()

# Visualization: Plot regression line with data points
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Data Points")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")
plt.xlabel("Members")
plt.ylabel("Rate")
plt.title("Linear Regression: Members & Price")
plt.legend()
plt.grid()
plt.show()