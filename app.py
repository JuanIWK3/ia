import matplotlib.pyplot as plt
import numpy as np

points = np.random.rand(10, 2)

plt.scatter(points[:, 0], points[:, 1])

plt.plot([0, 1], [0, 1], color="red")

plt.show()
