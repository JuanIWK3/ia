import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

def generate_dataset(n_classes, n_samples_per_class=20):
    X = []
    y = []
    centers = np.random.randn(n_classes, 2) * 3  # Randomly place class centers
    for i in range(n_classes):
        points = np.random.randn(n_samples_per_class, 2) + centers[i]
        X.append(points)
        y += [i] * n_samples_per_class
    X = np.vstack(X)
    y = np.array(y)
    return X, y

def plot_decision_boundaries(X, y, clf):
    # Create a mesh to plot the decision boundaries
    xx, yy = np.meshgrid(np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1, 500),
                         np.linspace(X[:, 1].min() - 1, X[:, 1].max() + 1, 500))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundaries
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)

    # Plot the original points
    for i in range(len(np.unique(y))):
        plt.scatter(X[y == i][:, 0], X[y == i][:, 1], label=f'Class {i}')

    plt.legend()

    plt.show()

def main(n_classes):
    X, y = generate_dataset(n_classes)

    clf = svm.SVC(kernel='linear', decision_function_shape='ovo')
    clf.fit(X, y)

    plot_decision_boundaries(X, y, clf)

main(n_classes=3)
