List = [1,2,3,4]

for i in range (len(List)):
    print(List[i]) #to print the element of list # if i want the index print (i) if i use range

print("-----------")
# if I want to print the elements in spesific index
for i in [2,4]: 
    print (i)
    
"-----------------"
s= [1,2,3,4,8]
x = s.copy()
print(x)
x[4]= 5
print(x)
print(s)

#ex1: print the element without comma but with space
x = [1,2,3]
for i in x:   
    print(i, end = " ")   
print()
#ex2: print the list * 2
s = [1,2,3]
for i in s:
    print(i*2, end = " ")
print()

#ex3: count negative number
count=0
m = [-1,2,5,-3,8]
for i in m:
    if (i<0):
        count += 1
print(count)

"##################################"
#append function ---> append value at the end of the list
f = []
f.append("hajer")

#insert function ---> insert the value in spesefic position (posetion,value)
f.insert(1,"sara")

#find function ---> to search for spesific element in a list
f.index("sara")
print(f)

#remove function ---> (pop()---> to remove element from the end of list)
                    # (remove() ----> to remove spesific element from spesific position)
f.pop()
f.append("nora")
print (f)
f.append("adam")
print (f)
f.remove("hajer")
print (f)

# to repeat element in a list
v = [0]*4
print (v)
