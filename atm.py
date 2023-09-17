class atm:
    def __init__(self, pin = 4356 ,balance = 3000):
        print("-----welcome-----")
        self.pin = pin 
        self.balance = balance
    
    def deposit(self , amount):
        self.amount = amount 
        self.balance = amount + self.balance
        print(f"Your bank balance : {self.balance}")
    
    def withdraw(self , amount):
        self.amount = amount
        if (self.amount < self.balance):
           self.balance = self.balance - self.amount 
           print(f"Your bank balance : {self.balance}")
        else:
            print("--------INSUFFICIENT BALANCE----------")

    def check_balance(self , balance):
        print(f"Your bank balance : {self.balance}")

    def exit(self):
        print("----- THANK YOU ------")

    def transaction(self):
        print(""" 
             ---------- TRANSACTION SITE -----------
              1. WITHDRAW 
              2. DEPOSIT
              3. CHECK BALANCE
              4. EXIT
               """)
         
        
        option = int(input("ENTER WHAT YOU WNAT DO 1 , 2 , 3 , 4 ")) 
        
        if (option == 1): 
            amount = int(input("ENTER AMOUNT YOU WANT TO WITHDRAW : "))        
            self.withdraw(amount)         
        elif (option == 2):        
            amount = int(input("ENTER AMOUNT YOU WANT TO DEPOSIT : "))     
            self.deposit(amount)         
        elif (option == 3):         
            self.check_balance()         
        elif (option == 4):         
            self.exit()
        else:
            print("__________ WRONG COMMAND _________")


print("------WELCOME TO SiB------ ")
atm_pin = int(input("ENTER YOUR ATM PIN : "))
if (atm_pin == 4356):
     atm1 = atm()
     atm1.transaction()
else:
    print("----INVALID PiN-----")






        