from datetime import datetime

def affichage(l):
    print(l)

def flightAdd(l):
    l.append([int(input("Insérer ici le numéro du vol : ")),input("Insérer le nom du vol ici : "),input("Insérer le point de départ : "),input("Insérer le point d'arrivée : "),input("Insérer l'heure de départ : "),input("Insérer l'heure d'arrivée : "),input("Insérer la date : ")])

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
    h,m=calculHH(l[i][4],l[i][5])
    print("La durée du vol est de ",h," heures et ",m," minutes")

def heures(l,d):
    # S=0
    # for i in range(len(l)):
    #     if l[i][6][-2:]>d[-2:] or (l[i][6][-2:]==d[-2:] and l[i][6][3:5]>d[3:5]) or (l[i][6][-2:]==d[-2:] and l[i][6][3:5]==d[3:5] and l[i][6][2:]>d[2:]):
    #         h,m=calculHH(l[i][4],l[i][5])
    #         S+=h+m/60
    # print(S," heures")
    S=0
    df="%d/%m/%Y"
    d=datetime.strptime(d,df)
    for i in range(len(l)):
        if datetime.strptime(l[i][6],df)>d:
            h,m=calculHH(l[i][4],l[i][5])
            S+=h+m/60
    print(S," heures")

def calculHH(d1,d2):
    k=0
    kk=0
    if int(d1[:2])>int(d2[:2]):
        if int(d1[-2:])>int(d2[-2:]):
            k=23
        else:
            k=24
    if int(d1[-2:])>int(d2[-2:]):
        kk=60
    return int(d2[:2])+k-int(d1[:2]),int(d2[-2:])+kk-int(d1[-2:])