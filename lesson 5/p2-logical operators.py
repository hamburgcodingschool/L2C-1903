# LOGICAL OPERATORS

#    and    or   not

print(True and True)
print(True and False)
print(False and True) # order does not matter
print(False and False)

print("------------")

print(True or True)
print(True or False)
print(False or True) # order does not matter
print(False or False)

print("------------")

print(not True)
print(not False)



print("Yo! Give me a number between 10 and 20")
n = int(input("> ")) # n 9

if n >= 10 and n <= 20:
    print("Thank you for complying!")
else:
    print("Maybe it's time for you to start looking jor a job elsewhere!")
