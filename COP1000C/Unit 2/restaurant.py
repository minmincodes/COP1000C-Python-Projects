#
# Minh D Le
#
# Calculates the cost of a restaurant meal with food and drinks included, the taxes and tipping percentage.
#


print("Restaurant Bill Calculator")

def calculate_bill(food_cost, drinks_cost):
    # Calculate total meal cost (food cost + drinks cost)
    total_cost = food_cost + drinks_cost

    # Calculate tax (7.5% of total meal cost)
    tax_rate = 0.075
    tax_amount = total_cost * tax_rate

    # Calculate total (total meal cost + tax)
    total = total_cost + tax_amount

    # Calculate tip (18% of subtotal)
    tip_rate = 0.18
    tip_amount = total * tip_rate

    # Calculate total with tips (total + tip)
    totalWithTip = total + tip_amount

    # Print the bill details
    print("Food Cost: ${:.2f}".format(food_cost))
    print("Drinks Cost: ${:.2f}".format(drinks_cost))
    print("Total Meal Cost: ${:.2f}".format(total_cost))
    print("Tax (7.5%): ${:.2f}".format(tax_amount))
    print("Total: ${:.2f}".format(total))
    print("Tip (18%): ${:.2f}".format(tip_amount))
    print("Total + Tips: ${:.2f}".format(totalWithTip))

# Get user input for food and drinks cost separately
try:
    food_cost = float(input("Enter the cost of food: $"))
    drinks_cost = float(input("Enter the cost of drinks: $"))
    calculate_bill(food_cost, drinks_cost)
except ValueError:
    print("Invalid input. Please enter valid numbers.")