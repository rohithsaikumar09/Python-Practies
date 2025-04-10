class Demo1:
    def disp1(self):
        print('Inside the Disp 1')
class Demo2:
    def disp2(self):
        print('Inside the Disp 2')

class Demo3(Demo1,Demo2):
    pass


D1 = Demo3()
D1.disp1()
D1.disp2()
