'''
	A program that would accept a positive ODD integer value not greater
   than 21 and display the pyramid of 'x' with the base count that of the 
   inputted value
   
   example:
   input: 5
        x
      x x x 
    x x x x x <==5
'''
from os import system
def main()->None:
    system("cls")
    try:
        n:int = int(input("Enter an ODD value(1..21):"))
        #validation
        if n>0 and n<=21 and n%2>0:
            for i in range(1,n+1,2):
                for space in range(0,(n*2)-i):
                    print(" ",end="")
                for star in range(0,i):
                    print("X ",end="")
                print()
        else:
            print("accept only ODD values from 1 to 21")
    except ValueError: 
        print("Invalid Input")

if __name__=="__main__":
    main()