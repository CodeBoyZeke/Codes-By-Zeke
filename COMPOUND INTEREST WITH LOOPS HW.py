# Compound Interest Calculator with Loops

# Get input from the user and validate it
def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:  # Ensure the value is positive or zero
                return value
            else:
                print("Please enter a positive number (or zero for the goal).")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get user inputs
deposit = get_positive_input("Enter the initial deposit amount (positive value): ")
interest_rate = get_positive_input("Enter the annual interest rate (percentage, e.g., 5 for 5%): ")
months = get_positive_input("Enter the number of months to calculate (positive value): ")
goal = get_positive_input("Enter the goal amount (can be zero if no goal): ")

# Convert annual interest rate to a monthly rate
monthly_interest_rate = interest_rate / 12 / 100

# Display the account balance for each month
print("\nCalculating monthly balances...\n")
current_balance = deposit
for month in range(1, int(months) + 1):
    interest = current_balance * monthly_interest_rate
    current_balance += interest
    print(f"Month {month}: Account Balance is ${current_balance:,.2f}")

# Calculate how long it will take to reach the goal (if a goal is given)
if goal > 0:
    print("\nCalculating how long it will take to reach your goal...\n")
    current_balance = deposit
    months_to_goal = 0
    while current_balance < goal:
        interest = current_balance * monthly_interest_rate
        current_balance += interest
        months_to_goal += 1
    print(f"It will take {months_to_goal} months to reach the goal of ${goal:,.2f}.")
else:
    print("\nNo goal was entered, so only the monthly balances were calculated.")
