# TIMES TABLE
#
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70
#
# ASK THE USER FOR A NUMBER AND SHOW THE TIMES TABLE FOR THAT NUMBER
#
# step 1 - do a loop and show the counter from 1 to 10
# step 2 - show the counter from 1 to 10 multiplied by the number variable. ex: number = 7 [7, 14, 21, ...]
# step 3 - make it pretty with format


print("Give me a number")
number = int(input("> "))

counter = 0

while counter < 10:
    counter += 1 # counter = counter + 1
    res = number * counter
    print("{} x {} = {}".format(number, counter, res))

