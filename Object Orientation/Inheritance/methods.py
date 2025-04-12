class Student:
    def cook():
        print('Student Can cook')
    def play():
        print(' is Playing')

class Employee(Student):
    def cook():
        print('Employee is cooking ')
    def work():
        print("Employee is working")


'''
work() = Specialized Method : only in child class
cook() = overriden Method : change the Implementations
play() = inheritated Method : as it is

'''