# Set initial value to start at
num = 1

# Loop through each number from 1 to 100
while num <= 100:
    # Check if number is divisable for printing other values
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")       # Prints FizzBuzz if divisable by 3 and 5
    elif num % 3 == 0:
        print("Fizz")           # Prints Fizz if divisable by 3
    elif num % 5 == 0:
        print("Buzz")           # Prints Buzz if divisable by 5
    else:
        print(num)              # Prints the number if not divisable by 3 or 5
    num += 1
