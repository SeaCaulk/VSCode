

def affichage(D):
    print(D)

def studentRemoval(D):
    nom=input("Qui supprimer ? ")
    if nom in D:
        del D[nom]
    else:
        prenom=input("Insérer le prénom ici : ")
        del D[f"{nom}_{prenom}"]

def moyenne(D):
    S=0
    n=0
    for i in D:
        S+=sum(D[i])/len(D[i])
        n+=1
    print(S/n)

def extrema(D):
    l=[]
    for i in D:
        l.append([i,sum(D[i])/len(D[i])])
    l.sort()
    if len(l)>1:
        print(f"{l[0][0]} est le minorant avec {l[0][1]} :(")
        print(f"{l[-1][0]} est le majorant avec {l[-1][1]} :)")
    else:
        print("Pas assez d'élèves pour établir un majorant et un minorant")



def NewStudent(D):
    Err=False
    nom=input("Insérer le nom ici : ")
    note=int(input("Insérer le nombre de notes ici : "))
    N=[]
    for i in range(1,note+1):
        N.append(int(input(f"Insérer la note numéro {i} ici : ")))
    for i in N:
        if not 0<=i<=20:
            print("Note incohérente (pas entre 0 et 20)")
            Err=True
    if not Err:
        if nom in D:
            prenom=input("Insérer le prénom ici : ")
            D[f"{nom}_{prenom}"]=N
        else:
            D[nom]=N