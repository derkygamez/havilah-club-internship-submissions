# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

f_name = "cunha"
print(type(f_name))

age = 25
print(type(age))

height = 5.9
print(type(height))

is_student = True
print(type(is_student))



# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Temperature in Celsius: {celsius}")


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2023
age = current_year - birth_year
year_turn_30 = birth_year + 30

print("Hello, " + name + "!")
print("You are currently " + str(age) + " years old.")
print("You will turn 30 in the year " + str(year_turn_30) + ".")
