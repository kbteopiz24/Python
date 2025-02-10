from os import system

def main() -> None:
    system("cls")  # Clear the console
    try:
        n: int = int(input("Enter an ODD value (1..21): "))
        
        # Validation for odd number between 1 and 21
        if n > 0 and n <= 21 and n % 2 > 0:
            max_width = n * 2  # Maximum width for centering, each X has a space after it
            # Loop to print each row in the inverted pyramid
            for i in range(n, 0, -2):  # Start from n, decrease by 2 until 1
                # Calculate spaces for centering
                spaces = (max_width - (i * 2)) // 2  # (i * 2) accounts for Xs and spaces after them
                # Print spaces to center the pyramid
                print(" " * spaces, end="")
                # Print the 'X's with a space between them
                print("X " * i)
                
        else:
            print("Accept only ODD values from 1 to 21.")
    
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


