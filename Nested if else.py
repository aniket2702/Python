#Aniket Sharma
#G-704

#Assignment 7

a=int(input("Enter first no."))
b=int(input("Enter Second No."))

if a>b:
    print(b,"is less than",a)
    print("square of ",b,"is",(b**2))
    print("cube of",a,"is",(a**3))
elif a<b:
    print(a, "is less than", b)
    print("square of ", a, "is", (a ** 2))
    print("cube of", b, "is", (b ** 3))
else:
    print("Both are equal")
    print("Square of ",a," is",(a**2))
    print("Square root of ",a,"is",(a**(1/2)))
    print("Cube root of ",a,"is", (a**(1/3)))
