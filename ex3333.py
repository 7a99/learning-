try:
    n = input ("Enter a value: ")
    print (int(n))
    
except ValueError:
    print ("invalid literal")
finally:
    print("Done")