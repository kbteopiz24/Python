'''
Name: Kristian Baron Teopiz BSIT-3

A program that would accept 5 positive integers not greater than 20, display all inputted values compute and display the sum and average.
Condition:
must have five(5) inputs otherwise no display and compute. 
'''
from os import system

def main() -> None:
    system('cls')

    numbers = {}

    # Accept 5 positive integers from the user
    for i in range(1, 6):
        while True:
            try:
                # Prompt the user for input
                num = int(input(f"Enter positive integer #{i} (not greater than 20): "))
                
                match num:
                    case num if 1 <= num <= 20:
                        numbers[f'num{i}'] = num  
                        break  
                    case _:
                        print("Please enter a positive integer not greater than 20.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Display the input values
    print("\nYou have entered the following values:")
    for key, value in numbers.items():
        print(f"{key}: {value}")
    
    # Calculate the sum and average
    total = sum(numbers.values())
    average = total / len(numbers)
    
    # Display the sum and average
    print(f"\nSum: {total}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()
