"""

Prémière version du jeu Deviner.

On crée une fenêtre simple qui demande à l'utilisateur de deviner le nombre secret.
Avec une possibilité de guide en indiquant si le nombre choisi est plus grand 
ou plus petit que le nombre secret

source d'inspiration: https://pythonfaqfr.readthedocs.io/en/latest/prog_even_tkinter.html#


"""
# coding: utf-8
# On importe randint pour geberer les nombres aléatoire
from random import randint
# On importe Tkinter pour la creation de l'interface graphique
import tkinter as tk #ici importation avec renommage,  #from tkinter import * à éviter
from tkinter.messagebox import *

# On defini notre fonction de traitement
def user_recup_choix(event):
    "fonction de rappel ou fonction de post-traitement quand le joueur a entré un nombre."
    nbre_choisi = int(reponse.get()) # on recupère la reponse de l'user
    reponse.delete(0, tk.END) # on vide le champ de saisie
    proposition["text"] = nbre_choisi #On recupère le choix de l'user
    if nombre_secret > nbre_choisi:
        result["text"] = "Le nombre est plus grand" # On affiche le texte pour aider l'user
    elif nombre_secret < nbre_choisi:
        result["text"] = "Le nombre est plus petit"
    else:
        # On enlève les éléments dont on n'a plus besoin
        lbl_reponse.destroy()
        reponse.destroy()
        # On replace les Labels `proposition` et `resultat` dans la ligne
        # en dessous du titre
        proposition.grid_forget()
        proposition.grid(row=1, column=0)
        result.grid_forget()
        result.grid(row=1, column=1)
        # On configure le label avec le texte voulu, dans le font voulu et
        # dans la couleur désirée.
        result.config(text="Tu as trouvé le nombre. Bravo!",
                        font=("", 12),
                        fg="green")


app = tk.Tk() # creation de la fenêtre
app.title("Mon premier jeu Avec Tkinter") # titre de ma fenetre


# fonction qutter
def Quitter():
    if askyesno('Confirmation', 'Êtes-vous sûr de vouloir quitter le jeu ?'):
        app.quit()
    else:
        showinfo('Confirmation', 'Continuer!')
		
# fonction a propos		
def Apropos():
   showinfo('A propos !', 'Devine (V1.0.0) est juste un jeu banal. \n le principe est simple, j\'ai un nombre et tu dois deviner ce nombre !')




# Menu de l'application
menubar = tk.Menu(app)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Créer")
menu1.add_command(label="Editer")
menu1.add_separator()
menu1.add_command(label="Quitter", command=app.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Couper")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=Apropos)
menubar.add_cascade(label="Aide", menu=menu3)

app.config(menu=menubar)
# fin menu

titre = tk.Label(app, text="Devine le nombre auquel je pense", font=("", 16))
titre.grid(row=0, columnspan=2, pady=8)

#Génération du nombre secret
nombre_secret = randint(0, 100) + 1 

lbl_reponse = tk.Label(app, text="Choisi un nombre entre 1 et 100 inclus:")
lbl_reponse.grid(row=1, column=0, pady=5, padx=5)

reponse = tk.Entry(app) # On demande ici la saisie dans le champ
reponse.grid(row=1, column=1, pady=5, padx=5)
reponse.bind("<Return>", user_recup_choix) # On affecte le resultat de la saisi dans la variable

#Création d'un Rejouer
bouton_rejouer = tk.Button(app, text="Rejouer")
bouton_rejouer.grid(row=3, column=1, pady=10, padx=10)


#Création d'un bouton Quitter
bouton_quitter = tk.Button(app, text="Quitter", command=Quitter)
bouton_quitter.grid(row=3, column=2, pady=15, padx=15)




proposition = tk.Label(app, text="")
proposition.grid(row=2, column=0, pady=5, padx=5)

result = tk.Label(app, text="")
result.grid(row=2, column=1, pady=5, padx=5)

app.mainloop()
