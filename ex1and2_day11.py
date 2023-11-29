class BankAccount:
    def __init__(self, balance, account_num):
        self.__balance=balance
        self.__account_num = account_num
        
    def deposit(self):
        deposit_ = int(input("Enter the deposit num: "))
        amount = self.__balance + deposit_
        print (f"the amount of account {self.__account_num} is",amount)
        
    def withdrawal(self):
        
        try:
            withdrawth = float(input("Enter the withdrawth num: "))
            if withdrawth>0:
                if withdrawth < self.__balance:
                    amount = self.__balance - withdrawth
                    return amount
                else:
                    return ("Error: your balance is low!!")
            else:
                return ("Error: your amount is less than 0!")
        except:
            return ("invalid input")
            
    
    def displaying_info(self): 
        print("account num:", self.__account_num)
        print("balance:", self.__balance)

b1 = BankAccount (50000,2938478925241)
b1.displaying_info()
b1.deposit()
print(b1.withdrawal())
