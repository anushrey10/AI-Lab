"""Create a program that takes two numbers as input, adds them, and
prints the result. Ensure they handle cases where the inputs might be
strings (requiring type conversion)."""

def add_numbers():
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = int(num1)
        num2 = int(num2)
        
        result = num1 + num2
        
        print(f"The result of adding {num1} and {num2} is: {result}")

add_numbers()