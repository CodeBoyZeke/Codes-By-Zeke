# A = Final amount in the account after t years
# P = Principal amount initially deposited
# r = Annual interest rate in decimal form
# n = Number of times the interest rate is compounded per year
# t = Number of years the money is left in account

P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): ")) / 100
n = int(input("Enter the number of times the interest is compounded per year: "))
t = int(input("Enter the number of years the account will earn interest: "))

# Calculate the final amount using the compound interest formula
A = P * (1 + r / n) ** (n * t)

# Display the result
print(f"\nThe amount in the account after {t} years will be: ${A:.2f}")
