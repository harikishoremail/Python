#!usr/bin/python
import math
sequence = "A B C D E F G F E D C B A";

n = len(sequence)
y =sequence
print (sequence)

for i in range(71,65,-1):
    x =""
    j=0
    while j<=n-1:
        if ord(y[j])==i:
            x = x
            if(y[j+1]==" "):
                x = x
                j +=1
        else:
            x += y[j]
        j +=1
    print (x)
    y = x
    n = len(y)
