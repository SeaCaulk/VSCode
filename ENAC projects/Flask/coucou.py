import tkinter as tk

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Je sais qui tu es :)")

# Ajouter un label avec le texte "Coucou!"
label = tk.Label(fenetre, text="Coucou collègue d'adresse IP comment vas-tu?", font=("Arial", 20))
label.pack(padx=20, pady=20)

# Lancer l'interface graphique
fenetre.mainloop()
