class demo1:
    def disp1(self):
        print('Inside disp1')

class demo2(demo1):
    def disp2(self):
        print('Inside disp2')
class demo3(demo1): 
    pass


d1 = demo2()
d1.disp1()
d1.disp2()

d2 = demo3()
d2.disp1()