#Program to accept marks and calculate aggregate while displaying relevant messages

a=list()                                           #creating a list
c=0
for x in range(5):
    a.append(int(input("Enter marks")))            #storing input in a list

print("Marks entered",a)
for y in range(5):                                 #checking if marks are greater than 40
    if a[y]>=40:
        c=c+1

s=sum(a)                                          #calculating sum
if c==5:                                          #printing result
    if s>=75:
        print("Distinction with",s/5,"%")
    elif s>=60 and s<75:
        print("First class",s/5,"%")
    elif s>=50 and s<60:
        print("Second class",s/5,"%")
    elif s>=40 and s<50:
        print("Third class",s/5,"%")
else:
    print("You have scored less than 40 in one or more subjects and percentage is",s/5,"%")
