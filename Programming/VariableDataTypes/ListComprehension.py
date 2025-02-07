li1 = [1,2,3,4,5]

# print(li1)

# sq_li = []

# for i in li1:
#     sq_li.append(i**2)
# print(sq_li)


duplicate_li =[i for i in li1] #print as it is
even_li = [i for i in li1 if i%2 ==0]#print even numbers
square_li = [i**2 for i in li1 ]#print square of all terms in list
odd_li = [i for i in li1 if i%2!=0]#print odd numbers
new_ele = [ele+2 for ele in li1]#Add +2 for all elements

print(duplicate_li)#[1, 2, 3, 4, 5]
print(even_li)#[2, 4]
print(square_li)#[1, 4, 9, 16, 25]
print(odd_li)#[1, 3, 5]
print(new_ele)#[3, 4, 5, 6, 7]

#list Comprehension for  if and else condition:
even_odd = [ 'even'if i%2 == 0 else 'odd' for i in li1]
print(even_odd) #['odd', 'even', 'odd', 'even', 'odd']


#multiple for loops Inside List Comprehsion
li = [[10,20],[30,40],[50,60]]

result =[ele for i in li for ele in i]
print(result)