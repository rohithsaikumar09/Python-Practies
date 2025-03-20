class Employee: 
    company_name = "CODE" # Class Based Variable
    def __init__(self,name, age, desig): # Instances variable
        self.name = name
        self.age = age
        self.desig = desig

    def login(self, time):
        print(f'{self.name} login at {time}')
    
    def logout(self, time):
        print(f'{self.name} is logout at {time}')
        
    def work(self, hours):
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print("Employee Name: " , self.name)
        print("Employee age: ", self.age)
        print("Designation: ", self.desig)

#Creating Objects: 
e1 = Employee("ak",22,"SED")
e2 = Employee("pk", 34, "Manager")
e3 = Employee("Rk", 33, "Developer")

e1.getDetails()