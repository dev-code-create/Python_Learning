from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
    "Free entry in 2 a weekly competition to win cash",
    "Hey, how are you doing?",
    "Congratulations, you have won a prize!",
    "Call me when you’re free",
    "Urgent! Your number has won",
    "Let’s catch up tomorrow",
]

labels = [1, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

y = labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = MultinomialNB()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))