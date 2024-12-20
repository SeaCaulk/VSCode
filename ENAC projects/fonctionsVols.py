

def affichage(l):
    print(l)

def flightAdd(l):
    l.append([int(input("Insérer ici le numéro du vol : ")),input("Insérer le nom du vol ici : "),input("Insérer le point de départ : "),input("Insérer le point d'arrivée : ")])

def flightRemove(l):
    r=int(input("Quel vol supprimer ? "))
    for i in range(0,len(l)):
        print(l[i],l[i][1])
        if l[i][0]==r:
            del l[i]
            break

def departA(l):
    a=input("Insérer le nom de l'aéroport ici : ")
    for i in range(0,len(l)):
        if l[i][2]==a:
            print(l[i])