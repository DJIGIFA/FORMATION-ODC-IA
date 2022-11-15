import math

#maniere procedurale
#f(x)
f = lambda x  : x / (x **2 + 1)

#g(x)
g = lambda x : math.atan(x)

#On pose h(x) = (f(x) - g(x))^2
h = lambda x : (f(x) - g(x)) **2

#L [-N : N] pour generer les valeur 
L = lambda N : [n for n in range(-N,N+1)]


#R(x) = somme(h(x)) pour x element L

R = lambda N : sum([h(x) for x in L(N)])

# print(L(2))
# print(R(2))

#avec POO

class R_class :
    
    def __f(self,x):
        return x / (x**2 + 1)
    
    def __g(self,x) :
        return math.atan(x)
    
    def __h(self,x) :
        return (self.__f(x) - self.__g(x)) **2
    
    def _L(self,N) :
        return [n for n in range(-N, N+1)] 
    
    def _getValeur(self,N) :
        return sum([self.__h(x) for x in self._L(N)])




#pour le test
if __name__ == "__main__":
    r = R_class()
    print(r._L(6))
    print(r._getValeur(6))





