class BankAccount:
    def __init__(self):
        self.__balance = 0 # private variable.

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposite of {amount} Sucessful. Current Balance: {self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive Value.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawl of {amount} seccessful. Current balance: {self.__balance}")
        else:
            print("Withdrawl failed. Insuffient Balance.")

    def get_balance(self):
        return self .__balance
    

# Create instance of Bank Account
account = BankAccount()

depodit_amount = int(input("Enter a Deposit Amount: "))
withdraw_amount = int(input("Enter a withdraw Amount: "))

account.deposite(depodit_amount)
account.withdraw(withdraw_amount)