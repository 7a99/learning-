class Employee:
    def __init__(self, emp_name, emp_id,emp_salary, emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        
    def calculate_emp_salary(self,emp_salary, hours_worked):
        self.emp_salary=emp_salary
        self.hours_worked=hours_worked
        if hours_worked > 50:
            overtime = self.hours_worked - 50
            overtime_amount = (overtime* (self.emp_salary/50))
            print (overtime)
            print (overtime_amount)
        
    def emp_assign_department(self, emp_department):
        emp_department.update()
        
    def print_emp_details(self, emp_name, emp_id,emp_salary, emp_department):
        print("the details of {} from Employee class".format(self.emp_name, self.emp_id, self.emp_salary, self.emp_department))
        
emp1 = Employee("ADAMS","E7876",50000, "ACCOUNTING")
emp2 = Employee("JONES","E7499",45000, "RESEARCH")
emp3 = Employee("MARTIN","E7900",50000,"SALES")
emp4 = Employee("SMITH","E7698",55000,"OPERATIONS")
print(emp1.calculate_emp_salary())

#     @classmethod
#     def creat_employee(cls,name,dob):
#         age= 2023-dob
#         return cls(name,age)
