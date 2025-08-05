import pandas
data = pandas.read_csv('result.csv')
print(data)

import matplotlib.pyplot as plt
plt.scatter(data['Day revised'], data['Estimated result'])
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[['Day revised']], data[['Estimated result']])
print(model.predict([[9]]))

