import math
from random import shuffle
import json
import os
import itertools
R,scores,cartesPosees,Joueurs,K=[],{},[],{},[]
cartes={f"{i}{k}":f"/static/img/Cartes/{j}_{k}.png" for i,j in [('H','Coeur'),('C','Carreau'),('P','Pique'),('T','Trefle')] for k in range(7,15)}

# cartes={'H7':'/static/img/Cartes/Coeur_7.png','H8':'/static/img/Cartes/Coeur_8.png','H9':'/static/img/Cartes/Coeur_9.png','H10':'/static/img/Cartes/Coeur_10.png','H11':'/static/img/Cartes/Coeur_Valet.png','H12':'/static/img/Cartes/Coeur_Dame.png','H13':'/static/img/Cartes/Coeur_Roi.png','H14':'/static/img/Cartes/Coeur_As.png',
#         'C7':'/static/img/Cartes/Carreau_7.png','C8':'/static/img/Cartes/Carreau_8.png','C9':'/static/img/Cartes/Carreau_9.png','C10':'/static/img/Cartes/Carreau_10.png','C11':'/static/img/Cartes/Carreau_Valet.png','C12':'/static/img/Cartes/Carreau_Dame.png','C13':'/static/img/Cartes/Carreau_Roi.png','C14':'/static/img/Cartes/Carreau_As.png',
#         'P7':'/static/img/Cartes/Pique_7.png','P8':'/static/img/Cartes/Pique_8.png','P9':'/static/img/Cartes/Pique_9.png','P10':'/static/img/Cartes/Pique_10.png','P11':'/static/img/Cartes/Pique_Valet.png','P12':'/static/img/Cartes/Pique_Dame.png','P13':'/static/img/Cartes/Pique_Roi.png','P14':'/static/img/Cartes/Pique_As.png',
#         'T7':'/static/img/Cartes/Trefle_7.png','T8':'/static/img/Cartes/Trefle_8.png','T9':'/static/img/Cartes/Trefle_9.png','T10':'/static/img/Cartes/Trefle_10.png','T11':'/static/img/Cartes/Trefle_Valet.png','T12':'/static/img/Cartes/Trefle_Dame.png','T13':'/static/img/Cartes/Trefle_Roi.png','T14':'/static/img/Cartes/Trefle_As.png'}
# if os.path.getsize("ENAC projects/BE/jeu.txt")>0:
#     with open("ENAC projects/BE/jeu.txt", "r") as file:
#         for i,j in enumerate((R,scores,cartesPosees,Joueurs,K)):
#             j=file.readline()
#             j=json.loads(j)
#             print(j,type(j))
if os.path.getsize("ENAC projects/BE/jeu.txt")>0:
    with open("ENAC projects/BE/jeu.txt", "r") as file:
        # for i,j in zip(range(R,scores,cartesPosees,Joueurs,K),file.readlines()):
        #         i=eval(j)
        #         print(i,type(i))
        R=eval(file.readline())
        scores=eval(file.readline())
        cartesPosees=eval(file.readline())
        Joueurs=eval(file.readline())
        K=eval(file.readline())

def save():
    with open("ENAC projects/BE/jeu.txt", "w") as file:
        file.write(f"{R}\n{scores}\n{cartesPosees}\n{Joueurs}\n{K}")

def randomSet():
    pass

def init(joueurs):
    i=1
    CartesC=shuffle(cartes.keys())
    for joueur in joueurs:
        Joueurs[joueur]=[]
        for carte in range(14+i):
            Joueurs[joueur].append(CartesC[carte])
            del CartesC[carte]
        i=0
    for i in range(len(CartesC)):
        if i%2==0:
            R.append(CartesC[-1])
            del CartesC[-1]
        else:
            K.append(CartesC[-1])
            del CartesC[-1]
    save()

def tour(joueur,cartes,input,R,K,carteAbandonnee, inputlists):
    illegal=False
    #prend une carte d'une des deux piles, selon le choix du joueur
    if input=='takeRandom':
        cartes[joueur].append(R[-1])
        del R[-1]
    elif input=='takeKnown':
        cartes[joueur].append(K[-1])
        del K[-1]

    #pose les cartes du joueur
    for inputlist in inputlists:
        inputlist.sort()
        if len(inputlist)>2 and (inputlist[0][1:]==inputlist[i][1:] for i in range(len(inputlist))):
            cartesPosees.append([inputlist])
        elif (inputlist[0][0]==inputlist[i][0] for i in range(len(inputlist))) and (inputlist[i][1:]==inputlist[i+1][1:]-1 for i in range(len(inputlist))):
            cartesPosees.append([inputlist])
        else:
            illegal=True
            return(illegal)
        
    #pose la carte choisie par le joueur
    K.append(cartes[joueur][carteAbandonnee])
    del cartes[joueur][carteAbandonnee]
    save()


def bot():
    pass

def AI():
    pass
