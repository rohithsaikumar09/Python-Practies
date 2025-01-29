# Step 1: Get the number of rows for the upper half of the diamond
n = int(input("Enter the number of rows for the upper half: "))

# Step 2: Loop for the upper half of the diamond
for i in range(n):
    # Print leading spaces for centering
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars, with spaces in between
    print("*", end="")
    if i > 0:  # Skip the inner space for the first row
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    
    # Move to the next line after each row
    print()

# Step 3: Loop for the lower half of the diamond
for i in range(n - 2, -1, -1):  # Reverse order for the lower half
    # Print leading spaces for centering
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars, with spaces in between
    print("*", end="")
    if i > 0:  # Skip the inner space for the first row
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    
    # Move to the next line after each row
    print()
