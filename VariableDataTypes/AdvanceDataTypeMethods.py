li1 = list('rohith')
print(li1)#['r', 'o', 'h', 'i', 't', 'h']

li2 = list((10,20,30))#tuple
print(li2)#[10, 20, 30]

li3 = list({100,200})#set
print(li3)#[200, 100]

li4 = list({'Name':'Rohith', 'Age': 22})#dist
print(li4)#['Name', 'Age']

li5 = list(range(1,11))
print(li5)

#tuple (iterable_object)
tu1 = tuple('ROhith')#string
tu2 = tuple({100,200,300})#set
tu3 = tuple([10,20,30])#List
tu4 = tuple(range(1,11))
tu5 = tuple({'name':'rohu','age':22})#dist

print(tu1)#('R', 'O', 'h', 'i', 't', 'h')
print(tu2)#(200, 100, 300)
print(tu3)#(10, 20, 30)
print(tu4)#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tu5)#('name', 'age')

#set (iterable_object)
s1 = set('Rohu')
s2 = set([10,20,30])
s3 = set(range(1,11))
s4 = set((1,2,3,4,5))
s5 = set({'name':'rr','age':22})

print(s1)#{'u', 'R', 'h', 'o'}
print(s2)#{10, 20, 30}
print(s3)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s4)#{1, 2, 3, 4, 5}
print(s5)#{'age', 'name'}

#dist(iterable_object:key:value)
d1 = dict([['name','Rohith'],['age',22]])
print(d1)#{'name': 'Rohith', 'age': 22}