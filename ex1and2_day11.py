class BankAccount:
    def __init__(self, balance, account_num):
        self.balance=balance
        self.account_num = account_num
        
    def deposit(self):
        deposit_ = int(input("Enter the deposit num: "))
        amount = self.balance + deposit_
        print (f"the amount of account {self.account_num} is",amount)
        
    def withdrawal(self):
        withdrawth = int(input("Enter the withdrawth num: "))
        if withdrawth < self.balance:
            amount = self.balance - withdrawth
            return amount
        else:
            print("your balance is low!!")
    
    def displaying_info(self): 
        print("account num:", self.account_num)
        print("balance:", self.balance)

b1 = BankAccount (50000,2938478925241)
b1.displaying_info()
b1.deposit()
b1.withdrawal()
