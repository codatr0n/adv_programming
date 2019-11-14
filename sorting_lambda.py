labels = ["25x25", "5x5", "10x10", "10x10", "15x15", "15x15"]
print(labels)

# calling sorted with a custom sorting algorithm using lambda
# the lambda expression multiplies the two numbers, returning an int
# which can be used to sort
labels = sorted(set(labels), key=lambda x: int(x.split("x")[0]) * int(x.split("x")[1]))
print(labels)
