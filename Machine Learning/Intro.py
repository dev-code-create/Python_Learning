import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Read the data
df = pd.read_csv("data.csv")
X = df[["Hours"]]
Y = df["Marks"]

#train
model = LinearRegression()
model.fit(X,Y)

#Predict
predicted = model.predict([[6.5]])
print("Predicted Marks for 6.5 hours of study", predicted[0])

#show the line
plt.scatter(X,Y,color = "blue")
plt.plot(X,model.predict(X),color="red")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Sttudy Hours vs marks")
plt.show()