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

#create the modules(function) for the math operation

def addition(a:int,b:int)->int:         return a+b
def subtraction(a:int,b:int)->int:      return a-b
def multiplication(a:int,b:int)->int:   return a*b
def division(a:int,b:int)->int:         return a/b
#
def displaymenu()->None:
    system("cls")
    menuitems:list = [
        "----- MAIN MENU -----",
        "1. MULTIPLICATION",
        "2. DIVISION",
        "3. ADDITION",
        "4. SUBTRACTION",
        "0. QUIT/EXIT",
        "---------------------",
    ];
    for menu in menuitems:
        print(menu)
        
def header(opname:str)->None:
    system("cls")
    print(opname.center(20,"-"))
    print("-"*20)

def dataentry():
    a:int = int(input("First value(1..20):"))
    b:int = int(input("Second value(1..20):"))
    #validate the input
    if a>0 and a<=20 and b>0 and b<=20:
        return a,b
    else:
        return 0,0
    
        
def main()->None:
    option:int = -1
    a:int = -1
    b:int = -1
    
    while option!=0:
        displaymenu()
        try:
            option = int(input("Enter Option(0..4):"))
            #
            if option == 1: 
                header("MULTIPLICATION")
                a,b = dataentry()
                print(f"The product of {a} x {b} is {multiplication(a,b)}")
                
            elif option == 2:
                header("DIVISION")
                a,b = dataentry()
                print(f"The quotient of {a} / {b} is {division(a,b):.4f}")
                
            elif option == 3:
                header("ADDITION")
                a,b = dataentry()
                print(f"The sum of {a} + {b} is {addition(a,b)}")
            elif option == 4:
                header("SUBTRACTION")
                a,b = dataentry()
                print(f"The difference of {a} - {b} is {subtraction(a,b)}")
            elif option == 0: print("Program Ended...")
            
            
        except:
            print("Invalid Input")
                
        input("Press any key to continue...")

if __name__=="__main__":
    main()