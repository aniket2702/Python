# Linear Search
a=int(input("Enter a No."))                   # accepting no.
p=[8,3,4444,5,6,7,889,1,2]                    # List
c=0
for x in range(len(p)):                       # loop to check positions in a list
   if p[x]==a:                               # checking for the no.
       print(a,"is present on position",x+1)
       break
if p[x]!=a:
   print(a,"Not found")

# Binary Search
a=[1,2,3,4,5,6,7,8,9,10]                      # List
k=int(input("Enter no."))
s=0                                           # start of list
c=0
e=len(a)-1                                    # end of list
while s<=e:                                   # loop condition
   c = c+1
   mid = (s+e) // 2                          # finding middle no.
   if a[mid] == k:                           # checking for the no.
       print("index of",k,"is",mid)
       print("No. of times loop ran is",c)
       break
   elif a[mid]>k:                            # checking if mid is greater than input no.
       e=mid-1
   else:
       s=mid+1

