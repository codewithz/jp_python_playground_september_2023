class Product:
    def __init__(self,name,price):
        self.name=name
        self.set_price(price)

    def set_price(self,value):
        print("Set Price is called")
        if(value<=0):
            raise ValueError("Price cannot be 0 or less")
        else:
            self.__price=value

    def get_price(self):
        print("Getter is called")
        return self.__price

    def __str__(self):
        return f"Product Name: {self.name} || Product Price: {self.__price}"

    price=property(get_price,set_price)

# -----------------------------------------------
try:

    pr1=Product("Earphones",300)
    # print(pr1)
    #
    # pr1.__price=-400
    # print(pr1)
    print(40*"-")
    pr1.price=-200
    print(pr1.price)
except Exception as ex:
    print(ex)

    # pr2=Product("Keyboard",700)
    # print(pr2)