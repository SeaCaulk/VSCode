import fonctionsVols
import pickle as pkl
import os

vols=[]
continuer = True
if os.path.getsize("vols.txt")>0:
    with open("vols.txt", "rb") as file:
        vols = pkl.load(file)

while continuer:
    # Print menu
    print("\t\t\t ------- MENU -------")
    print("\t\t\t Quit               Q")
    print("\t\t\t Afficher Vols      P")
    print("\t\t\t Départs aérodrome  D")
    print("\t\t\t Ajouter Vol        A")
    print("\t\t\t Supprimer Vol      S")
    print("\t\t\t --------------------")

    choice = input("\t\t\t Your choice? ").upper()

    if choice == "Q":
        continuer = False
        with open("vols.txt", "wb") as file:
            pkl.dump(vols, file)
    elif choice== "P":
        fonctionsVols.affichage(vols)
    elif choice=="D":
        fonctionsVols.departA(vols)
    elif choice=="A":
        fonctionsVols.flightAdd(vols)
    elif choice=="S":
        fonctionsVols.flightRemove(vols)
    else:
        print("Skill issue")