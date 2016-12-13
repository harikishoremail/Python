#!usr/bin/python
startNumber = int(input("Enter starting number: "))
endNumber = int(input("Enter ending number: "))
A = 0
B = 1
while A < endNumber:
    if A > startNumber:
        print(A)
    C = A + B
    A = B
    B = C
