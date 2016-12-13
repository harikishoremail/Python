#!usr/bin/python
string = input("Enter String to reverse: ");
i = len(string)
reverse = ""
while i != 0:
    reverse = reverse + string[i-1]
    i = i - 1
print ("The reverse of string is:",reverse)
