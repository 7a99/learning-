# class Person:
#     def __init__(self, name, gender, age=22):
#         self.name = name
#         self.age =age
#         self.gender =gender
#     def say_hi(self):
#         print("hello {} from parent class".format(self.name))
# class Student(Person):
#     def __init__(self, name, age=22):
#         super().__init__(name, age)
#     def say_hi(self):
#         print("hello {} from student class".format(self.name))
#         
# p1 = Person("A", 22)
# s1 = Student("B", 15)
# s2 = Student("C")
# s1.say_hi()
# p1.say_hi()

class Shape:
    def __init__(self, color, name):
        self.color =color
        self.name = name
    
    def area(self):
        return "Area of parent class"
         
    def discription(self):
        print("I'm {} from Shape class".format(self.name))
        
class Sequare (Shape):
    def __init__(self, color, name, side):
        self.side=side
        super().__init__(color, name)
    def area(self):
        area1 = self.side * self.side
        return area1
    
class Circle (Shape):
    def __init__(self, color, name, radius):
        self.radius = radius
        super().__init__(color, name)
    def area(self):
        area2 = 3.14*(self.radius**2)
        return area2
    
seq = Sequare("red","Sequare1",3)
cir = Circle("blue","circle1",2)
sh = Shape ("blue", "shape")
print(seq.area())
print(cir.area())
print(sh.area())
seq.discription()