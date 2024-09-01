import matplotlib.pyplot as plt
import numpy as np

# Generate random points within a specific range
points = np.random.randn(10, 2) * 10  # Generate 10 random points with a larger spread

print("Points:\n", points)

# Select two random points
indices = np.random.choice(
    len(points), 2, replace=False
)  # Ensure two different indices
point1 = points[indices[0]]
point2 = points[indices[1]]

print("Selected points:\n", point1, point2)

plt.scatter(points[:, 0], points[:, 1], label="Random Points")

# Plot the line between the two selected points
x1 = point1[0]
y1 = point1[1]
x2 = point2[0]
y2 = point2[1]
plt.plot([x1, x2], [y1, y2], color="red", linewidth=2, label="Line")

plt.legend()
plt.show()  # Display the plot
