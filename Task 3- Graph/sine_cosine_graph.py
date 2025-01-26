import numpy as np
import matplotlib.pyplot as plt

# Define the x values (angles in radians)
x = np.linspace(0, 2 * np.pi, 500)  # From 0 to 2π with 500 points

# Calculate the sine and cosine values
y_sine = np.sin(x)
y_cosine = np.cos(x)

# Plot the sine graph
plt.plot(x, y_sine, label="Sine", color="blue", linestyle="-", linewidth=2)

# Plot the cosine graph
plt.plot(x, y_cosine, label="Cosine", color="red", linestyle="--", linewidth=2)

# Add labels and title
plt.title("Sine and Cosine Graph")
plt.xlabel("Angle (radians)")
plt.ylabel("Value")

# Add a legend
plt.legend()

# Add grid lines for better readability
plt.grid()

# Show the graph
plt.show()
