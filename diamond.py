from os import system

def main() -> None:
    system("cls")  # Clear the console
    try:
        n: int = int(input("Enter an ODD value (1..21): "))
        
        # Validation for odd number between 1 and 21
        if n > 0 and n <= 21 and n % 2 > 0:
            max_width = n * 2  # Maximum width for centering, each X has a space after it
            
            # Upper pyramid (increasing part of the diamond)
            for i in range(1, n+1, 2):  # Start from 1, increase by 2 until n
                spaces = (max_width - (i * 2)) // 2  # Calculate spaces for centering
                print(" " * spaces, end="")  # Print leading spaces
                print("X " * i)  # Print 'X's with a space between each
            
            # Lower pyramid (decreasing part of the diamond)
            for i in range(n-2, 0, -2):  # Start from n-2, decrease by 2 until 1
                spaces = (max_width - (i * 2)) // 2  # Calculate spaces for centering
                print(" " * spaces, end="")  # Print leading spaces
                print("X " * i)  # Print 'X's with a space between each
                
        else:
            print("Accept only ODD values from 1 to 21.")
    
    except ValueError:
        print("Invalid Input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
