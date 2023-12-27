import copy
class composition():
    
    def __init__(self, product , quantity ):
        self.__product = copy.copy(product)
        self.__quantity = quantity

    #getters
    @property
    def getproduct(self):
        return self.__product
     
    @property
    
    def getquantity(self):
        return self.__quantity
    
    #setters
    def setproduct(self,product):
        self.__product = product

    def setquantity(self,quantity):
        self.__quantity = quantity
    
    def __str__(self):
        return (f"the product :{str(self.getproduct)}\n the quantity: {self.getquantity}")

    def __eq__(self,other):
        return self.__product == other.__product
