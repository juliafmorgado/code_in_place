"""
This program asks the user for two numbers and prints their average.
"""

def main():
    print("This program averages two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2
    print("The average is", average)

if __name__ == '__main__':
    main()