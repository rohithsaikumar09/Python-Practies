#map (function , iterable_object)--> Iterable object

def double(x):
    return x*2

li = [1,2,3,4,5]
double_li = list(map(double,li))
print(double_li)#[2, 4, 6, 8, 10]

tup = ('10', '20', '30')
print(tup)
tup = tuple(map(int,tup))
print(tup)#(10, 20, 30)

li2 = [1,4,55]
print(li2)#[1, 4, 55]
li2 = list(map(float,li2))
print(li2)#[1.0, 4.0, 55.0]