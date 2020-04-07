#Aniket Sharma
#G-704

#Assignment 12

#Declaring Matrices
m=[[1,2,3],[4,5,6],[7,8,9]]
n=[[10,20,30],[40,50,60],[70,80,90]]
s=[[0,0,0],[0,0,0],[0,0,0]]
mul=[[0,0,0],[0,0,0],[0,0,0]]
print("Matrix 1")
for a in m:
    print(a)
print("Matrix 2")
for b in n:
    print(b)
# for rows in m
for i in range(len(m)):
    #for columns of n
    for j in range(len(n)):
        s[i][j]=m[i][j]+n[i][j]
# for rows of m
for i in range(len(m)):
    #for columns of n
    for j in range(len(n[0])):
        #for rows of n
        for k in range(len(n)):
            mul[i][j]+=m[i][k]*n[k][j]
#printing matrices
print("Sum of Matrix 1&2")
for x in s:
    print(x)
print("Product of Matrix 1&2")
for y in mul:
    print(y)
