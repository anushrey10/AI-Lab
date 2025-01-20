"""Write a Python program to generate the Fibonacci series up to a
specified number of terms. Use a while loop and branching to
implement the logic."""

def fibonacci_series():
    terms = int(input("Enter the number of terms: "))
    
    if terms <= 0:
        print("Please enter a positive integer.")
        return
    
    print("Fibonacci Series:")

    first, second = 0, 1
    count = 0

    while count < terms:
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term
        count += 1

fibonacci_series()