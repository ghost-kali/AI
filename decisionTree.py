from sklearn.tree import DecisionTreeClassifier

# Sample data: [age, owns_computer (1=yes, 0=no)]
X = [[25, 1], [30, 0], [45, 1], [35, 0]]
y = ['Yes', 'No', 'Yes', 'No']  # Label: Will Buy Product?

# Train decision tree
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Predict new input
print(clf.predict([[28, 1]]))  # e.g., 28-year-old with computer
