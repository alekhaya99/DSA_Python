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

class Infant(Patient):
    ''' Patient under 2 years'''
    
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name,age)
        
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Patient has had {self.vaccinations} vaccines.' \
               f' Current information: {self.conditions}.' \
               f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')


archie = Infant('Archie Fittleworth',0)        
archie.add_vac('MMR') 

print(archie.get_details())
         