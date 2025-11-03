employees=[]

def add_employee(employee):
    employees.append(employee)
    print("employee added success")

def search_employee(id):
    i=0
    for employee in employees:
        if employee["id"]==id:
            return i
        i+=1
    return -1

def update_salary(id,salary):
    index=search_employee(id)
    if index!=-1:
        employees[index]["salary"]=salary
        print("salary updated successfull")
    else:
        print("employees not found")

def delete_employee(id):
    index=search_employee(id)
    if index!=-1:
        employees.pop(index)
        print("employee deleted successfully")
    else:
        print("not found")


add_employee({"name":"Tarun","id":101,"role":"software engineer","salary":38000})
add_employee({"name":"rakesh","id":102,"role":"software autmation","salary":40000})

print(employees)
found_index=search_employee(102)

if found_index!=-1:
    print("employee found",employees[found_index])
else:
    print("employees not found")

update_salary(102,76000)
delete_employee(102)
for emp in employees:
    print(emp)