from employee import employee
from repo import manager
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