import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

#Step 1: Load & Explore the Data
df = pd.read_csv("Titanic_dataset.csv")
le = LabelEncoder()

print(df.head())

print(df.info())

print(df.isnull().sum())

# Step 2 : Data Cleaning

df.drop('Cabin', axis=1 , inplace=True)

df['Age'].fillna(df['Age'].median(), inplace=True)

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

scaler = StandardScaler()

df[['Age', 'Fare', 'FamilySize']] = scaler.fit_transform(df[['Age', 'Fare', 'FamilySize']])

df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)



df.drop(['Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)




# Step 3 : Feature Selection + Train-Test Split

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked', 'FamilySize', 'IsAlone']]
Y = df['Survived']               # target label

X_train , X_test , Y_train  ,Y_test = train_test_split(
  X , Y , test_size=0.2 , random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train , Y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(Y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(Y_test, y_pred))
print("\nClassification Report:\n", classification_report(Y_test, y_pred))