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

    def showall_employees(self):
        if not self.employees:
            print("not employees fund")
        else:
            print("employee list")
            for emp in self.emloyees:
                print(emp)
            print
manager=EmployeeManager()

print("employee management system")
print("enter your choice :(1-6)")
print("1.Add employee")
print("2.search employee")
print("3.update salary")
print("4.delete employees")
print("5.show all employees")
print("6.exit")

choice=input("enter you choice(1-6):")

if choice=="1":
    id=int(input("Enter  employee id: "))
    name=input("enter employee name: ")
    role=input("enter role:")
    salary=float(input("enter your salary:"))
    emp=employee(id,name,role,salary)
    manager.add_employees(emp)
elif choice=="2":
    emp_id=int(input("enter employee id to search:"))
    emp=manager.search_employee(id)
    if emp:
        print("employee found:",emp)
    else:
        print("employees not found")
elif choice=="3":
    emp_id=int(input("enter employee id to update salary:"))
    salary=float(input("enter a new salary"))
    manager.update_salary(emp_id,salary)
elif choice=="4":
    emp_id=int(input("enter employee id to delete employee:"))
    manager.delete_employee(emp_id)
elif choice=="5":
    manager.showall_employees()
elif choice=="6":
    print("exit status")
    #break
else:
    print("invalid choice")