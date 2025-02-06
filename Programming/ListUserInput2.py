#ex-->1
li = input('Enter space seperated Eleement: ')

print(li,type(li))#12 23 55 44 66  <class 'str'>
li =li.split()
print(li)#['12', '23', '55', '44', '66']
li = list(map(int,li))
print(li)#[12, 23, 55, 44, 66]



#ex-->2
tup = tuple(map(int,input('Enter space seperated Element: ').split()))
print(tup)#(11, 22, 44, 55, 66, 88)