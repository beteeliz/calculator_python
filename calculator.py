def add(number1, number2):
    result = number1 + number2
    print(str(number1) + " + " + str(number2) + " = " + str(result))

def subtract(number1, number2):
    result = number1 - number2
    print(str(number1) + " - " + str(number2) + " = " + str(result))

def multiply(number1, number2):
    result = number1 * number2
    print(str(number1) + " * " + str(number2) + " = " + str(result))

def divide(number1, number2):
    if number2 == 0:
        print("\nThere is no division by zero. \n")
    else:
        result = number1 / number2
        print(str(number1) + " / " + str(number2) + " = " + str(result))

while True:
    print("\nChoose one of the operations below:")
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit \n")

    choice = input("\nType your choice: \n")

    if choice == "a" or choice == "A":
        print("Addition")
        number1 = int(input("\nType a number: "))
        number2 = int(input("Type a second number: "))
        add(number1, number2)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        number1 = int(input("\nType a number: "))
        number2 = int(input("Type a second number: "))
        subtract(number1, number2)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        number1 = int(input("\nType a number: "))
        number2 = int(input("Type a second number: "))
        multiply(number1, number2)

    elif choice == "d" or choice == "D":
        print("Division")
        number1 = int(input("\nType a number: "))
        number2 = int(input("Type a second number: "))
        divide(number1, number2)

    elif choice == "e" or choice == "E":
        print("Your calculator ended. \n")
        quit()