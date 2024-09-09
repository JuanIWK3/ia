import matplotlib.pyplot as plt
import numpy as np


def degrau(y, t):
    return 1 if y > t else 0


def plot_perceptron(ax, x1, x2, w1, w2, y, r, calculation, position):
    ax.clear()

    # Define vertical positions with more space
    vertical_spacing = 1.5
    positions = {0: (0, 1), 1: (0, 0), 2: (1, 1), 3: (1, 0)}
    pos = positions[position]
    x_pos, y_pos = pos

    # Plotting the inputs
    ax.text(-0.2, 0.5, f"x1={x1}", fontsize=12, ha="center")
    ax.text(-0.2, -0.5, f"x2={x2}", fontsize=12, ha="center")

    # Plotting the weights
    ax.text(0.4, -0.3, f"{w1:.2f}", fontsize=12, ha="center", rotation=15)
    ax.text(0.4, 0.3, f"{w2:.2f}", fontsize=12, ha="center", rotation=-15)

    # Plotting the output
    ax.text(1.3, 0, f"{y}", fontsize=12, ha="center")

    # Draw the arrows (inputs to output)
    ax.arrow(
        -0.05, 0.5, 1.15, -0.46, head_width=0.1, head_length=0.1, fc="blue", ec="blue"
    )
    ax.arrow(
        -0.05, -0.5, 1.15, 0.46, head_width=0.1, head_length=0.1, fc="blue", ec="blue"
    )

    # Plot the calculation being made
    ax.text(0.5, -1.4, calculation, fontsize=10, ha="center")

    # Set limits and turn off the axis
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-2, 2)
    ax.axis("off")
    ax.set_title(f"Expected: {r}  |  Output: {y}")


def main():
    w1 = np.random.rand() - 0.5  # Initialize weights randomly
    w2 = np.random.rand() - 0.5  # Initialize weights randomly
    b = np.random.rand() - 0.5  # Initialize bias randomly
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    r = [0, 0, 0, 1]  # expected results for AND logic
    a = 0.5  # learning rate, increased to speed up learning

    plt.ion()
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    max_epochs = 1000
    epoch = 0

    while epoch < max_epochs:
        correct_predictions = True

        for c in range(len(x1)):
            y = x1[c] * w1 + x2[c] * w2 + b
            output = degrau(y, 0)
            calculation = f"{x1[c]}*{w1:.2f} + {x2[c]}*{w2:.2f} + {b:.2f} = {y:.2f} -> step({y:.2f}) = {output}"

            print(f"Test {c + 1}:")
            print(f"Inputs: x1 = {x1[c]}, x2 = {x2[c]}")
            print(f"Calculation: {calculation}")
            print(f"Expected: {r[c]}  |  Output: {output}")
            print("-" * 30)  # Separator line for clarity

            # Plot the perceptron for each test in a 2x2 grid
            plot_perceptron(
                axs[c // 2, c % 2], x1[c], x2[c], w1, w2, output, r[c], calculation, c
            )
            plt.pause(0.1)

            if output != r[c]:  # train if output is incorrect
                e = r[c] - output
                w1 = w1 + (a * x1[c] * e)
                w2 = w2 + (a * x2[c] * e)
                b = b + (a * e)
                correct_predictions = (
                    False  # We made a change, so we're not 100% correct yet
                )

        epoch += 1
        print(f"Epoch {epoch} complete.")
        if correct_predictions:
            print(f"100% accuracy achieved after {epoch} epochs!")
            break  # Exit the loop if 100% accuracy is achieved
        else:
            input("Press Enter to continue...")
            print("\n")

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()
