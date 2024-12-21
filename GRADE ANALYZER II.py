# Ask for the person's name
person_name = input("Enter the name of the person we are calculating the grades for: ")

# Ask for each test score one by one
test1 = int(input("Enter Test 1 score: "))
test2 = int(input("Enter Test 2 score: "))
test3 = int(input("Enter Test 3 score: "))
test4 = int(input("Enter Test 4 score: "))

# Check if any score is below 0, and exit if so
if test1 < 0 or test2 < 0 or test3 < 0 or test4 < 0:
    print("Test scores must be greater than 0")
    exit()

# Ask if the user wants to drop the lowest score
drop_lowest = input("Do you want to drop the lowest score? (Y/N): ").strip().upper()

# Make sure the answer is Y or N
if drop_lowest != 'Y' and drop_lowest != 'N':
    print("Please enter Y or N.")
    exit()

# Calculate the average based on the user's choice
if drop_lowest == 'Y':
    # Find the lowest score using if statements
    if test1 <= test2 and test1 <= test3 and test1 <= test4:
        lowest_score = test1
    elif test2 <= test1 and test2 <= test3 and test2 <= test4:
        lowest_score = test2
    elif test3 <= test1 and test3 <= test2 and test3 <= test4:
        lowest_score = test3
    else:
        lowest_score = test4

    # Subtract the lowest score and calculate the average of the remaining 3
    total = test1 + test2 + test3 + test4 - lowest_score
    average = total / 3
else:
    # Calculate the average of all 4 scores
    total = test1 + test2 + test3 + test4
    average = total / 4

# Round average to one decimal place
average = float(f"{average:.1f}")

# Decide the letter grade
if average >= 97.0:
    letter_grade = 'A+'
elif average >= 94.0:
    letter_grade = 'A'
elif average >= 90.0:
    letter_grade = 'A-'
elif average >= 87.0:
    letter_grade = 'B+'
elif average >= 84.0:
    letter_grade = 'B'
elif average >= 80.0:
    letter_grade = 'B-'
elif average >= 77.0:
    letter_grade = 'C+'
elif average >= 74.0:
    letter_grade = 'C'
elif average >= 70.0:
    letter_grade = 'C-'
elif average >= 67.0:
    letter_grade = 'D+'
elif average >= 64.0:
    letter_grade = 'D'
elif average >= 60.0:
    letter_grade = 'D-'
else:
    letter_grade = 'F'

# Print the results
print(person_name + "'s test average is: " + str(average))
print("Letter Grade for the test is: " + letter_grade)
