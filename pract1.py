from os import system
def main() ->None:
    system('cls')
    try:
        n:int = int(input("Enter value(1 to 20):"))
        if n>0 and n<=20:
            i:int = 1
            while i<=n:
                print (i)
                i=i+1
        else:
                print('accept only 1 to 20')
    except:
                print("Input Error")
                
if __name__ == "__main__":
    main()