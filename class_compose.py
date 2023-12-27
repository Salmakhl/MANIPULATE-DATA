from class_produit import*
from class_composition import*

class compose(produit):
    
    def __init__(self, name, code,frais  , listeconti, tva = 0.18):
        super().__init__(name, code)
        self.__frais = frais
        self.tva = tva
        self.__listeconti = listeconti

    #getters
    @property
    def getfrais(self):
        return self.__frais
    

    
    @property
    def getlisleconti(self):
        return self.__listeconti
    
    #setters
    def setfrais(self,frais):
        self.__frais = frais



    def setlisteconti(self,listeconti):
        self.__listeconti = listeconti

    def __str__(self):
        constituant = "\n".join(f"{x}" for x in self.getlisleconti)
        return (f"the name :{self.getname}\n the code: {self.getcode} \n the tva: {self.tva} \n constituants : {constituant}\
                \n frais: {self.getfrais} \n price : {self.getPrixht()} ")
    

    def __eq__(self,other):
        return self.__code == other.__code
    
    #method
    def getPrixht(self):
        total = sum(x.getproduct.getPrixht for x in self.__listeconti)
        total += self.getfrais 
        return total
        
        
