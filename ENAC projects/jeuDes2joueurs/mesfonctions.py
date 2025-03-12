import random

def init(filename,nom_joueur2):
    fic = open(filename,"w");
    fic.write("0\n0\n0 0\n") #le numero du tour, le joueur courant, puis les scores
    fic.close()

def jouer_tour(partie):
    partie["de1"] = random.randint(1,6) #on lance les 2 dés
    partie["de2"] = random.randint(1,6)
    if partie["de1"] == partie["de2"]:  #si le joueur fait un double il marque un point
        partie["scores"][partie["joueur_courant"]]+=1
    
    if partie['joueur_courant']==0: #alternance du joueur et incrémentation du tour
        partie['joueur_courant']=1
        partie['tour']+=1
    else:
        partie['joueur_courant']=0   
    

def charger_partie(filename):
    partie = {}
    with open(filename,"r") as fic:
        partie["tour"]=int(fic.readline().strip())
        partie["joueur_courant"] = int(fic.readline().strip())
        temp = fic.readline().split()
        partie["scores"]=[int(temp[0]),int(temp[1])]
    return partie

def sauver_partie(partie,filename):
    print(partie)
    #methode classique
    '''with open(filename,"w") as fic:
        fic.write(str(partie["tour"])+"\n")
        fic.write(str(partie["joueur_courant"])+"\n")
        fic.write(str(partie["scores"][0])+" "+str(partie["scores"][1]))'''
    with open(filename,"w") as fic:
        fic.write(f"{partie['tour']}\n{partie['joueur_courant']}\n{partie['scores'][0]} {partie['scores'][1]}")

    
        