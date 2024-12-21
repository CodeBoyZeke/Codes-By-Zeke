# Constants for gravitational force on different celestial bodies
GRAVITY_MERCURY = 0.38
GRAVITY_VENUS = 0.91
GRAVITY_MOON = 0.165
GRAVITY_MARS = 0.38
GRAVITY_JUPITER = 2.34
GRAVITY_SATURN = 0.93
GRAVITY_URANUS = 0.92
GRAVITY_NEPTUNE = 1.12
GRAVITY_PLUTO = 0.066

def main():
    # Get user input
    s_name = input("Enter your name: ")
    n_earth_weight = float(input("Enter your Earth weight (pounds): "))

    # Calculate weight on different celestial bodies
    n_mercury_weight = n_earth_weight * GRAVITY_MERCURY
    n_venus_weight = n_earth_weight * GRAVITY_VENUS
    n_moon_weight = n_earth_weight * GRAVITY_MOON
    n_mars_weight = n_earth_weight * GRAVITY_MARS
    n_jupiter_weight = n_earth_weight * GRAVITY_JUPITER
    n_saturn_weight = n_earth_weight * GRAVITY_SATURN
    n_uranus_weight = n_earth_weight * GRAVITY_URANUS
    n_neptune_weight = n_earth_weight * GRAVITY_NEPTUNE
    n_pluto_weight = n_earth_weight * GRAVITY_PLUTO

    # Print the results
    print(f"\nSolar System's Weight Conversion for {s_name}")
    print(f"{'Planet':<10}{'Weight (lbs)':>10}")
    print(f"{'Mercury':<10}{n_mercury_weight:10.2f}")
    print(f"{'Venus':<10}{n_venus_weight:10.2f}")
    print(f"{'Moon':<10}{n_moon_weight:10.2f}")
    print(f"{'Mars':<10}{n_mars_weight:10.2f}")
    print(f"{'Jupiter':<10}{n_jupiter_weight:10.2f}")
    print(f"{'Saturn':<10}{n_saturn_weight:10.2f}")
    print(f"{'Uranus':<10}{n_uranus_weight:10.2f}")
    print(f"{'Neptune':<10}{n_neptune_weight:10.2f}")
    print(f"{'Pluto':<10}{n_pluto_weight:10.2f}")

# Call main function if the script is executed directly
if __name__ == "__main__":
    main()
