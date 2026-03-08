class atm:
    def __init__(self,name,account_number,pin,balance):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self):
         entered_pin = int(input("Enter your PIN: "))
         if entered_pin == self.pin:
              print("✅ Login Successful\n")   
              self.menu()
         else:
              print("❌ Incorrect PIN") 

    def menu(self):
         while True:
              print("\n===== ATM MENU =====")
              print("1. Check Balance")
              print("2. Withdraw Money")
              print("3. Deposit Money")
              print("4. Account Details")
              print("5. Exit")          

              choice = input("Enter your choice:  " )   

              if choice == "1":
                   self.check_balance()  

              elif choice == "2":
                   amount = float(input("Enter withdraw amount:"))  
                   self.withdraw(amount)  

              elif choice == "3":
                   amount = float(input("Enter withdraw amount:"))  
                   self.deposit(amount)

              elif choice == "4":
                   self.account_details()    

              elif choice == "5":
                print("🙏 Thank you for using ATM")
                break

              else:
                 print("❌ Invalid choice")               

    def withdraw(self,amount):
        if amount<=0:
            print("❌ Withdraw amount must be greater than 0")
            return
        
        if amount > self.balance:
            print("❌ Insufficient balance!")
            return

        
        self.balance -= amount
        print(f"✅ Withdrawn ₹{amount} successfully!")

    def check_balance(self):
            print(f"💰 Current Balance: ₹{self.balance}")
 
    
    def deposit(self,amount):
         if amount<=0:
              print("❌ Deposit must be greater than 0")
              return
         
         self.balance += amount
         print(f"✅ Deposited ₹{amount}")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")    

    def account_details(self):
        masked = "**** **** " + str(self.account_number)[-4:]
        print("\n🏦 Account Details")
        print("----------------------")
        print(f"Name: {self.name}")
        print(f"Account Number: {masked}")
        print(f"Balance: ₹{self.balance}")    

user1 = atm("manveer",9678746287346,9008,8089)
user1.login()


# furthur..............
# Transaction history
# Multiple users (like real bank database)
# PIN retry limit (3 attempts)
# CSV file to store accounts