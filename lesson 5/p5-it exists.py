# def existsInArray(needle, haystack):
#
#     for i in range(0, len(haystack)):
#         #print(haystack[i])
#         if needle == haystack[i]:
#             return True
#
#     return False
#
# number = 12
# list = [12, 45, 12, 3, 5, 12]
#
# if existsInArray(number, list):
#     print("YAY")
# else:
#     print("BOO")

number = 345
list = [12, 45, 12, 3, 5, 12]

if number in list:
    print("YAY")
else:
    print("BOO")