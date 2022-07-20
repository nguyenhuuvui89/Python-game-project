class Products:
    def __init__(self,name,price,discount_percent):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent
    def discount_amount(self):
        return self.price*self.discount_percent/100
    def discount_price(self):
        return self.price - self.discount_amount()
product1=Products("Stanley 13 Ounce Wood Hammer", 12.99, 62)
product2=Products('National Hardware 3/4" Wire Nails', 5.06, 0)
product3=Products("Economy Duct Tape, 60 yds, Silver", 7.24, 0)
products=(product1,product2,product3)
def introduction(products):
    print("The Product Viewer program \n\nPRODUCTS")
    for i in range(len(products)):
        print (f"{i+1}. {products[i].name}")
    print()
def product_data(products):
    product_number = input("Enter product number: ")
    print("\nPRODUCT DATA")
    if not product_number.isnumeric() or not 1<=int(product_number) <= len(products):
        print(f"Please input valid number between 1 and {len(products)}")
        return product_data()
    else:
        product_number = int(product_number)
        for i in range(len(products)):
            if (product_number - 1) == i:
                print(f"Name:   {products[i].name}")
                print(f"Price:  {products[i].price}")
                print(f"Discount percent:   {products[i].discount_percent}%")
                print(f"Discount amount:    {products[i].discount_amount():.2f}")
                print(f"Discount price: {products[i].discount_price():.2f}")

def main():
    introduction(products)
    again = True
    while again:
        product_data(products)
        print()
        view_again = input("View another product? (y/n) \n")
        if view_again.lower() != 'y':
            again = False

if __name__ == "__main__":
    main()