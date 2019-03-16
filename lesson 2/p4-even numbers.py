

# a = 32
#
# if a % 2 == 0:
#     print("THE NUMBER IS EVEN")
# else:
#     print("THE NUMBER IS ODD")


counter = 0

while counter < 100:
    counter += 1

    if counter % 9 == 0:
        print(str(counter) + "!!!!")
    elif counter % 5 == 0:
        print(str(counter) + "!!!")
    elif counter % 3 == 0:
        print(str(counter) + "!!")
    elif counter % 2 == 0:
        print(str(counter) + "!")
    else:
        print(counter)

