avg=0
# sum_=0
# stu=int(input("Enter the num of student: "))
def grade_avg (x):
    sum_=0
    for i in range (1,x+1):
        grade=float(input("Enter student grade: "))
        sum_ += grade
    avg = sum_/x
    return(avg)

result= grade_avg (2)
print(result)
