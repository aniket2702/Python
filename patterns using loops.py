#Star Patterns

#Left alligned
n=int(input("Enter number of rows"))
for i in range(n):                          #for loop for rows

           for j in range(0, i+1):          #for loop for star printing
                print("* ",end=" ")
           print("\n")


#Right Alligned
k = 2*n - 2
for i in range(0, n):                      #for loop for rows
        for j in range(0, k):              #for loop for spaces
            print(end=" ")
        k = k - 2
        for j in range(0, i+1):            #for loop for star printing
            print("* ", end="")
        print("\n")


#centre Alligned
k = 2*n - 2
for i in range(0, n):                      #for loop for rows
        for j in range(0, k):              #for loop for spaces
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):            #for loop for star printing
            print("* ", end="")
        print("\n")
