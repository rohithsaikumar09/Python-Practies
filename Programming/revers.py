#object.revers() will reverse the original object
li = [10,5,20,7 ,40]   
print('Before Revers:' ,li)
li.reverse()
print('After Revers: ', li)

#reversed(object):
li2 = [11,3,44,66]
reversed_li = tuple(reversed(li2))
print(li2)
print(reversed_li)


li3 = [10,22,34,55,56]
reverse_li3 = list(reversed(li3))#--> creating new revers List
li3.reverse()#-->Reversing Original List
print(reverse_li3)

