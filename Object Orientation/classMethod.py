class Student:
    collage_name = "ABCD"

    
    def info(self):
        print('Collage Name is: ', Student.collage_name)

    @classmethod
    def change_name(cls, newName):
        cls.collage_name = newName


s1 = Student()
s1.info()
s1.change_name("JNTU")
s1.info()