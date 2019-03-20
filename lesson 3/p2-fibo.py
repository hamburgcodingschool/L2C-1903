a = 0
b = 1

print("1: 0")
print("2: 1")

counter = 2
while counter < 20:
    counter += 1

    res = a + b
    print("{}: {}".format(counter, res))

    # now i have to shift a and b
    # res will be the new b
    # b will be the new a
    a = b
    b = res
