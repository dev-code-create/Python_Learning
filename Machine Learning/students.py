import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("Students.csv")
X = df[["Hours"]] #input 
Y = df["Passed"] #output

X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size = 0.2)

model = LogisticRegression()
model.fit(X_train , Y_train)

#Predict 
y_pred = model.predict(X_test)
print("Predicted", y_pred)
print("Accuracy:", accuracy_score(Y_test, y_pred))

#Predict new student
new_hours = [[6.5]]
result = model.predict(new_hours)
print("Will the student pass (1=yes, 0=no)?", result[0])

