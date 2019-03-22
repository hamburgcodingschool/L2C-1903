
names = ["Jax", "Mary", "Igor", "Frank", "Sam", "Teresa", "Iris"]

# 1 - Use a for loop to print all the names in the array...

# 2 - find out which is the longest name in the array


# for i in range(0, len(names)):
#     print(names[i])
#
# print("--------")
#
# for name in names:
#     print(name)
#
# print("--------")
#
# for i in range(0, len(names)):
#     print("{}: {}".format(i+1, names[i]))
#
# print("--------")
#
# counter = 0
# for name in names:
#     counter +=1
#     print("{}: {}".format(counter, name))


posHighest = 0
for i in range(0, len(names)):
    if len(names[i]) > len(names[posHighest]):
        posHighest = i

print(names[posHighest])