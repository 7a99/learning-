# file = open("text.txt", "r")
# line= file.readline() # to print first line
# print(file.readline())
# print(file.read()) # to print all document
# print(line)
# while (line != ""):
#     line= file.readline()
#     print(line)
# 
# #read from file mode:
# count =0
# file = open("text.txt", "r")
# line= file.readline()
# sum_ = float(line)
# # find avg by using while loop
# while (line != ""):
#     line= file.readline()
#     count+=1
#     avg = (sum_ /count)
# print(avg)
# 
# #by using for loop
# for line in file:
#     sum_ = float(line)
#     count +=1
# print(sum_ /count)
# 
# #write in file mode:
# 
# file = open("text.txt", "w")
# print("hello python", file= file)
# file.close()

file = open("text.txt", "r")
for line in file:
    line=line.split(" ")
    mark = int(line)
        if mark > 70:
            print(line[0], "mark is: ", line[1])