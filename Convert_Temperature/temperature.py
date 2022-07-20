def to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
def to_fahrenheit(celsius):
    fahrenheit= celsius*5/9 + 32
    return fahrenheit
def main():
    for temp in range(0,212,40):
        print(temp," Fahrenheit = ", round(to_celsius(temp)), "Celsius")
    for temp in range(0,100,20):
        print(temp, "Celsius  =", round(to_fahrenheit(temp)), "Fahrenheit")
if __name__=="__main__":
    main()