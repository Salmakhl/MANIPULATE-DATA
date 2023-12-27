from class_produit import*

class elementaie(produit):
    def __init__(self,  name,code ,price):
        super().__init__(name , code)
        self.__price = price

    #getter
    @property
    def getPrixht(self):
        return self.__price
    
    #setter
    def setprice(self,price):
        self.__price = price



    def __str__(self):
        return (f"{self.getname}; the code: {self.getcode} ; the price: {self.getPrixht}")

