from os import system
def main() ->None:
    system('cls')
    try:
        n:int = int(input("Enter value(1 to 20):"))
        if n>0 and n<=20:
            for i in range(1,n+1):
               print(i,end="")
        else:
                print('accept only 1 to 20')
    except:
                print("Input Error")
                
if __name__ == "__main__":
    main()
