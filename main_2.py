# 📥 Step 1: Import Libraries
import pandas as pd               # For data handling
import matplotlib.pyplot as plt   # For plotting
from sklearn.linear_model import LinearRegression  # For creating the ML model

# 📁 Step 2: Load Data from CSV
data = pd.read_csv('result.csv')  # Load dataset
print(data)                       # Display the dataset

# 📈 Step 3: Visualize the Data
plt.scatter(data['Day revised'], data['Estimated result'], color='red')
plt.title('Study Days vs Estimated Result')
plt.xlabel('Days Revised')
plt.ylabel('Estimated Result')
plt.grid(True)
plt.show()

# 🤖 Step 4: Create and Train Linear Regression Model
model = LinearRegression()
model.fit(data[['Day revised']], data[['Estimated result']])

# 🔮 Step 5: Predict the Result for 9 Days of Study
predicted_result = model.predict([[9]])
print(f"Estimated result for 9 days of study: {predicted_result[0][0]:.2f}")
