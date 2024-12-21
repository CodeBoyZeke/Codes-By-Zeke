# Function to get a valid float input
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:  # Ensure value is positive and non-zero
                return value
            else:
                print("Please enter a positive number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate the number of gallons needed
def get_gallons_of_paint(square_feet, feet_per_gallon):
    gallons = square_feet / feet_per_gallon
    return int(gallons) + (1 if gallons % 1 > 0 else 0)  # Round up to the nearest whole number

# Function to calculate labor hours
def get_labor_hours(gallons, labor_hours_per_gallon):
    return gallons * labor_hours_per_gallon

# Function to calculate labor cost
def get_labor_cost(labor_hours, labor_charge_per_hour):
    return labor_hours * labor_charge_per_hour

# Function to calculate paint cost
def get_paint_cost(gallons, paint_price):
    return gallons * paint_price

# Function to calculate sales tax
def get_sales_tax(total_cost, state):
    if state == "CT":
        return total_cost * 0.06
    elif state == "MA":
        return total_cost * 0.0625
    elif state == "ME":
        return total_cost * 0.085
    elif state == "NH":
        return 0.0
    elif state == "RI":
        return total_cost * 0.07
    elif state == "VT":
        return total_cost * 0.06
    else:
        return 0.0

# Function to display the results and write to a file
def show_results(customer_name, state, square_feet, paint_price, feet_per_gallon,
                 labor_charge_per_hour, gallons, labor_hours, paint_cost, labor_cost, tax, total_cost):
    print("\n--- Paint Job Estimate ---")
    print(f"Customer Name: {customer_name}")
    print(f"State job is in: {state}")
    print(f"Square Feet to Paint: {square_feet}")
    print(f"Paint Price per Gallon: ${paint_price:.2f}")
    print(f"Feet per Gallon: {feet_per_gallon}")
    print(f"Labor Charge per Hour: ${labor_charge_per_hour:.2f}")
    print(f"Gallons of paint: {gallons}")
    print(f"Labor hours: {labor_hours:.2f}")
    print(f"Paint charges: ${paint_cost:.2f}")
    print(f"Labor charges: ${labor_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    
    # Save to file
    file_name = f"{customer_name}_PaintJobOutput.txt"
    with open(file_name, "w") as file:
        file.write(f"Customer Name: {customer_name}\n")
        file.write(f"State job is in: {state}\n")
        file.write(f"Square Feet to Paint: {square_feet}\n")
        file.write(f"Paint Price per Gallon: ${paint_price:.2f}\n")
        file.write(f"Feet per Gallon: {feet_per_gallon}\n")
        file.write(f"Labor Charge per Hour: ${labor_charge_per_hour:.2f}\n")
        file.write(f"Gallons of paint: {gallons}\n")
        file.write(f"Labor hours: {labor_hours:.2f}\n")
        file.write(f"Paint charges: ${paint_cost:.2f}\n")
        file.write(f"Labor charges: ${labor_cost:.2f}\n")
        file.write(f"Tax: ${tax:.2f}\n")
        file.write(f"Total cost: ${total_cost:.2f}\n")
    print(f"\nFile '{file_name}' was created.")

# Main function
def main():
    print("Welcome to the Paint Job Estimator!")

    # Get user inputs
    square_feet = get_float_input("Enter wall space in square feet: ")
    paint_price = get_float_input("Enter paint price per gallon: ")
    feet_per_gallon = get_float_input("Enter feet per gallon: ")
    labor_charge_per_hour = get_float_input("Enter labor charge per hour: ")
    labor_hours_per_gallon = get_float_input("Enter labor hours per gallon: ")

    state = input("Enter state abbreviation (e.g., MA, CT): ").strip().upper()
    customer_name = input("Enter customer's last name: ").strip()

    # Perform calculations
    gallons = get_gallons_of_paint(square_feet, feet_per_gallon)
    labor_hours = get_labor_hours(gallons, labor_hours_per_gallon)
    paint_cost = get_paint_cost(gallons, paint_price)
    labor_cost = get_labor_cost(labor_hours, labor_charge_per_hour)
    total_cost_before_tax = paint_cost + labor_cost
    tax = get_sales_tax(total_cost_before_tax, state)
    total_cost = total_cost_before_tax + tax

    # Show results
    show_results(customer_name, state, square_feet, paint_price, feet_per_gallon,
                 labor_charge_per_hour, gallons, labor_hours, paint_cost, labor_cost, tax, total_cost)

# Run the program
if __name__ == "__main__":
    main()
