from random import randint

num = randint(1,20)

while (True):
    gussed_num= int(input("Enter any number: "))
    if ( gussed_num > num):
       print("Wrong number! go down")
       continue
    elif (gussed_num < num):
       print("Wrong number! go up")
       continue
    else:
       print("correct number!")
    break