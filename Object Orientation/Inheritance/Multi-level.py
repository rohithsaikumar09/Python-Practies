class demo1: 
    def disp1(self):
        print('inside disp1')

class demo2(demo1): 
    def disp2(self):
        print('inside disp2')

class demo3(demo2):
    pass

d = demo3()
d.disp1()
d.disp2()