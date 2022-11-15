import exo1
import exo2


while True :
    print("**********Menu principale ******************** ")
    print("Tapez 1. Exercice 1 : ")
    print("Tapez 2. Exercice 2 : ")
    print("Tapez 3. Quitter : ")
    choix = input()
    
    if(choix == "1"):
        print("****************Exercice 1************************")
        N = input("Donnez la valeur de N : ")
        
        try:
            N = int(N)
            while True:
                print("Tapez 1. affiche L : ")
                print("Tapez 2. calculer R : ")
                print("Tapez 3. retour au menu principal : ")
                choix_2 = input()
                if(choix_2 == "1") :
                    print(exo1.L(N))
                elif(choix_2 == "2") :
                    print(exo1.R(N))
                elif (choix_2 == "3"):
                    break
                else :
                    print("choix invalide")
                    
                
        except :
            print("Donnée invalide")
        
    elif (choix == "2") :
        print("****************Exercice 2************************")
        print("Donnez la valeur de n : ")
        n = input()
        print("Donnez la valeur S : ")
        s = input()
        
        try:
            n = int(n)
            s = int(s)
            dataTrans = exo2.DataTrans(n,s)
            while True:
                print("Tapez 1. afficher la liste D : ")
                print("Tapez 2. afficher Les min et les max :")
                print("Tapez 3. afficher le min global : ")
                print("Tapez 4. afficher le max global : ")
                print("Tapez 5. Calculer D' : ")
                print("Tapez 6. retour au menu principal : ")
                
                choix_3 = input()
                
                if(choix_3 == "1"):
                    print(dataTrans.getD())
                elif (choix_3 == "2") :
                    print(dataTrans.getMinMax())
                elif (choix_3 == "3") :
                    print(dataTrans.minGlobal())
                elif (choix_3 == "4"):
                    print(dataTrans.maxGlobal())
                elif (choix_3 == "5"):
                    print(dataTrans.dPrime())
                elif(choix_3 == "6"):
                    break
                else:
                    print("Choix invalide")
            
            
        except :
            print("Donnee invalide")
            
    elif (choix == "3"):
        break
    else :
        print("choix invalide")

print("Fin ...")