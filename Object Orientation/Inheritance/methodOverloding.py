class Demo:
    def disp(self):
        print('inside disp with 0 par')
    def disp(self,a):
        print('inside disp with 1 par')
    def disp(self,a,b):
        print('inside disp with 2 par')

d = Demo()

# d.disp()
# d.disp(1)
d.disp(10,20)