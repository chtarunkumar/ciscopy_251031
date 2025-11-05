from db_setup import session, Employee


def read_all_employees():
    employees = session.query(Employee).all()
    return employees


def add_employee(employee):
    session.add(employee)
    session.commit()
    print('Employee Added Successfully')


def search_employee(id):
    employee = session.query(Employee).filter_by(id=id).first()
    return employee
 
def update_employee(id, salary):
    old_employee = search_employee(id)
    if old_employee:
        old_employee.salary = salary
        session.commit()
        print('Employee Updated Successfully')
    else:
        print('Employee Not Found.')


def delete_employee(id):
    old_employee = search_employee(id)
    if old_employee:
        session.delete(old_employee)
        session.commit()
        print('Employee Deleted Successfully')
    else:
        print('Employee Not Found.')
# from db_setup import session, Employee

# # import db_json as db 
# # from log import logging

# try:
#     employees = db.read_employees()
#     logging.info("Employees loaded successfully from database.")
# except Exception as e:
#     logging.error(f"Failed to load employees from database: {e}")
#     employees = []
# #employees = db.read_employees() #employee is object of attr (id, name, job_title, salary)
# # list of objects -> list of dict -> save to file
# # read from file -> list of dict -> list of objs

# def add_employee(employee):

#     employees.append(employee)
#     db.write_employees(employees)
#     logging.info('Employee Added Successfully')


# def search_employee(id): 
#     I = 0
#     for employee in employees: 
#         if employee.id == id:
#             return I
#         I += 1
#     return -1 
 
# def update_employee(id, salary):
#     index = search_employee(id)
#     if index != -1:
#         employee = employees[index]
#         employee.salary = salary
#         db.write_employees(employees)
#         logging.info('Employee Updated Successfully')
#     else: 
#         logging.info('Employee Not Found.')

# def delete_employee(id):
#     index = search_employee(id) 
#     if index != -1:
#         employees.pop(index)
#         db.write_employees(employees)
#         logging.info('Employee Deleted Successfully')
#     else: 
#         logging.info('Employee Not Found.')