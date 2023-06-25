# Create a Product class and a Shop class.
""" class product:
    pass
class shop:
    pass """

# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
class Product:
    def __init__(self,n,pz) -> None:
        self.name = n
        self.prize = pz


class shop:
    def __init__(self) -> None:
        self.products = []

    def add_product(self,n,pz):
        product = Product(n,pz)
        self.products.append(product)
    
    def buy_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Congratulatuin you here is your",name)
                return
            else :
                print("Sorry this item is not available here!!!!!!")
    def show(self):
        for product in self.products:
            print('Producr: ',product.name)
            print('Product: ',product.prize)
            print()
    

my_shop = shop()
my_shop.add_product("I-Phone",50000)
my_shop.add_product("nokia",200)
my_shop.show()
my_shop.buy_product('I-Phone')
my_shop.buy_product('I-Phone')
my_shop.buy_product('Samsung')
