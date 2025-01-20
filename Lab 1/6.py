"""Create a program that takes user input and checks whether the
entered number is a prime number or not. Utilize a for loop and
branching statements."""

def check_prime():
    number = int(input("Enter a number: "))
    
    if number <= 1:
        print(f"{number} is not a prime number.")
        return
    
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return
    
    print(f"{number} is a prime number.")

check_prime()