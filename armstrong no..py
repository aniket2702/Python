# Armstrong Numbers Check

n=int(input("Enter a no."))
p=n
rem=0
sum=0
if n>=100:                       # input data validation
    while n>0:                   # while condition
        rem=n%10                 # finding last digit
        sum=sum+(rem*rem*rem)    # cubing and storing in sum
        n=n//10                  # dividing to get quotient
    if p==sum:                   # condition check
        print(p,"is Armstrong No." )
    else:
        print(p,"is not Armstong No.")
elif n==0 or n==1:
    print(n," is Armstrong No.")
else:
    print("No.cannot be Armstrong")
