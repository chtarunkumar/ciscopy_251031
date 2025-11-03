employees=[]

def add_employee(employee):
    employees.append(employee)
    print("employee added successfully")


def search_employee(id):
    i=0
    for employee in employees:
        if employee[1]==id:
            return i
        i=i+1
    return -1


def update_employee(id,salary):
    index=search_employee(id)
    if index != -1:
        employees[index][3]=salary
        print("salary updated")
    else:
        print("employeesnot found")


def delete_employee(id):
    index=search_employee(id)
    if index!=-1:
        employees.pop(index)
        print("employee deleted successfully")
    else:
        print("employee not found")

add_employee(['tarun',101,'software trainee',38000])
add_employee(['kowshk',102,'automation developer',45000])
add_employee(['deepak',103,'software developer',40000])

#print(employees)

#search_id=102
found_index=search_employee(102)

if found_index!=-1:
    print(employees[found_index])
else:
    print('employee not found')

update_employee(101,90000)
delete_employee(101)
for emp in employees:
    print(emp)