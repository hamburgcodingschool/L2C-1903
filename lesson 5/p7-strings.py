name = "bom mob"

#homework:
# ask the user for a string and tell the user if it is a palindrome or not


#small hint (maybe)
# for i in range(0, 10):
#     print(i) #print the numbers
#     print(9-i) #print the numbers in reverse
#     print("-----")

def isPalindrome(word):

    for i in range(0, int(len(word) / 2)):
        mirrorPos = len(word)-1-i

        letter = word[i]
        mirrorLetter = word[mirrorPos]

        if letter != mirrorLetter:
            return False

    return True

print(isPalindrome("hanh"))



