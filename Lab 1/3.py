"""Write a program that takes an integer input, checks if it's even or
odd, and prints a message accordingly. Additionally, use the modulo
operation for this determination."""

def odd_even():
        number = input("Enter an integer : ")
        
        number = int(number)
        
        if number%2 == 0:
            print(f"{number} is an Even number.")
            
        else:
            print(f"{number} is an odd number.")

        
odd_even()