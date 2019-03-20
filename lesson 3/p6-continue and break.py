pinNumber = 1234

print("What's PIN?")
userNumber = int(input("> "))

counter = 0

accessGranted = True

while (userNumber != pinNumber):
    counter += 1

    if counter >= 3:
        accessGranted = False
        break

    print("Wrong try again")
    userNumber = int(input("> "))


if accessGranted:
    print("WELCOME!")
else:
    print("ACCESS DENIED! PLEASE INSERT PUK OR CONTACT YOUR ACCESS PROVIDER!")