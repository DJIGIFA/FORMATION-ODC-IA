import random

#fonction : Creation de D avec des valeurs aleatoires
def getD(n,s):
    ma_liste = [] 
    
    for i in range(0,n) :
        
        liste_temp = [] 
        for i in range(0,s) :
            a = random.randint(0,100) 
            liste_temp.append(a)
        
        ma_liste.append(liste_temp)
    return ma_liste

#fonction : min et max local de toutes les listes contenus dans D
def getMinMax(liste) :  # liste = D
    
    ma_liste = []
    
    for element in  liste :
        m = min(element)
        M = max(element)
        ma_liste.append([m,M])  
        
    return ma_liste
# min global
def minGlobal(liste) :  #liste = la  liste contenant les min et les max 
    
    l = min (liste)
    return l[0]
# max globale
def maxGlobal(liste) : #liste = Soit D ou bien la liste contenant les min et les max
    
    Max = [max(l) for l in liste]
    
    return max(Max)
    
    
F = lambda x : x**3 + 3*x**2 -5
def dPrime(D) :
    return [ [F(x) for x in liste] for liste in D ]


# D = getD(3,5) 
# print(D)
# print(dPrime(D))

class DataTrans :
    
    def __init__(self,n,s) -> None:
        self.s = s
        self.n = n
        self.F = lambda x : x**3 + 3*x**2 -5
        
        self.D = [] 
        
        for i in range(0,self.n) :
            
            liste_temp = [] 
            for i in range(0,self.s) :
                a = random.randint(0,100) 
                liste_temp.append(a)
            
            self.D.append(liste_temp)
        

    def getD(self):
        return self.D
    
    def getMinMax(self) :
        ma_liste = []
        
        for element in  self.getD() :
            m = min(element)
            M = max(element)
            ma_liste.append([m,M])  
            
        return ma_liste
    

    def minGlobal(self) :
        
        l = min (self.getMinMax())
        return l[0]
    
    def maxGlobal(self) :
    
        Max = [max(l) for l in self.getMinMax()]
        return max(Max)

    def dPrime(self) :
        return [ [self.F(x) for x in liste] for liste in self.getD() ]






#pour le test
if __name__ == "__main__":
    D = DataTrans(3,5)
    print(D.getD())
    print(D.getMinMax())
    print(D.maxGlobal())
    print(D.minGlobal())
    print(D.dPrime())