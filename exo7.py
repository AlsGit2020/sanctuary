
def saisi_dictionnaire(n) :
    dictionnaire1 = dict()
    for i in range (n):
        cle= input(" Entrez un le nom du produit:  ")
        valeur= input("Entrez un le prix  du produit: ")
        dictionnaire1[cle]=valeur
    return dictionnaire1

dictionnaire1 = dict()
def affichage(dictionnaire):
    for element in dictionnaire:
        print (element, dictionnaire[element])


print ("Ce programme permet à l’utilisateur d’entrer N nom de produits et leur prix")
print ("qui seront stocké dans un tableau associatif") 
N=int(input("Nombre d'articles a saisir  N = "))
ListeProduit = dict()
ListeProduit = saisi_dictionnaire(N)
affichage (ListeProduit)
