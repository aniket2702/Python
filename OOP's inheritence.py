#Aniket Sharma
#G-704

#Assignment 11(b)

class BankAcc:
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
#child class using inheritance
class Acc(BankAcc):
    #init function to declare variables
    def __init__(self):
        self.balance=0
        self.cname=""
        self.acno=0
    #function accno
    def accno(self):
        self.cname=input("Enter name")
        self.acno=input("Enter Account No.")
    #Display Function
    def display(self):
        print("Customer name ",self.cname)
        print("Account No. is", self.acno)
        print("Balance remaining is Rs.", self.balance)
#Creating object cstmr to inherited class Acc
cstmr=Acc()

cstmr.accno()             #function of derived class
cstmr.deposit()           #function of parent class
cstmr.withdraw()          #function of parent class
print("\n")
cstmr.display()           #function of derived class
