import pickle
import os

file_name='employees_db.dat'
def read_employees(employees):
    with open(file_name,'wb') as out_file:
        pickle.dump(employees,out_file)

    with open(file_name,'rb') as in_file:
        pickle.load(in_file)
    if os.path.exists(file_name):
        print(f"the file_name{file_name} exists")
    else:
        print(f"the file doesn't exist{file_name}")

read_employees()