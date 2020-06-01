#factorial of a no. by decreasing input
n=int(input("Enter No."))
f=1
while n>=1 :                  # while condition
    f=f*n                     # multiplying to store factorial
    n=n-1                     # decreasing n
print("Factorial is",f)

# factorial by incrementing upto n
p=int(input("enter no."))
fc=1
i=1
if p==0:                       # input data validation
    print("Factorial is 1")
elif p==2:
    print("Factorial is 2")
elif p>2:
    while i<=p:               # while condition
        fc=fc*i               # calculating factorial
        i=i+1                 # incrementing i
    print("factorial is",fc)
else:
    print("Factorial of negative no. DNE")


# factorial using predefined function
import math
print("The factorial of",p,"using math function is",math.factorial(p))
