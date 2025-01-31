import fonctionsNotes1
import pickle as pkl
import os

Notes={}
continuer = True
if os.path.getsize("notes.txt")>0:
    with open("notes.txt", "rb") as file:
        Notes = pkl.load(file)

while continuer:
    # Print menu
    print("\t\t\t ------- MENU -------")
    print("\t\t\t Quit               Q")
    print("\t\t\t Afficher notes     P")
    print("\t\t\t Moyenne            M")
    print("\t\t\t Majorant/Minorant  E")
    print("\t\t\t Ajouter étudiant   A")
    print("\t\t\t Supprimer étudiant S")
    print("\t\t\t --------------------")

    choice = input("\t\t\t Your choice? ").upper()

    if choice == "Q":
        continuer = False
        with open("notes.txt", "wb") as file:
            pkl.dump(Notes, file)
    elif choice== "P":
        fonctionsNotes1.affichage(Notes)
    elif choice== "M":
        fonctionsNotes1.moyenne(Notes)
    elif choice== "E":
        fonctionsNotes1.extrema(Notes)
    elif choice=="A":
        fonctionsNotes1.NewStudent(Notes)
    elif choice=="S":
        fonctionsNotes1.studentRemoval(Notes)
    else:
        print("Skill issue")