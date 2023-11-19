# Write a python code to draw this shape:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
for i in range (1,5):
    print("*"*i)
for j in range (5,0,-1):
    print("*"*j)

"""
given a number and its divisors, find it the number is perfect
"""
num = int(input("Enter the num to be checked: "))
pos_divisors = input("Enter the positive divisors of the num: ")
sum_ = 0
# print([int(i) for i in pos_divisors.split(",")])
List = []
for i in pos_divisors.split(","):
    List.append(int(i))   
    perfect_num= sum(List)
# calculate the sum
#sum_ = sum(List)
for i in range (0, len(List)): #
    sum_ += List[i]
# compare   
if (sum_ == num ):
    print(num)

# Print all perfect number from 1 to 100, if you know that a perfect 
# number is a positive integer that is equal to the sum of its 
# positive divisors, excluding the number itself. For instance, 6 has 
# divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a 
# perfect number.
    
for num in range (1,101):
    divisors = []
    for j in range(1, num):
        if num%j == 0:
            divisors.append(j) 
    
    sum_ = sum(divisors)
    
    if (num == sum_):
        print(num)
    
    
    
    
    
    
