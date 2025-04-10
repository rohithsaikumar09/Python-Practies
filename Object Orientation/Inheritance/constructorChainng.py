class grandParent:
    def __init__(self):
        self.x = 100

class parent(grandParent):
    def __init__(self):
        self.y = 200
        super().__init__()

class child(parent):
    def __init__(self):
        self.z = 300
        super().__init__()

c = child()
print(c.z)
print(c.y)
print(c.x)