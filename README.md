# ML_task--2
Orinson Technologies - Machine Learning Internship : Task-2
**OBJECTIVE**
The objective of this program is to analyze the relationship between the number of members ("Members") and their associated rates ("Rate") using Linear Regression. The program predicts rates based on the number of members and visualizes the relationship using scatter plots and regression lines.

**Step by Step Explanation:-**
1. Importing the neccessary Libraries
2. Loading the Dataset
Dataset: The program loads an Excel file (Rooms.xlsx) containing data with two columns:
Members: Number of members.
Rate: Corresponding rates.
The dataset is displayed for inspection.
3.Extract Features (X) and Target Variable (y)
Features (X): Members column, reshaped into a 2D array (required for scikit-learn).
Target Variable (y): Rate column.
4. Split the Dataset into Training and Testing Sets
Training Set: 80% of the data, used to train the model.
Testing Set: 20% of the data, used to evaluate the model's performance.
random_state=42: Ensures consistent random splitting for reproducibility.
5. Initialize and Train the Linear Regression Model
Initialize: Creates an instance of the LinearRegression model.
Train: The model learns the relationship between Members (X) and Rate (y) using the training set.
6.Predict on the Test Set
The model predicts the Rate for the test set based on the trained linear regression model.
7. Calculate Performance Metrics
Mean Squared Error (MSE): Measures the average squared difference between actual and predicted values. Lower MSE indicates better performance.
R² Score: Explains the proportion of variance in the target variable explained by the model. Values closer to 1 indicate better performance.
8. Visualizations
-Scatter Plot of Data Points
-Regression Line Plot
-Combined Plot (Data Points and Regression Line)
