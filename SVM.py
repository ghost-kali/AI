from sklearn import svm

# Sample dataset: [experience (yrs), test_score, interview_score]
X = [
    [1, 60, 70],
    [2, 80, 90],
    [3, 88, 85],
    [5, 92, 90],
    [1, 55, 60],
    [2, 60, 65],
]
# Labels: 1 = Hire, 0 = Don't Hire
y = [0, 1, 1, 1, 0, 0]

# Train SVM model
model = svm.SVC(kernel='linear')
model.fit(X, y)

# Predict new candidate
new_candidate = [[2, 75, 80]]  # Example input
prediction = model.predict(new_candidate)

print("Hire" if prediction[0] == 1 else "Don't Hire")
