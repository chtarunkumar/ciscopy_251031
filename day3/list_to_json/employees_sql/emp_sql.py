from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,Float,create_engine

Base=declarative_base()
class Employee(Base):
    __tablename__='employees'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)
    job_title=Column(String(150),nullable=False)
    salary=Column(Float,nullable=False)

    def __repr__(self):
        return f'[id={self.id},name={self.name},job_title={self.job_title},salary={self.salary}]'


# from sqlalchemy.orm import declarative_base,sessionmaker
# from sqlalchemy import Column,String,Integer,Float,create_engine

# Base=declarative_base()
# class Employee(Base):
#     __tablename__='employees'
#     id=Column(Integer,primary_key=True)
#     name=Column(String(255),nullable=False)
#     job_title=Column(String(150),nullable=False)
#     salary=Column(Float,nullable=False)

#     def __repr__(self):
#         return f'[id={self.id},name={self.name},job_title={self.job_title},salary={self.salary}]'

# #setup database
# engine=create_engine('sqlite:///employees_db.sqlite',echo=True) # create a database if it not exists
# Base.metadata.create_all(engine) # create the tables

# #setup things for transcations(crud ops)
# sessionLocal=sessionmaker(bind=engine)
# session=sessionLocal()

# #crud ops
# dravid=Employee(name='dravid',job_title='old coach',salary=1200)
# session.add(dravid)
# session.commit()

# Tarun=Employee(name='Tarun',job_title='SDE',salary=35)
# session.add(Tarun)
# session.commit()

# employees=session.query(Employee).all()
# print(employees)

# lav=session.query(Employee).filter_by(name="Lavanya").first()
# print(lav)

# Tarun.salary=38000
# session.commit()

# employees=session.query(Employee).all()
# print(employees)
