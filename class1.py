""" We are Creating a Class for real life environment, Like an ATM machine Program with 
basic features like set pin, deposit amount, withdrawl amount and etc"""

class Atm:
    def __init__(self): #constructor
            self.pin=""     #intializing the data variables
            self.balance=0
            self.menu()  #calls the menu method

    def menu(self):
        user_input = input(""" Welcome to this Class of ATM here are some options for you so you can choose accordingly and 
                           enjoy the ATM functionality 
                           
                        1. Enter 1 to create Pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check Balance
                        5. Enter 5 to exit  """)
        if user_input=="1":
             print("creating the pin")
             self.create_pin()
        elif user_input=="2":
             print("Depositing the amount")
             self.deposit_amount()
        elif user_input=="3":
             print("Withdrawing the amount")
             self.withdraw_amount()

        elif user_input=="4":
             print("Showing Balance")
             self.show_balance()
        else:
             print("Thanks For Coming")

    
    
    def create_pin(self):
         self.pin=input("Enter the Pin")
         print("Pin changed succesfully")
    
    
    def deposit_amount(self):
         temp=input("Enter the pin")
         if temp==self.pin:
            deposit=int(input("Enter the amount you want to deposit"))
            self.balance+=deposit
            preview=input("Press 1 to show the balance or 2 to skip")
            if preview=="1":
                self.show_balance()
            else:
                print("Thanks for coming")
         else:
              print("Invalid Pin") 

    def withdraw_amount(self):
         temp=input("Enter the pin")
         if temp==self.pin:
            withdraw=int(input("Enter the amount you want to withdraw"))
            if withdraw <= self.balance:
                 self.balance-=withdraw
                 preview=input("Press 1 to show the balance or 2 to skip")
                 if preview=="1":
                    self.show_balance()
                 else:
                    print("Thanks for coming")
            else:
                 print("Insufficient Funds")     
            
         else:
              print("Invalid Pin") 

    def show_balance(self):
          temp=input("Enter the pin")
          if temp==self.pin:
            print(self.balance)   
          else:
               print("Invalid Pin") 
