class employee:
    def __init__(self,name,id,role,salary):
        self.name=name
        self.id=id
        self.role=role
        self.salary=salary

    def __str__(self):
        return f"Name:{self.name},id:{self.id},role:{self.role},salary:{self.salary}"
    