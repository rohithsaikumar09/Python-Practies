#once we declear a string we cannot modify it
# if we try to modify the string it will create new string
#2. if new String dos not have any referance variable then it will be Removed



# s1 = 'kodnest'
# s2 = s1.upper()
# print(s2)

# print(id(s1))
# print(id(s2))

s1 = 'Hello'
s2 = 'World!'
print(s1, id(s1))
print(s2, id(s2))

print(s1[0])
print(s1[-1])

print('s2 The Id of w: ',id(s2[0]))
print('s2 The Id of o: ',id(s2[1]))