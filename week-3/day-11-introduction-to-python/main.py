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

# ── Extra Exercise: Arithmetic Operations ─────────────────────────────────────
# Ask the user to enter two numbers, convert them to numeric values,
# and display the sum, difference, product, quotient, and remainder.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
print(f"Sum: {sum_result}")

difference_result = num1 - num2
print(f"Difference: {difference_result}")

product_result = num1 * num2
print(f"Product: {product_result}")

quotient_result = num1 / num2
print(f"Quotient: {quotient_result}")

remainder_result = num1 % num2
print(f"Remainder: {remainder_result}")

# ── Robot Sensor Monitor ─────────────────────────────────────────────────────
# Simulate sensor data collection from a robot and print a formatted status report.

robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

safety_difference = operating_limit - sensor_reading

print("\n=== Robot Sensor Monitor Report ===")
print(f"Robot Name: {robot_name}")
print(f"Robot ID: {robot_id}")
print(f"Sensor Name: {sensor_name}")
print(f"Sensor Reading: {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Difference (Operating Limit - Sensor Reading): {safety_difference}")

