
#########################################################################
# nom : jeu_ordi 
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu et 
#                  nombre d'allumette que l'on peut prendre au plus. 
# valeurs sortie : prise, nombre d'allumettes prises. 
# fonction : retourne la meilleure prise a faire 
######################################################################### 
def jeu_ordi(nb_allum, prise_max):
    s = prise_max + 1 
    t = (nb_allum - s) % (prise_max + 1) 
    while(t != 0): 
        s=s-1 
        t = (nb_allum - s) % (prise_max + 1) 
    prise = s - 1 
    if ( prise == 0): 
        prise = 1 
    print("l'ordi en prend : ", prise) 
    return prise


#########################################################################
# nom : jeu_humain 
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu et 
#                  nombre d'allumette que l'on peut prendre au plus. 
# valeurs sortie : prise, nombre d'allumettes prises. 
# fonction : retourne le nombre d'allumettes prises 
######################################################################### 
def jeu_humain(nb_allum, prise_max):
    prise = 0
    while( prise < 1 or prise > prise_max or prise > nb_allum): 
        try: 
            prise=int(input("Combien d'allumette vous desirez vous enlevez?")) 
        except: 
            print("saisie incorrecte")
    return prise

########################################################################
#nom : drow_allumette
#valeurs entree :nb_allum,  nombre d'allumette restant
#fonction : presenter le nombre d'allumette restant sous forme de dessin
########################################################################
def afficher_allumette(nb_allum):
    print("il rest "+str(nb_allum)+" allumette")
    for allum in range(nb_allum):
        print("o", end = "  ")
    print("")
    for allum in range(nb_allum):
        print("|", end = "  ")
    print("")
    

######################################################################### 
# nom : main 
# fonction : initialiser le jeu et l'organiser. 
######################################################################### 
def main(): 
    # initialisation des variables. 
    while True :
        nb_max_d=0 #nbre d'allumettes maxi au depart 
        nb_allu_max=0 #nbre d'allumettes maxi que l'on peut tirer au maxi 
        nb_allu_rest=0; #nbre d'allumettes restantes 
        prise=0 #nbre d'allumettes prises par le joueur 
        qui = -1 #qui joue? 0=User --- 1=PC
        choice = ""
    
        # verification pour l'initialisation. 
        while( nb_max_d < 10 or nb_max_d > 60): 
            try: 
                nb_max_d=int(input("Entrez un nombre max d'allumette au depart entre 10 et 60.")) 
            except: 
                print("saisie incorrecte")
        # mise a jour du nombre d'allumette en jeu. 
        nb_allu_rest=nb_max_d 
        #####################
        while( nb_allu_max < 1 or nb_allu_max > 10): 
            try: 
                nb_allu_max=int(input("Entrez un nombre max d'allumette  que l'on peut retirer entre 1 et 10.")) 
            except: 
                print("saisie incorrecte")
        #####################
        while( qui !=0 and qui !=1): 
            try: 
                qui=int(input("Qui commence? (0 pour vous et 1 pour l'ordinateur)")) 
            except: 
                print("saisie incorrecte")
        #Commencer le jeu tour a tour entre le joueur et l'ordinateur
        while(nb_allu_rest > 0):
            afficher_allumette(nb_allu_rest)
            if(qui == 0):
                prise = jeu_humain(nb_allu_rest, nb_allu_max)
                qui = 1
            else :
                prise = jeu_ordi(nb_allu_rest, nb_allu_max)
                qui = 0
            nb_allu_rest-= prise
        if(qui == 1):
            print("Vous avez perdu")
        else:
            print("L'ordinateur a perdu")
        ####Demandez au joueur s'il veut continuer ou arreter####
        while (choice != 'Y' and choice != 'N'):
            try: 
                choice=input("Voulez Vous continuer? Y/N")
            except: 
                print("saisie incorrecte")
        if(choice == 'N'):
            break
   
    
if __name__ == "__main__" :
    main()
