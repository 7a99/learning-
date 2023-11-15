#write a program that calculates the discount based on total amount
#if the total amount is grater than 100$
#apply a 10% dicount, otherwise apply 5% discount

total_amount =int(input("enter the amount"))

if (total_amount > 100):
    discount=total_amount*10/100
else:
    discount=total_amount*5/100
    
print ("your total amount is: ", total_amount-discount)
    