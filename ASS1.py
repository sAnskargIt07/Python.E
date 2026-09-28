
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("\nBasic Calculations")
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    if b != 0:
        print("Division =", a / b)
    else:
        print("Division not possible (cannot divide by zero)")

    choice = input("\nDo you want hard calculations? (yes/no): ")

    if choice.lower() == "yes":
        print("\nHard Calculations")
        print("Exponentiation =", a ** b)
        print("Modulus =", a % b)

except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot perform modulus with zero.")