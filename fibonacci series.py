#print fibbonacci series upto entered terms

n=int(input("enter end value"))
a=0
b=1
p=0
c=0
while c<=n:                               # loop condition
    print(a,end=" ")                      # printing value
    p=a+b                                 # adding previous two values
    a=b                                   # swapping values
    b=p                                   # swapping values
    c=c+1                                 # counter incrementation

print("\n")
# printing fibbonacci sequence upto nth term
p=int(input("end term"))
a=0
b=1
c=0
i=3
print(a,b,end=" ")                        # printing 0,1
while i<=p:                               # while condition
    c=a+b                                 # adding previous two values
    if c>p:                               # checking for nth term
        break
    else:
        print(c,end=" ")
        a=b                                                                              #   swapping values
        b=c                               # swapping values
        i=i+1
