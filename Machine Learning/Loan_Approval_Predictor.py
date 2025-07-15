import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Step1 : Load Data
df = pd.read_csv("loan_data.csv")

#Split features X and Target Y
X = df[["Income","Age","CreditScore"]]
Y = df["Approved"]

#train and split data
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size = 0.2)

#create and train model
model = LogisticRegression()
model.fit(X_train,Y_train)

#step predict and check accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(Y_test,y_pred))

new_applicant = [[32000, 26, 690]]
result = model.predict(new_applicant)
print("Loan Approved?" if result[0] == 1 else "Loan Rejected")
