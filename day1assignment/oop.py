class employee:
    def __init__(self,name,id,role,salary):
        self.name=name
        self.id=id
        self.role=role
        self.salary=salary

    def __str__(self):
        return f"Name:{self.name},id:{self.id},role:{self.role},salary:{self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employees=[]
    
    def add_employees(self,employee):
        self.employees.append(employee)
        print("Employee added successfully")

    def search_employee(self,id):
        for emp in self.employees:
            if emp.id==id:
                return emp
        return None
    
    def update_salary(self,id,salary):
        index=self.search_employee(id)
        if index:
            index.salary=salary
            print("salary updated successfully")
        else:
            print("employees not found")

    def delete_employee(self,id):
        index=self.search_employee(id)
        if index:
            self.employees.remove(index)
        else:
            print("employees not found")
manager=EmployeeManager()
e1=employee("Tarun",101,"software trainee",38000)
e2=employee("kowshik",102,"automation deeloper",70000)
manager.add_employees(e1)
manager.add_employees(e2)
emp=manager.search_employee(101)
manager.update_salary(102,90000)
manager.delete_employee(101)
if emp:
    print("employee found:",emp)
else:
    print("employee not found!")
for emp in manager.employees:
    print(emp)

