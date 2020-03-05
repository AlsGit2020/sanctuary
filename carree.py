#exercice 1
def carree(nombre) : return nombre*nombre

#exercice 2
def fonctionduplusgrand(a,b) :
    if a < b :
        return carree(b)
    else :
        return carree(a)

#exercice 3
print (" cet exercice permet de teste uniquement la foncion carree en faisant appel aux fonctions predefines  ")
nombre1 = int(input("Entrer la valeur du nombre 1  "))
nombre2 = int(input("Entrer la valeur du nombre 2  "))
resultat = fonctionduplusgrand (nombre1,nombre2)
print ("Le carree du plus grand nombre est egal a  ", resultat)