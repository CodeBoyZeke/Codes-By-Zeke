# Welcome message
print("Zeke's Temp Converter:")

# Prompt user for a temperature value (float allows decimals)
temp_value = float(input("Enter a temperature: "))

# Prompt user to specify Fahrenheit or Celsius
temp_type = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().lower()

# Check if the user input is valid (either 'f' or 'c')
if temp_type not in ['f', 'c']:
    print("You must enter a F or C")
else:
    if temp_type == 'f':
        # Fahrenheit to Celsius conversion
        if temp_value > 212:
            print("Temp can not be > 212")
        else:
            celsius = (5.0 / 9) * (temp_value - 32)
            print(f"The Celsius equivalent is: {celsius:.1f}")
    elif temp_type == 'c':
        # Celsius to Fahrenheit conversion
        if temp_value > 100:
            print("Temp can not be > 100")
        else:
            fahrenheit = (9.0 / 5) * temp_value + 32
            print(f"The Fahrenheit equivalent is: {fahrenheit:.1f}")
