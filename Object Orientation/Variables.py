class Bank:
    #class Base Variables
    bank_name = "ICCI"

    def __init__(self,name,age,balance):
        #instance Variables
        self.user_name = name
        self.user_age = age
        self.User_balance = balance


    def display_info(self):
        print(f'Bank Name: {Bank.bank_name}, Name: {self.user_name}, Age: {self.user_age}, balance: {self.User_balance}')



#Taking User Input
name = input()
age = int(input())
balance = float(input())

#Creating Object
p1 = Bank(name, age, balance)


p1.display_info()#Bank Name: ICCI, Name: Ajay, Age: 22, balance: 4567.0