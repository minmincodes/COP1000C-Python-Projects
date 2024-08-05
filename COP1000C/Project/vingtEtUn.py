#
# Minh D Le
#
# vingtEtUn.py
#
# This game is called VingtEtUn also known as Blackjack, the game simulates the real life game by allowing both player and house to play the game, trying to get closest to 21 without going over
#


import random

# Set of rules
def display_rules():
    print("Rules of Vingt-et-un:")
    print("1. The goal is to score 21 points or as close as possible without going over.")
    print("2. Players take turns throwing two dice and adding up the numbers.")
    print("3. A player who totals over 21 is bust and loses the game.")
    print("4. The player or house nearest to 21 wins after each has had a turn.")
    print("5. If there's an equality in the high total, the game is tied.")
    print("6. Once a player totals 14 or more, only one die is rolled for consecutive turns.")
    print("7. The house must throw the dice until the total is 17 or higher, and it must stay at 17 or higher.")
    print("8. The game is over when one or both players are bust, or both players choose to stay.")


# Function to roll a specified number of dice and return the sum
def roll_dice(num_of_dice):
    # Using list comprehension to generate random dice rolls and summing them
    return sum(random.randint(1, 6) for _ in range(num_of_dice))


# Function to play a round of the game for a given player
def play_round(player_name):
    # Initializing variables for total points and dice count
    total_points = 0
    dice_count = 2

    # Loop for the player's turn
    while True:
        print(f"\n{player_name}'s total: {total_points}")

        # Adjusting dice count based on total points
        if total_points >= 14:
            dice_count = 1

        # Asking the player to roll or stay
        roll_or_stay = input("Roll or Stay? (r/s): ").lower()

        # Handling player's choice to roll
        if roll_or_stay == 'r':
            # Rolling dice, updating total points, and displaying the result
            roll_result = roll_dice(dice_count)
            total_points += roll_result
            print(f"{player_name} rolled {roll_result}")

            # Checking for bust condition
            if total_points > 21:
                print(f"{player_name} is bust! Total points: {total_points}")
                return total_points

        # Handling player's choice to stay
        elif roll_or_stay == 's':
            print(f"{player_name} chooses to stay. Total points: {total_points}")
            return total_points


# Function to determine the winner of the game
def determine_winner(player_total, house_total):
    # Comparing player's and house's totals to determine the winner
    if player_total > 21 or (house_total <= 21 and house_total >= player_total):
        return "House"
    elif house_total > 21 or (player_total <= 21 and player_total > house_total):
        return "Player"
    else:
        return "Tie"


# Main function to drive the game
def main():
    print("Welcome to Vingt-et-un!")
    player_name = input("Enter your name: ")

    # Main game loop
    while True:
        print("\nMenu:")
        print("1. See the Rules.")
        print("2. Play Vingt-et-un.")
        print("3. Quit.")

        # Taking user's choice
        choice = input("Enter your choice (1, 2, or 3): ")

        # Branching based on user's choice
        if choice == '1':
            display_rules()
        elif choice == '2':
            # Playing a round for the player and the house
            player_total = play_round(player_name)
            house_total = play_round("House")

            # Determining and displaying the winner
            winner = determine_winner(player_total, house_total)
            print(f"\nGame Result: {winner} wins!\n")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Starting the game when the script is run
if __name__ == "__main__":
    main()

