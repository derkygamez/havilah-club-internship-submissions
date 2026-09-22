# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(grade=None):
    if grade is None:
        while True:
            try:
                grade = int(input("What's your score? (0-100): "))
                break
            except ValueError:
                print("Invalid input. Please enter a whole number from 0 to 100.")

    if grade < 0 or grade > 100:
        print("This is not a valid score. Please enter a score between 0 and 100.")
        return

    if grade >= 70:
        print("A")
    elif grade >= 60:
        print("B")
    elif grade >= 50:
        print("C")
    elif grade >= 40:
        print("D")
    else:
        print("F")

# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    while True:
        user_input = input("Enter a number to see its multiplication table (or 'quit' to exit): ").strip().lower()

        if user_input == 'quit':
            print("Exiting multiplication table.")
            break

        try:
            number = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")
            continue

        print(f"\nMultiplication table for {number}:")
        for i in range(1, 13):
            print(str(number) + " x " + str(i) + " = " + str(number * i))

# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().
def calculate_volume(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def your_function():
    while True:
        user_input = input("Enter the radius of a sphere to calculate its volume (or 'quit' to exit): ").strip().lower()

        if user_input == 'quit':
            print("Exiting sphere volume calculator.")
            break

        try:
            radius = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")
            continue

        if radius < 0:
            print("Radius cannot be negative.")
            continue

        volume = calculate_volume(radius)
        print(f"The volume of the sphere is: {volume:.2f} cubic units.")

# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Sphere Volume Calculator")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            calculate_grade()
        elif choice == 2:
            multiplication_table()
        elif choice == 3:
            your_function()
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
