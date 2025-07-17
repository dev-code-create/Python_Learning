import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("Knn_data.csv")

le = LabelEncoder()

df("Gender") = le.fit_transform(df["Gender"]) #Male=1 , Female=0

X = df[["Height","Weight"]]
Y = df["Gender"]

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train , Y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(Y_test, y_pred))