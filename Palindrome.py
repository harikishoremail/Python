#!usr/bin/python

str = input("\nEnter String to find Palindrome or not:")


def palindrome(str):
    index = 0
    check = True
    while index < len(str):
        if str[index] == str[-1-index]:
            index += 1
            return True
        return False
if palindrome(str) == True:
    print("Entered String is a Palindrome")
else:
    print("Entered String is not a Palindrome")
