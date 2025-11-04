import pickle
class employee:
    def __init__(self,name,id,role,salary):
        self.name=name
        self.id=id
        self.role=role
        self.salary=salary

    def __str__(self):
        return f"Name:{self.name},id:{self.id},role:{self.role},salary:{self.salary}"
    
empoyees=[employee("Tarun",101,"software trainee",38000),
employee("kowshik",102,"automation deeloper",70000)]

file_name='employee_db_t'
print('to save employees into binary file')
with open('file_name','wb') as out_file:
    pickle.dump(empoyees,out_file)
    print('saved files into binary format')

with open('file_name','rb') as in_file:
    files_name=pickle.load(in_file)
    print('binary to normal coversaion')

print(files_name)
