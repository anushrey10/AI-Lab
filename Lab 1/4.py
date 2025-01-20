"""Create a Python program that functions as an advanced calculator. It
should take user input for mathematical expressions and evaluate
them, supporting basic operations, parentheses, and scientific
notation."""

def simple_calculator():
    
    expression = input("Enter a mathematical expression : ")
    
    output = eval(expression)
    
    print(f"{expression} = {output}")

simple_calculator()