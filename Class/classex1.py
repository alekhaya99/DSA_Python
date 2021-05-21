class Patient(object):
    status='patient'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.conditions=[]
    def get_details(self):
        print(f'The name is {self.name} and the age is {self.age}'\
            f'Current information: {self.conditions}')
    def add_info(self,information):
        self.conditions.append(information)

Pat1=Patient("Name1",54)
Pat2=Patient("Name2",45)

print(Pat1.name)
print(Pat2.age)
print(Pat1.status)
Pat1.add_info("Hello World")
print(Pat1.get_details())
