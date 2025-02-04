'''
1.In dict we can store duplicate keys
2.In dict we can store dublicates values
3.disct ar mutable

'''

d1 = {'name':'Rohith', 'age' : 22, 'Phone': 1353432}
print(d1,type(d1))#{True, 33.99, 'rohith', 20, 10} <class 'set'>

d1['name'] ='Sai'
print(d1)#{'name': 'Sai', 'age': 22, 'Phone': 1353432}

marks ={'sci':75,'Math':44}#Allowed


for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)