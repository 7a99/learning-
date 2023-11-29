class Person:
    num = 0
    def __init__(self, name, age=22): ##to create the attributes of the class
        self.name = name
        self.age =age
        Person.num +=1
    def set_name (self, new_name):
        self.__name = new_name
    def __str__(self):
        return "hello {} you are {} years old".format(self.name,self.age)
    def talk(self):
        return "{} is talking".format(self.name)
p1 = Person("Hajer",23)
p2 = Person("Sara",20)
p3 = Person("Noora")
p2.set_name("shhh")
print(p1)
print(p2)
print(p3.age)
print(p3.num)

        