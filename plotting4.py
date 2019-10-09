import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

# set axis for x and y - first two are min/max for x, next two are min/max for y
plt.axis([0, 1100, 0, 1100000])

plt.savefig("squares_plot.png", bbox_inches="tight")
