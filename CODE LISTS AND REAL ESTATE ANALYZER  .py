# Function to get a valid float input
def getFloatInput(prompt):
    while True:  # Keep asking until the input is valid
        try:
            value = float(input(prompt))  # Try to convert input to a float
            if value > 0:  # Check if the number is positive
                return value
            else:
                print("Please enter a number greater than 0.")  # Error message
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Error message

# Function to calculate the median
def getMedian(numbers):
    numbers.sort()  # Sort the list in ascending order
    count = len(numbers)  # Find the number of elements in the list
    if count % 2 == 1:  # If the count is odd
        return numbers[count // 2]  # Middle element
    else:  # If the count is even
        middle1 = numbers[count // 2]  # First middle element
        middle2 = numbers[count // 2 - 1]  # Second middle element
        return (middle1 + middle2) / 2  # Average of the two middle elements

# Main function to handle the program logic
def main():
    sales = []  # List to store sales values

    while True:  # Loop until the user decides to stop
        sales_value = getFloatInput("Enter property sales value: ")  # Get sales input
        sales.append(sales_value)  # Add the value to the list
        
        # Ask the user if they want to continue
        user_input = input("Enter another value Y or N: ").strip().lower()
        if user_input == 'n':  # If the user enters 'N', stop the loop
            break
        elif user_input != 'y':  # If the input is not 'Y', show an error
            print("Invalid input. Please enter Y or N.")

    # Sort the list in ascending order
    sales.sort()

    # Print the sorted sales values
    print("\nSales List:")
    for i in range(len(sales)):
        print(f"Property {i + 1}: $ {sales[i]:,.2f}")

    # Calculate statistics
    minimum = sales[0]  # Smallest value
    maximum = sales[-1]  # Largest value
    total = sum(sales)  # Sum of all values
    average = total / len(sales)  # Average value
    median = getMedian(sales)  # Median value
    commission = total * 0.03  # 3% of the total

    # Print the results
    print("\nResults:")
    print(f"Minimum: $ {minimum:,.2f}")
    print(f"Maximum: $ {maximum:,.2f}")
    print(f"Total: $ {total:,.2f}")
    print(f"Average: $ {average:,.2f}")
    print(f"Median: $ {median:,.2f}")
    print(f"Commission: $ {commission:,.2f}")

# Run the program
if __name__ == "__main__":
    main()
