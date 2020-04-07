#Aniket Sharma
#G-704

#Assignment 11(a)

#Creating class
class BankAcc:
    #init function to declare variables
    def __init__(self):
        self.balance=0
    #function deposit
    def deposit(self):
        amt=float(input("Enter Amount to Deposit"))
        self.balance +=amt
        print("Current amount present is Rs.",self.balance)
    #Function withdraw
    def withdraw(self):
        wit=float(input("Enter amount to be withdrawn"))
        if self.balance>=wit:
            self.balance-=wit
            print("You withdrew Rs.",wit)
        else:
            print("Insufficient balance")
    #Function display
    def display(self):
        print("Balance remaining is Rs.",self.balance)
#creating customer object
cstmr=BankAcc()
#calling functions of class BankAcc using object cstmr
cstmr.deposit()
cstmr.withdraw()
cstmr.display()