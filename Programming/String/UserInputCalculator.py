# Calculator Program

# Addition
A1 = float(input("Enter Number 1 for addition: "))  # Convert input to float
A2 = float(input("Enter Number 2 for addition: "))  # Convert input to float
print("Addition: " + str(A1 + A2))  # Perform addition and convert the result to string for printing

# Subtraction
s1 = float(input("Enter Number 1 for Subtraction: "))  # Convert input to float
s2 = float(input("Enter Number 2 for Subtraction: "))  # Convert input to float
print("Subtraction: " + str(s1 - s2))  # Perform subtraction and convert the result to string for printing

# Multiplication
m1 = float(input("Enter Number 1 for Multiply: "))  # Convert input to float
m2 = float(input("Enter Number 2 for Multiply: "))  # Convert input to float
print("Multiplication: " + str(m1 * m2))  # Perform multiplication and convert the result to string for printing

# Division
d1 = float(input("Enter Number 1 for divide: "))  # Convert input to float
d2 = float(input("Enter Number 2 for divide: "))  # Convert input to float

# Handle division by zero
if d2 != 0:
    print("Division: " + str(d1 / d2))  # Perform division and convert the result to string for printing
else:
    print("Error: Division by zero is not allowed.")

