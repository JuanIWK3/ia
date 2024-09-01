import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Create points for two classes
X_red = np.random.randn(20, 2)
X_green = np.random.randn(20, 2) + np.array([3, 1])  # Green class centered at (3, 1)

# Combine the datasets
X = np.vstack((X_red, X_green))
y = np.array([0] * 20 + [1] * 20)  # Labels (0: red, 1: green)

# Create an SVM classifier with a linear kernel
clf = svm.SVC(kernel="linear", C=0.1)  # C is the soft margin parameter

# Fit the classifier to the data
clf.fit(X, y)

# Create a mesh to plot the decision boundaries
xx, yy = np.meshgrid(np.linspace(-3, 6, 500), np.linspace(-3, 7, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary (where Z=0)
plt.contour(xx, yy, Z, colors="black", levels=[0], linestyles=["-"])

# Plot the original points
plt.scatter(X[:20, 0], X[:20, 1], c="red", label="Red class")
plt.scatter(X[20:40, 0], X[20:40, 1], c="green", label="Green class")

# Add a legend
plt.legend()

# Display the plot
plt.show()
