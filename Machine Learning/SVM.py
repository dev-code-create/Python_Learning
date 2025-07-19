from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
Y = iris.target

X_train, X_test , Y_train , Y_test = train_test_split(X, Y , test_size=0.2)

model = SVC(kernel='linear')
model.fit(X_train , Y_train)


prediction = model.predict(X_test)
print("Acccuracy", accuracy_score(Y_test,prediction))