class Employee:
    def __init__ (self, name,age):
        self.name = name
        self.age = age

    def work(self):
        print(self.name , " Is working")

e1 = Employee("Poja",10)
e1.work()