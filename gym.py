import numpy as np
import matplotlib.pyplot as plt


# Simulate a heuristic function
def heuristic(X):
    bench_presses = X[:, 0]
    dips = X[:, 1]
    triceps = bench_presses + dips * 2
    return triceps


# Function to run the simulation
def run_simulation(n_iterations, n_points, n_top_results):
    for iteration in range(n_iterations):
        # Generate random data
        X = np.random.rand(n_points, 2) * 100  # Scale to 100 for better range

        # Calculate the heuristic
        triceps = heuristic(X)

        # Get the indices of the top results
        indices = triceps.argsort()[-n_top_results:][::-1]

        # Plot the original data
        plt.figure()
        plt.scatter(X[:, 0], X[:, 1], c="blue", label="Original Data")

        # Highlight the top results
        plt.scatter(X[indices, 0], X[indices, 1], c="red", label="Top Results")

        plt.title(f"Iteration {iteration + 1}")
        plt.xlabel("Bench Presses")
        plt.ylabel("Dips")
        plt.legend()

        # Generate new data points based on the top results
        top_results = X[indices]
        new_data_points = np.vstack(
            [
                top_results + np.random.randn(*top_results.shape) * 5
                for _ in range(n_points - n_top_results)
            ]
        )

        # Combine original data with new data points
        X_new = np.vstack([X, new_data_points])

        # Calculate the heuristic for new data points
        triceps_new = heuristic(X_new)

        # Plot the new data
        plt.figure()
        plt.scatter(X_new[:, 0], X_new[:, 1], c="blue", label="All Data")
        plt.scatter(X[indices, 0], X[indices, 1], c="red", label="Top Results")

        plt.title(f"Iteration {iteration + 1} with New Data")
        plt.xlabel("Bench Presses")
        plt.ylabel("Dips")
        plt.legend()

    plt.show()


# Run the simulation 3 times, with 40 initial points and focusing on the top 5 results
run_simulation(n_iterations=20, n_points=40, n_top_results=5)
