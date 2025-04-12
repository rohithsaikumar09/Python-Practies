class cal:
    def calsi(self, a, b):
        print("Result of a and b")

class Add(cal):
    def calsi(self, a, b):
        print("Addition: ", a + b)

class Sub(cal):
    def calsi(self, a, b):
        print("Subtraction: ", a - b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def permit(ref, a, b):
    ref.calsi(a, b)

# Example usage:
permit(Add(), a, b)
permit(Sub(), a, b)
