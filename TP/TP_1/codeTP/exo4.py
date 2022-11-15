#Exercice 4
import random
from math import sqrt

taille_liste = 100 
ma_liste = [] 
    
for i in range(0,taille_liste) :
    a = random.random() * 100
    b = round(a,1)
    ma_liste.append(b)

#calcule de la moyenne
ma_liste.sort()

moyenne = sum(ma_liste) / taille_liste
mediane = (ma_liste[49] + ma_liste[50]) / 2
#print(mediane)
#print(moyenne)


temp_somme = 0
for element in ma_liste :
    
    temp_somme = temp_somme + (element - moyenne) ** 2

variance = temp_somme / taille_liste
#print(variance)

ecartType = sqrt(variance)
#print(ecartType)

print(ma_liste)
print(f"Moyenne = {moyenne}")
print(f"Mediane = {mediane}")
print(f"Variance = {variance}")
print(f"ecart type = {ecartType}")


    
    