"""
1. Conditional : if, else, if-else
2. Looping : for, while
3.Jumping : break, continue, pass
"""

# def checkAge(age):
#     if(age >= 18):
#         print("Age is greater than 18")
#     else:
#         print("Age is not greateer than 18")

age = int(input("ENter your age"))
if(age < 18):
    print("Your Child")
elif(age >=18 and age <65):
    print("Your Adult")
else:
    print("Your Senior Citizen")

