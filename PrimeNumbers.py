#!usr/bin/python
i = 1
x = 500
print ("Prime Numbers from 1 to 500 are listed below.")
for k in range (1, (x+1), 1):
    c=0;
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0) : c = c+1
    if (c==2) : print (i)
    else : k = k-1
    i=i+1
print ("These are the Prime Numbers from 1 to 500.")
