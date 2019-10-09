import matplotlib.pyplot as plt

plt.figure()
plt.scatter(2, 4, s=200)  # s is the scalar value determines the area of the point.

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

# Set size of tick labels.
plt.tick_params(axis="both", which="major", labelsize=10)
plt.show()
