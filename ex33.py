try:
    x = [1,2,3,4,6]
    print(x[9])
    
except ZeroDivisionError:
    print("can not divide by zero")
    
except:
    print("something going wrong")
    
except Exception as exc:
    print("error: ", type(exc))
finally: