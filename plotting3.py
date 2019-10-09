import matplotlib.pyplot as plt

plt.figure()
x_values = range(1, 6)
y_values = [x ** 2 for x in x_values]
print("Points to be plotted {}".format(list(zip(x_values, y_values))))

# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.
# plt.scatter(x_values, y_values, s=100)

# c = color, edgecolor = border
plt.scatter(x_values, y_values, c="red", edgecolor="none", s=40)

# color can be RGB values from 0 to 1
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor="none", s=40)

# must be called before show()
plt.savefig(
    "filename.png", bbox_inches="tight"
)  # bbox_inches crops the white space around figure
plt.savefig("filename2.png")

plt.show()

