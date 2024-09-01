import matplotlib.pyplot as plt
import numpy as np

points = np.random.randn(10, 2)  # Generate 100 random points

print(points)

plt.scatter(points[:, 0], points[:, 1], label="Random Points")  # Plot the points
plt.legend()  # Add a legend
plt.show()  # Display the plot
