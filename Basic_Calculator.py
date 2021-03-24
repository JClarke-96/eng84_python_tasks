# Add two numbers
def add(num1, num2):
    return num1 + num2


# Subtract one number from another
def subtract(num1, num2):
    return num1 - num2


# Multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Divide one number by another
def divide(num1, num2):
    return num1 / num2


# Calculate area of a circle
def circle(num1):
    return 3.14 * (num1 * num1)


# Calculate area of a square
def square(num1):
    return num1 * num1


# Calculate area of a triangle
def triangle(num1, num2):
    return 0.5 * num1 * num2


# Ask user for numbers to use in calculation
def input_numbers():
    global num1
    num1 = int(input("What is the first number?    "))
    global num2
    num2 = int(input("What is the second number?    "))

# Asks user what they would like to use the calculator for
def user_choice():
    print("Please choose one of the following options:")
    calculator_use = input("ADD/SUBTRACT/MULTIPLY/DIVIDE/CIRCLE/SQUARE/TRIANGLE or END    ").upper()
    if calculator_use == "ADD":
        input_numbers()
        print(add(num1, num2))
    elif calculator_use == "SUBTRACT":
        input_numbers()
        print(subtract(num1, num2))
    elif calculator_use == "MULTIPLY":
        input_numbers()
        print(multiply(num1, num2))
    elif calculator_use == "DIVIDE":
        input_numbers()
        print(divide(num1, num2))
    elif calculator_use == "CIRCLE":
        input_numbers()
        print(circle(num1))
    elif calculator_use == "SQUARE":
        input_numbers()
        print(square(num1))
    elif calculator_use == "TRIANGLE":
        input_numbers()
        print(triangle(num1, num2))
    elif calculator_use == "END":
        global in_use
        in_use = False
    else:
        print("Invalid input")


# Display info to the user about the calculator5
print("This calculator can add, subtract, multiply, or divide two numbers")
print("It can also calculate the area of a circle, square, or triangle")

# Keep using calculator until user enters END
in_use = True
while in_use:
    user_choice()
