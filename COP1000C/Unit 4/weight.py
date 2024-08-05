#
# Minh D Le
#
# This app will give user options of choice with answers behind each choice for weightloss
#


# Prints the 10 ways guideline
def cut_calories_guidelines():
    print("Try these 10 ways to cut 500 calories every day:")
    print("1. Swap your snack.")
    print("2. Cut one high-calorie treat.")
    print("3. DO NOT drink your calories.")
    print("4. Skip seconds.")
    print("5. Make low-calorie substitutions.")
    print("6. Ask for a doggie bag.")
    print("7. Just say 'no' to fried food.")
    print("8. Build a thinner pizza.")
    print("9. Use a smaller plate.")
    print("10. Avoid alcohol.")
    print("Source: US National Library of Medicine")
# Expected weight table display
def generate_weight_table(starting_weight):
    weight = starting_weight
    print("\nExpected weight table for the next 6 months:")
    print("Month\tExpected Weight")
    for month in range(1, 7):
        weight -= 4  # Assuming 4 pounds weight loss per month
        print(f"{month}\t{weight} pounds")
# The option table if-elif statement
def main():
    while True:
        print("\nMenu:")
        print("1. Display '10 ways to cut 500 calories' guideline.")
        print("2. Generate next semester expected weight table.")
        print("3. Quit.")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            cut_calories_guidelines()
        elif choice == '2':
            try:
                starting_weight = float(input("Enter your starting weight (in pounds): "))
                if starting_weight < 100:
                    print("Error: Weight must be 100 pounds or more.")
                else:
                    generate_weight_table(starting_weight)
            except ValueError:
                print("Error: Please enter a valid weight.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()