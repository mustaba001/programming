
#data handling
import pandas
data = pandas.read_csv('result.csv')
print(data)

#Visualization the data
import matplotlib.pyplot as plt
plt.scatter(data['Day revised'], data['Estimated result'], color='blue')
plt.title('Study vs Estimated Result')
plt.xlabel('Study Day revised')
plt.ylabel('Estimated Result')
plt.grid()
plt.show()

#Creat and training Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[['Day revised']], data[['Estimated result']])

#predict result for day of studying
predict_result = model.predict([[8]])

#Maximum limit of result
final_result = min(predict_result[0][0], 4.00)

print(f'Estimated result will be : {final_result:.2f}')
