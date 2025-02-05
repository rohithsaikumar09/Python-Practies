# li = input('Enter space seperated Eleement: ')

# print(li,type(li))#12 23 55 44 66  <class 'str'>
# li =li.split()
# print(li)#['12', '23', '55', '44', '66']
# li = list(map(int,li))
# print(li)#[12, 23, 55, 44, 66]

tup = tuple(map(int,input('Enter space seperated Element: ').split()))
print(tup)