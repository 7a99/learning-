gender = input ("Enter your gender: ")

if ( gender.upper() == "M" ):
    
    age = int (input ("Enter your age:"))
    if (24<=age<=30):
        print ("Accepted")
        
    else:
        print ("your age is not matches")
        
else:
    
    print ("Rejected")
        