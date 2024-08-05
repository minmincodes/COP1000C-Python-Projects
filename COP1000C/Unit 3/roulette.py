#
# Minh D Le
#
# Takes an input number from 0 - 36 and picks a color based on the numbers in the roulette, will error if number is not between 0 and 36
#

print("Roulette Wheel Colors")

def determine_pocket_color(pocket_number):
    if pocket_number == 0:
        return "Green"
    elif 1 <= pocket_number <= 10 or 19 <= pocket_number <= 28:
        return "Red" if pocket_number % 2 == 1 else "Black"
    elif 11 <= pocket_number <= 18 or 29 <= pocket_number <= 36:
        return "Black" if pocket_number % 2 == 1 else "Red"
    else:
        return "Invalid pocket number"

# Get user input for the pocket number with input validation
try:
    pocket_number = int(input("Enter the pocket number (0 to 36): "))
    if 0 <= pocket_number <= 36:
        pocket_color = determine_pocket_color(pocket_number)
        print(f"The color of pocket {pocket_number} is {pocket_color}.")
    else:
        print("Error: Invalid pocket number. Please enter a number between 0 and 36.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
