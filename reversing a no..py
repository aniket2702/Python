# Reverse of a Number
n=int(input("Enter a no."))
p=n
rem=0
sum=0
while n>0:              # while condition
    rem=n%10            # calculating remainder
    print(rem,end=" ")  # printing remainder
    n=n//10             # dividing to get quotient
