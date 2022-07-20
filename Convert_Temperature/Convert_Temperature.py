import temperature as temp
def display():
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

def convert():
    opt=input("Enter a menu option: \n")
    if opt.isnumeric():
        opt=int(opt) 
        if opt==1:
            Fah=int(input("Enter degrees Fahrenheit: \n"))
            Celsius=temp.to_celsius(Fah)
            print(f" Degree Celsius: {round(Celsius,2)}")
        elif opt==2:
            Cel=int(input("Enter degree Celsius: \n"))
            Fahrenheit=temp.to_fahrenheit(Cel)
            print(f"Degree Fahrenheit: {round(Fahrenheit,2)}")
        else:
            print("Please enter number between 1 and 2")
            return convert()
    else:
        print("Please enter number between 1 and 2")
        return convert()
def main():
    display()
    cont= "y"
    while cont.lower() == "y":
        convert()
        cont=input("Convert another temperature? (y/n) \n")
    print ("bye")
if __name__=="__main__":
    main()