import matplotlib.pyplot as plt

plt.figure()  # The figure() command here is optional because figure will be created by default
squares = [x ** 2 for x in range(1, 6)]
print(squares)
plt.plot(squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis="both", labelsize=14)
plt.show()
