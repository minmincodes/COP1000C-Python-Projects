#
# Minh D Le
#
#guessNumber.py
#
# This game allows users to guess a number under a certain amount of times, if user wins, user is prompted to play again or not.
# Game repeats itself as player wants to keep playing.
#

import random

# Constants
MAX_ROUNDS_PER_GAME = 7
MIN_NUMBER = 1
MAX_NUMBER = 100

# Function to get player's guess with input validation
def get_guess(first, last):
    while True:
        try:
            guess = int(input(f"Guess the number ({first}-{last}): "))
            if first <= guess <= last:
                return guess
            else:
                print("Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to provide feedback on player's guess
def guess_win(number, guess):
    if guess > number:
        print("Too High...")
    elif guess < number:
        print("Too Low...")
    else:
        print("Congratulations! You guessed the number.")
        return True
    return False

# Main game loop
def main():
    print("Welcome to the Number Guessing Game!")

    while True:
        # Generate a new mystery number for each game
        mystery_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        rounds_left = MAX_ROUNDS_PER_GAME

        print("\nNew Game! Try to guess the mystery number.")

        # Game loop for each round
        while rounds_left > 0:
            player_guess = get_guess(MIN_NUMBER, MAX_NUMBER)

            if guess_win(mystery_number, player_guess):
                break

            rounds_left -= 1
            print(f"Rounds left: {rounds_left}")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
