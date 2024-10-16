import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Number of attempts allowed
attempts = 3

print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the number between 1 and 10.")

# Loop until the player guesses the correct number or runs out of attempts
while attempts > 0:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    # Check if the guess is too high or too low
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    
    # Reduce the number of attempts left
    attempts -= 1
    print(f"Attempts left: {attempts}")

# If player didn't guess correctly within the attempts
if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")