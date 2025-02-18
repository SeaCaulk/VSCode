import math

scores={}
cartes={}
R=[]
K=[]
def randomSet():
    pass

def init():
    pass

def tour(joueur,cartes,input,R,K,input2):
    if input=='takeRandom':
        cartes[joueur].append(R[-1])
        del R[-1]
    elif input=='takeKnown':
        cartes[joueur].append(K[-1])
        del K[-1]
    elif input=='leave':
        # enlever la carte du deck sur laquelle il clique somehow
        # event listener?
        # si c'est la dernière carte, fin du tour
        # ajouter la carte à la liste R ou K
        K.append(cartes[joueur][input2])
        del cartes[joueur][input2]
    elif input=='drop':
        # poser les cartes qu'il sélectionne, si légal
        pass


def bot():
    pass

def AI():
    pass
