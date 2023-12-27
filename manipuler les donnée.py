from class_produit import*
from class_elementaire import*
from class_composition import* 
from class_compose import*
from collections import namedtuple
from collections import defaultdict


tomato = elementaie("tomato","poo1",10)
egg = elementaie("egg","poo2",1.5)

c1 = composition("tomato",2)
c2 = composition("egg",5)

listeconti = [c1, c2]
bm = compose("bm","poo3", 5, listeconti)
 
listproduit = [tomato,egg,bm]

def info():
    for x in listproduit :
        if type(x) == elementaie :
            print(f"l'element :{x.getname} \n le prix: {x.getPrixht}")
        else:
            for y in x.getlisleconti:
                print(f"{x.getname} composé de {y.getproduct}")

description = namedtuple('description',[ 'produit','detail'])
desliste = defaultdict()
for x in listproduit:
      if type(x) == elementaie:
         pr1 = description(produit= f"{x.getname}", detail="description")
         print(pr1)
         des = pr1._asdict()
         desliste.update({ pr1.produit : pr1.detail} )
         
      else:
          for y in x.getlisleconti:
              print(f"{x.getname} compose de ", y.getproduct  )
              pr1 = description(produit=f"{x.getname}",detail=f"compose de {y.getproduct} ")
              des = pr1._asdict()
              desliste.update({pr1.produit : pr1.detail})




print(desliste)
info()

