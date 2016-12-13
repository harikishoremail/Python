#!usr/bin/python3.5
import numpy as np
from numpy import *

print("Enter first matrix Details")
m = int(input("Enter Rows: "))
n = int(input("Enter Columns: "))

Matrix1 = [[0 for x in range(m)] for x in range(n)]
for x in range(0, m):
    for y in range(0, n):
        Matrix1[x][y] = int(input("Row %r Column %r : " % (x, y)))
print("\n")

print("Enter second Matrix Details")
m1 = int(input("Enter Rows: "))
n1 = int(input("Enter Columns: "))

Matrix2 = [[0 for x in range(m1)] for x in range(n1)]
for x in range(0, m1):
    for y in range(0, n1):
        Matrix2[x][y] = int(input("Row %r Column %r : " % (x, y)))
print("\n")

M1 = np.matrix(Matrix1)
print("Matrix 1: \n", M1)
M2 = np.matrix(Matrix2)
print("Matrix 2: \n", M2)

if(n==m1):
    result = M1.dot(M2)
    print("Matrix Multiplication : \n", result)
else:
    print("\nUnable to do multiplication to thee above given Matrix......!!")