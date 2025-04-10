class grandParent():
    def cook(self):
        print('Can cook Biryani')
class parent(grandParent):
    def cook(self):
        print('can cook Rice')

class child(parent):
    def cook(self):
        print("can't cook")
        super(parent,self).cook()
        super().cook()

c = child()
c.cook()