from os import system

def main() -> None:
    system('cls')  # Clears the console screen
    try: 
        n = int(input("Enter an odd number between 1 and 20: "))
        
        if n > 0 and n <= 20 and n % 2 == 1:
            for i in range(1, n + 1, 2):  # Loop through odd numbers up to 'n'
                print(" " * ((n - i) // 2) + "x" * i)  # Print the row with spaces and 'x's
        else:
            print("Please enter an odd number between 1 and 20.")
    except ValueError:  # Catch invalid input when the user enters a non-integer
        print("Invalid input. Please enter a valid integer.")
        
if __name__ == "__main__":
    main()

