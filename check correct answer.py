answer="abaacb"
q = input("Enter your answer: ")

mark=0
for i in range (len(answer)):
    true = 1
    false = 0
    if (answer[i]==q[i]):
        mark +=1
        print (true)
    else:
        print(false)
       
print ("your mark is: ", mark,"out of", len(answer))
        

def grade_exam (q,markforeach):
    sum_mark = 0
    answer=input("Enter the correct answer".q)
    q = input("Enter your answer: ")

    for i in range (len(answer)):
        true = 1
        false = 0
        if (answer[i]==q[i]):
            sum_mark+= markforeach
            print (true)
        else:
            print(false)
           
    print ("your mark is: ", sum_mark,"out of", len(answer))      
grade_exam(12,2)