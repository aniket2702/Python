# if else loop for raising numbers to powers

num=int(input("enter your choice"))                   # accepting a no.
if num>=0 and num<10:                                 # if condition
    print("square of the number ",pow(num,2))
elif num>=10 and num<100:                          # else if condition
    print("square root of the number",pow(num,1/2))
elif num>=100 and num<1000:                        # else if condition
    print("cube root of the number",pow(num,1/3))
else:                                              # else condition
    print("number not in range")
