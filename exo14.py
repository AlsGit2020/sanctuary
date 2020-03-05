print ("Ce programme affiche tous les nombres inférieurs à 500 égaux à la somme des cubes de leurs chiffres")

def cube (n) :
    return n*n*n

def unite(nombre):
    cub=0
    for element in nombre :
        chiffre = int(element)
        cub +=cube(chiffre)
    return cub

LesNombre=""

for i in range (501):
    if unite(str(i))==i:
        LesNombre+=str(i)+" "
print(LesNombre)
