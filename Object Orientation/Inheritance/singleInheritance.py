class demo1:
    def disp1():
        print('Inside the disp 1')
class demo2(demo1):
    pass

d = demo2
d.disp1()