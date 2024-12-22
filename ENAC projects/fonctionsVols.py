

def affichage(l):
    print(l)

def flightAdd(l):
    l.append([int(input("Insérer ici le numéro du vol : ")),input("Insérer le nom du vol ici : "),input("Insérer le point de départ : "),input("Insérer le point d'arrivée : "),input("Insérer l'heure de départ : "),input("Insérer l'heure d'arrivée : ")])

def flightRemove(l):
    r=int(input("Quel vol supprimer ? "))
    for i in range(0,len(l)):
        if l[i][0]==r:
            del l[i]
            break

def departA(l):
    a=input("Insérer le nom de l'aéroport ici : ")
    for i in range(0,len(l)):
        if l[i][2]==a:
            print(l[i])

def calculH(l):
    r=int(input("Insérer le numéro du vol ici : "))
    for j in range(len(l)):
        if l[j][0]==r:
            i=j
            break
    print(i)
    k=0
    kk=0
    if int(l[i][4][:2])>int(l[i][5][:2]):
        k=24
    if int(l[i][4][-2:])>int(l[i][5][-2:]):
        kk=60
    print("La durée du vol est de ",int(l[i][5][:2])+k-int(l[i][4][:2])," heures et ",int(l[i][5][-2:])+kk-int(l[i][4][-2:])," minutes")