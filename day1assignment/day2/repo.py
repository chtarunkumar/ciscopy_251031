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