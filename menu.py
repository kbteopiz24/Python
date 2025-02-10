'''
    A program that would accept two positive
    integer values from 1 to 20. Create a module(function) for each mathematical operation that would provide the necessary computation.
    Create a menu for this program
    
    ----- Main Menu -----
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    0. Quit/End
    ---------------------
    Enter Option(0..4)
'''

from os import system  

def addition(a: int, b: int) -> int:
    return a + b

def subtraction(a: int, b: int) -> int:
    return a - b

def multiplication(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> float:
    return a / b if b != 0 else float('inf')  

def displaymenu() -> None:
    system("cls")  
    menuitems = [
        "----- MAIN MENU -----",
        "1. ADDITION",
        "2. SUBTRACTION",
        "3. MULTIPLICATION",
        "4. DIVISION",
        "0. QUIT/EXIT",
        "---------------------"
    ]
    for item in menuitems:
        print(item)

def header(operationname: str) -> None:
    system("cls")  
    print(operationname.center(20, "-"))
    print("-" * 20)

def dataentry() -> tuple[int, int]:
    try:
        a = int(input("First value (1-20): "))
        b = int(input("Second value (1-20): "))

        # Validate input
        if 1 <= a <= 20 and 1 <= b <= 20:
            return a, b
        else:
            print("Invalid input! Numbers must be between 1 and 20.")
            return 0, 0
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return 0, 0

def main() -> None:
    option = -1  

    while option != 0:
        displaymenu()
        try:
            option = int(input("Enter Option (0-4): "))

            if option == 1:
                header("ADDITION")
                a, b = dataentry()
                print(f"The sum of {a} + {b} = {addition(a, b)}")

            elif option == 2:
                header("SUBTRACTION")
                a, b = dataentry()
                print(f"The difference of {a} - {b} = {subtraction(a, b)}")

            elif option == 3:
                header("MULTIPLICATION")
                a, b = dataentry()
                print(f"The product of {a} * {b} = {multiplication(a, b)}")

            elif option == 4:
                header("DIVISION")
                a, b = dataentry()
                if b != 0:
                    print(f"The quotient of {a} ÷ {b} = {division(a, b):.4f}")
                else:
                    print("Error! Division by zero is not allowed.")

            elif option == 0:
                print("Program Ended...")
            else:
                print("Invalid Option! Please enter a number between 0 and 4.")

        except ValueError:
            print("Invalid Input! Please enter numbers only.")

        input("Press Enter to continue...")  

if __name__ == "__main__":
    main()
