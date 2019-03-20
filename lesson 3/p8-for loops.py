# FOR LOOP

# #range
# # 1 argument, only stop, start is 0 by default
# range(5)
#
# # 2 arguments, start and stop (inclusive and exclusive)
# range(0, 5)
#
# # 3 arguments, start and stop (inclusive and exclusive) 3rd is the stepper
# range(0, 5, 2)

for i in range(0, 10):
    print(i)


print("Give me a number")
number = int(input("> "))

for i in range(1, 11):
    res = number * i
    print("{} x {} = {}".format(number, i, res))