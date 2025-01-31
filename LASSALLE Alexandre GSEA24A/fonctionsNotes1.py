

def affichage(D):
    print(D)

def studentRemoval(D):
    nom=input("A qui supprimer la note (nom) ? ")
    if nom in D:
        del D[nom]
    # else:
    #     prenom=input("Insérer le prénom ici : ")
    #     del D[f"{nom}_{prenom}"]

def moyenne(D):
    S=0
    n=0
    for i in D:
        S+=D[i]
        n+=1
    print(S/n)

def extrema(D):
    l=[]
    for i in D:
        l.append(D[i])
    l.sort()
    for i in D:
        if D[i]==l[0]:
            print(f"{i} est le minorant :( avec {l[0]}")
        if D[i]==l[-1]:
            print(f"{i} est le majorant :) avec {l[-1]}")



def NewStudent(D):
    nom=input("Insérer le nom ici : ")
    note=int(input("Insérer la note ici : "))
    if 0<=note<=20:
        if nom in D:
            pass
            # prenom=input("Insérer le prénom ici : ")
            # D[f"{nom}_{prenom}"]=note
        else:
            D[nom]=note
    else:
        print("Note incohérente (pas entre 0 et 20)")