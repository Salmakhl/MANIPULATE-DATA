from abc import ABCMeta , abstractmethod
import copy

class produit(metaclass = ABCMeta):
    def __init__(self, name , code):
        self.__name = name
        self.__code = code

    #getters
    @property
    def getname(self):
        return self.__name
    @property
    def getcode(self):
        return self.__code
    
    #setters
    def setname(self,name):
        self.__name = name

    def setcode(self,code):
        self.__code = code

    #method
    @abstractmethod
    def getPrixht():
        pass

    def __str__(self):
        return (f"the name :{self.__name}\n the code: {self.__code}")

    def __eq__(self,other):
        return self.__code == other.__code




    
