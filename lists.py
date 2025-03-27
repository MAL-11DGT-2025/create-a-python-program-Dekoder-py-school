# colors = ["red", "green", "blue", "purple", "yellow"]

# for i in colors:
#     print(i)

# print(colors[-1])
# print(colors[-3])

# print(len(colors))

# for i in colors:
#     if i == "yellow":
#         print("There is yellow!")

colours = []

print(colours)

colours.append("green")  # adds green to list
print(colours)

colours.append("blue")  # adds blue to list
print(colours)

print(colours[1])  # prints the second item in the list
print(len(colours))
# prints the number of items in the list
colours.append("green")
colours.append("green")

print(colours)
print(colours.count("green"))  # prints how many items are green
colours.sort()  # sort the list alphabetically
print(colours)