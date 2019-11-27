Programmation événementielle avec tkinter, Python 
====================

[![Project Status](http://opensource.box.com/badges/active.svg)](http://opensource.box.com/badges)
[![Project Status](http://opensource.box.com/badges/maintenance.svg)](http://opensource.box.com/badges)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/noutcha/Perl_API_Twitter.svg)](http://isitmaintained.com/project/noutcha/Perl_API_Twitter "Average time to resolve an issue")
[![Percentage of open issues](http://isitmaintained.com/badge/open/noutcha/Perl_API_Twitter.svg)](http://isitmaintained.com/project/noutcha/Perl_API_Twitter "Percentage of issues still open")
[![GPL License](https://badges.frapsoft.com/os/gpl/gpl.png?v=103)](https://opensource.org/licenses/GPL-3.0/)


Déscription
============
Python ? oui, python est un langage de programmation(langage de script) simple et puissant, 
il nous permet d'écrire un programme ou un bout de programme informatique qui va exécuter une 
fonction au moment de l'affichage d'une page web/execution ou de la réalisation d'une action utilisateur. 
Python est très simples mais si vous ètes prétentieux, vous pouvez travailler sur des projets 
plus ambitieux grâce à ses nombreuses bibliothèques.

programmer une interface utilisateur(IU) ou Graphic User Interface(GUI) en anglais est différent 
de la programmation sous console.  
L'histoire nous dit que les programmes console sont les touts premiers à apparaître. Comme par 
exemple Le premier vrai système d'exploitation: le DOS(Disk Operating System, 1981), et l'ordinateur
était un terminal dédié uniquement à l'envoi et au retour des commandes. Le code bloque tant que 
l’utilisateur n’a pas enfoncé la touche Entrée. Trés faible pour créer des fenêtres comme on le fait aujourd'hui.


Avez-vous eu l'idée d'une application avec une interface utilisateur avancée avec pyhton ?
Vous avez fait python en consol et vous voulez construire des fenetres et des boutons ?
Vous etes bien tomber avec python c'est facile et simple. 
Dans cet exemple, nous verrons comment creer un progamme avec IU en python en utilisant 
la bibliothèque tkinter(https://fr.wikipedia.org/wiki/Tkinter). 

Imaginez un jeu donc le principe est le suivant :
Le programme genère un nombre au hasard( ente 0 et 100 inclus) et vous devez deviner ce nombre 
et donner au programme, si vous trouvez le nombre, c'est à dire le nombre que vous donnez au 
programme est le nombre qu'il a generé, il vous felicitera.

Ne vous inquiétez, je l'ai écrit pour vous!

Conditions préalables
=====================

Vous deviez installer :
* [Python V3.8.0](https://docs.python.org/fr/3/using/index.html)


Installation de Python ?
------------ 
Oui, pour programmer avec python, vous avez besoin d'un environnement qui permet d'executer un programme python.
Vous deviez aussi avoir un editeur de texte. Moi j'ai utilisé Notepad++(mon preferé).

Pour etre court, allez à la source [Installation et utilisation de Python](https://docs.python.org/fr/3/using/index.htm)

On a parlé de TKinter python ?
------------ 
Oui !

Tkinter est un module de base intégré dans Python , normalement vous n'avez rien à faire pour 
pouvoir l'utiliser. L'un des avantages de Tkinter est sa portabilité sur les OS les plus utilisés 
par le grand public.

Pour tout savoir sur TKinter allez à la source [Interface graphique Tkinter python] (https://python.doctor/page-tkinter-interface-graphique-python-tutoriel)
Cette source m'a aider à realiser ce programme. le code du menu vient de là, c'est vraiment le good doctor.

Un grand merci à [Daniel Gillet](https://pythonfaqfr.readthedocs.io/en/latest/prog_even_tkinter.html) pour le tutoriel detaillé.

Example : importer Tkinter pour la creation de l'interface graphique(le fameux hello world)
------
Cet exemple est disponible sur le site pyhton.doctor  qui donne plus de details sur cette bibliothèque.


```python

# coding: utf-8
 
from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()

```

Bonnes pratique !!
------------ 
```python

 from tkinter import * 
 
```
est à éviter quand on importe une bibliothèque, car on fait appelle à tous les éléments et pourtant on ne doit 
pas les utiliser.

```python

# coding: utf-8

# On importe Tkinter pour la creation de l'interface graphique
import tkinter as tk #ici importation avec renommage


fenetre = tk.Tk()
fenetre.title("Bonjour le monde") # titre de ma fenetre


label = tk.Label(fenetre, text="Hello World") # contenu de la fenetre
label.pack()

fenetre.mainloop()

```


Si vous souhaitez des petits exemple de codes qui pourront enrichir votre
boite a outils de developreur, regardez les sources de mon depot.

Autres exemples et documentation
==========================

Pour plus de détails et des exemples de code, consultez 
la page de démonstration et de documentation sur: https://www.tutorialspoint.com/python3/python_gui_programming.htm

Construire à partir de la source
================================
Pour créer Devine à partir des sources, vous aurez simplement besoin d’un utilitaire make et de python 3 ou plus récent. 
Pour obtenir et compiler automatiquement Devine, vous aurez peut-être également besoin d'un client git.

Pour obtenir le Devine directement à partir de son dépôt:

```cmd

	>git clone git://github.com/noutcha/devine.git

```
La procédure d’exécution
========================
Pour exécuter le programme (en considérant que pyhton est déjà installer sur votre PC).
Si c'est n'est pas le cas, visitez la page  [Installation et utilisation de Python](https://docs.python.org/fr/3/using/index.htm) 
1)	Décompressez le fichier devine.zip sur votre disque local
2)	Placez-vous dans ce dossier décompressé et ouvrez l’invite de commande à cet endroit
3)	Tapez la commande >py devine.py

Extrait du code source
=======

```python


#Prémière version du jeu Devine.

#On crée une fenêtre simple qui demande à l'utilisateur de deviner le nombre secret.
#Avec une possibilité de guide en indiquant si le nombre choisi est plus grand 
#ou plus petit que le nombre secret.


# coding: utf-8
# On importe randint pour geberer les nombres aléatoire
from random import randint
# On importe Tkinter pour la creation de l'interface graphique
import tkinter as tk #ici importation avec renommage,  #from tkinter import * à éviter
from tkinter.messagebox import *


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
   

titre = tk.Label(app, text="Devine le nombre auquel je pense", font=("", 16))
titre.grid(row=0, columnspan=2, pady=8)

#Génération du nombre secret
nombre_secret = randint(0, 100) + 1 

lbl_reponse = tk.Label(app, text="Choisi un nombre entre 1 et 100 inclus:")
lbl_reponse.grid(row=1, column=0, pady=5, padx=5)

reponse = tk.Entry(app) # On demande ici la saisie dans le champ
reponse.grid(row=1, column=1, pady=5, padx=5)
reponse.bind("<Return>", user_recup_choix) # On affecte le resultat de la saisi dans la variable

#Création d'un bouton Quitter
bouton_quitter = tk.Button(app, text="Quitter", command=Quitter)
bouton_quitter.grid(row=3, column=2, pady=15, padx=15)

result = tk.Label(app, text="")
result.grid(row=2, column=1, pady=5, padx=5)

app.mainloop()

```
Aperçus du resultat
=======

R1
---
![Resultat](https://i.ibb.co/5hnRFGC/devine4.png)

R2
---

![Resultat](https://i.ibb.co/CM22zdM/devine2.png)

License
======
Double licence sous les licences MIT ou GPL version 2.


Contribuant
===========
**Michel NOUTCHA**  :wink:

<a href="https://ibb.co/HBs68F3"><img src="https://i.ibb.co/HBs68F3/ntm.jpg" width="50" height="50" alt="Michel NOUTCHA" border="0"></a>
