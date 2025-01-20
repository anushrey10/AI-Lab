"""Implement a simple Guess the Number game in Python. In the game, the user has to guess a randomly generated number. Use branching, looping, and flow control
    statements to manage the game's flow. Some salient features of the game implementation is as follows:
    a) Use the random module to generate a random number between a specified range. This will be the number the user needs to guess.
    b) Use a while loop to repeatedly prompt the user for their guess until they correctly guess the number.
    c) Use if..else statements to check if the user's guess is correct, too high, or too low. Provide appropriate feedback.
    d) Introduce flow control statements like continue to skip certain parts of the loop or break to exit the loop when the correct guess is made."""
    
import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Prompt the user for their guess
            user_guess = int(input("Enter your guess (1-100): "))
            
            # Increment the attempts counter
            attempts += 1
            
            # Check if the user's guess is correct, too high, or too low
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range 1-100.")
                continue
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    print("Thank you for playing the Guess the Number game!")

# Run the game
guess_the_number()