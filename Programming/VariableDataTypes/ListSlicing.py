li1 = [10,20,30,40,50,60]

sub_list1 = li1[::]
print(sub_list1)#[10, 20, 30, 40, 50, 60]

sub_list2 = li1[1::]
print(sub_list2)#[20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3)#[10, 30, 50]

rev_list = li1[::-1]
print(rev_list)#[60, 50, 40, 30, 20, 10]