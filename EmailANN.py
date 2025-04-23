from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Sample data (texts and labels)
emails = [
    "Win money now", "Limited time offer", "Meeting at 10am", "Project deadline",
    "You won a free ticket", "Call me later", "Cheap meds available", "Let's catch up"
]
labels = [1, 1, 0, 0, 1, 0, 1, 0]  # 1 = spam, 0 = not spam

# Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails).toarray()
y = np.array(labels)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Build ANN model
model = Sequential()
model.add(Dense(8, input_dim=X.shape[1], activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile and train
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, verbose=0)

# Test prediction
test_email = ["Free money offer"]
test_vector = vectorizer.transform(test_email).toarray()
prediction = model.predict(test_vector)

print("Spam" if prediction[0][0] > 0.5 else "Not Spam")
