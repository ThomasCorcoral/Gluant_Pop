# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:39:46 2016

@author: Thomas Corcoral
"""

##########################################
#############  Importation  ##############
##########################################

import tkinter as tk
import random
#import Image
from PIL import Image
from PIL import ImageTk
import tkinter.font as tkFont

##########################################
########  Création de la fenêtre  ########
##########################################

fenetre = tk.Tk()                                                               #On créer la fenêtre principale
fenetre.title("Gluant P0P")                                                     #On nomme cette fenêtre par le nom du jeu "Gluant POP"

##########################################
#####  Initialisation des variables  #####
##########################################

quadrillage = 8                 
# Nombre de case dans le canvas, ici on peut réaliser un quadrillage de 8 cases par 8 cependant un carré de 6x6 est utilisé
large = 300                     
# Cette variable définie la largeur du canvas de mini-jeu.
haut = large
# Celle-ci la hauteur, on souhaite obtenir un carré elle est donc égale à la largeur
pts_de_vie = 500
# Il s'agit de l'initialisation des points de vie du boss, ceux-ci changeront au fil des niveaux
niveau = 1
# Variable des niveaux, a chaque fois qu'un monstre est tué (pts_de_vie <= 0) on gagne un niveau
# Cette dernière permettra la gestion des points de vie, des fond et des gluants
limite_clic = 20
# Intialisation du nombre de coups restant, cette variable va beaucoup évoluer durant le jeu
degat = 0
#Dégâts infligés par le joueur au boss, le but de cette variable est de compté les dégâts (les points)
#que le joueur inflige au boss. Elle est réinitialisé à chaque niveau, le but de cette variable est 
#de vérifier que le monstre n'est pas tué et de faire descendre la barre de vie
start_jeu2 = False
#Variable vérifiant le lancement du second mini-jeu ou il faut attraper un gluant, son rôle
#est d'arrêter le minuteur lorsque le jeu est fini.
argent = 0
#Variable représentant l'argent du joueur, l'argent est gagner grace au dégâts en surplus
#C'est à dire que si l'utilisateur inflige un total de 570 dégats au monstre alors que ce
#dernier avait 500 points de vie, le joueur gagne 70 pièces (argent)
blocage = True
#Cette variable est utilisé pour le tutoriel afin que l'utilisateur ne puisse pas appuyer
#très rapidement sur la fenêtre et causer des problèmes au programme. Son rôle est de fluidifier le programme
pages_tuto = 0
# Initialisation de l'image en cours de lecture dans la liste ci-dessous
images_tuto = ["images/tuto/tuto1.png","images/tuto/tuto2.png","images/tuto/tuto3.png","images/tuto/tuto4.png","images/tuto/tuto5.png","images/tuto/tuto6.png","images/tuto/tuto7.png","images/tuto/tuto8.png","images/tuto/tuto9.png","images/tuto/tuto10.png"]
#Liste des images du tutoriel
bonus = 1
#Cette variable est définie sur 1 afin de ne pas influencer les dégâts dès le début. En effet,
#son rôle est de multiplier les dégâts, à l'initialisation ils sont donc multipliés par 1
#puis grace à des achats dans la boutique il est possible de multiplier cette variable et donc ses dégâts.
achat1 = True
achat3 = True
achat4 = True
#Les trois variable ci-dessus ont pour but de ne pas autorisé l'achat d'un objet dans la boutique plus d'une fois
lettre=0
#Variable utilisé dans l'affichage du texte lors de l'ouverture de la boutique, elle augmente de 1
#à chaque fois q'une lettre est positionnée afin de séléctionner la lettre suivante.
place=125
#Coordonés de la lettre positionnée, augmente à chaque fois pour positionné la lettre suivante
debug_clic = True
#Variable bloquante qui empêche à l'utilisateur de cliqué lorqu'elle est positionnée sur "Flase"
#Son but est d'empêcher un clic lorsque l'animation d'explosion est en marche.
timer = 0
#Variable minuteur créant le ddécompte pour le second mini-jeu.
goutte = ImageTk.PhotoImage(Image.open('images/jeu/goutte2.png'))
#variable contenant l'image de l'animation de l'explosion 
var_y=0
#coordonées en y du boss, utile lors de son animation
var_x=0
#coordonées en x du boss, utile lors de son animation
r = 15
#Variable contenant le rayon du gluant, son rôle est de déplacer le gluant et de vérifier 
#que l'utilisateur clic bien dessus lors du second mini-jeu
coord_x = large/2
#coordonées en x du milieu du canvas, utilisé pour le second mini-jeu afin de positionner le
#gluant au milieu de l'écran
coord_y = haut/2
#coordonées en y du milieu du canvas, utilisé pour le second mini-jeu afin de positionner le
#gluant au milieu de l'écran
ran_1 = random.uniform(0 , 1)
#Un nombre aléatoir entre 0 et 1 afin d'avoir 2 vitesse différentes en x et y par la suite
ran_2 = random.uniform(0 , 1)
#Un nombre aléatoir entre 0 et 1 afin d'avoir 2 vitesse différentes en x et y par la suite
vitesse = 8*(3 * (niveau*1.2))
#Vitesse de base de la modification des coordonées pour le second mini-jeu
dif_x = vitesse* ran_1
#Une vitesse de modification des coordonées en x aléatoire grace aux variables précédentes, cela 
#permet au gluant d'avoir des rebonds aléatoires (pour le second mini-jeu)
dif_y = vitesse* ran_2
#Une vitesse de modification des coordonées en y aléatoire grace aux variables précédentes, cela 
#permet au gluant d'avoir des rebonds aléatoires (pour le second mini-jeu)
sec = 24
#Temps de base du minuteur pour le deuxième mini-jeu, il sera modifié en diminuant au gré des niveaux
helv36 = tkFont.Font(family='Helvetica',size=10, weight='bold')
helv362 = tkFont.Font(family='Helvetica',size=8, weight='bold')
helv363 = tkFont.Font(family='Helvetica',size=6, weight='bold')
#Trois différents font utilisés pour la boutique, elles modifient la police d'écriture, la taille
#Et définissent une écriture en gras.
fontttt = tkFont.Font(family='comic sans ms', size=12)
#font utilisé cette fois-ci pour le menu, il modifie la police d'écriture et la taille.
boutique_verif = False
#Variable indiquant si la boutique est ouverte ou non, au début, elle est fermé.
num_lettre = 0
#Variable utilisé dans l'affichage du texte de l'histoire, elle augmente de 1
#à chaque fois q'une lettre est positionnée afin de séléctionner la lettre suivante.
rang = 127
#position de la lettre par rapport à la rangée
ligne = 250
#position de la lettre par rapport aux lignes
font_hist = tkFont.Font(family='Helvetica',size=18, weight='bold')
#font pour le texte de l'histoire

##########################################
##############  Quitter  #################
##########################################

def quitter():
    fenetre.destroy()
    
#cette fonction a pour simple but de détruire la fenêtre, elle sera appeler lorsque l'utilisateur
#appuye sur un bouton quitter.

##########################################
##########  Zone du mini-jeu  ############
##########################################

mini_jeu = tk.Canvas(fenetre, width=large, height = haut)
mini_jeu.grid(row=20,column=2,columnspan=10,rowspan=10)

#Création du canvas pour le mini-jeu principal, il ne sera pas dominant au début et laissera
#place aux autres canvas du menu, de l'histoire et du tuto.

##########################################
###########  Zone du combat  #############
##########################################

combat = tk.Canvas(fenetre, width=large, height = haut/(1.5), bg = "white")
combat.grid(row=1,column=2,columnspan=7,rowspan=10)

#Création du canvas de la zone de combat, la ou sera affiché le boss, sa barre de vie, le nombre
#de coups restant et le fond du boss. Ce dernier sera églamenent secondaire au début

##########################################
################# Menu ###################
##########################################

menu = tk.Canvas(fenetre, width=1020, height=750)
menu.grid(row=0,column=0,rowspan=100,columnspan=100)

#Création du canvas du menu, celui-ci sera principale au début, il sera supprimer par la suite
#afin de laisser place au jeu.

##########################################
##############  Lancement  ###############
##########################################

def demarage():
    global foret, jouer, jouer_sans_histoire, quitte, image_menu
    foret = Image.open('images/bg/foret.png')                                 #Importation de l'image de fond
    foret = foret.resize((1022,800), Image.ANTIALIAS)               #On retaille l'image afin qu'elle rentre dans le canvas et occupe ce dernier en entier
    foret = ImageTk.PhotoImage(foret)                               #On l'ouvre ensuite
    image_menu = menu.create_image(0,0,anchor='nw',image=foret)     #Puis on définie l'image sur le canvas, ici on la définie avant tous le reste afin qu'elle soit au dernier plan          
    jouer=tk.Button(menu, text='Jouer',command=histoire, font = fontttt, bg = "skyblue")            #Création du premier boutton, sur ce dernier sera écrit "Jouer" il engendrera la fonction histoire, utilise le font créer lors de l'initialisation "fonttt" et possède un fond bleu clair.
    jouer.place(relx=.193,rely=.560)                                #Cette ligne permet de positionner le boutton sur le canvas à des coordonés précises.
    jouer_sans_histoire=tk.Button(menu, text="Passer l'histoire \n et jouer",command=demande_tuto, font = fontttt, bg = "skyblue")          #Création d'un boutton pour jouer sans devoir faire l'histoire, il lance directement la fonction demande_tuto. Il reprend les mêmes caractéristiques que le boutton précédent.
    jouer_sans_histoire.place(relx=.698,rely=.560)                  #Cette ligne permet de positionner le boutton sur le canvas à des coordonés précises.
    quitte=tk.Button(menu, text='Quitter',command=quitter, font = fontttt, bg = "skyblue" )         #Un simple boutton pour quitter qui renvoie à la fonction définie précédemment quitter. Il reprend les mêmes caractéristiques que les deux autres bouttons.
    quitte.place(relx=.455,rely=.880)                               #Cette ligne permet de positionner le boutton sur le canvas à des coordonés précises.
    
# Cette fonction est celle qui se lancera lorsque l'utilisateur lancera le programme.
# Elle va tout d'abord créer un image de fond puis positionner les bouttons nécésseaires 

fenetre.after(100, demarage)

#Un after à pour but de lancer une fonction après un temps donné, ici on lance 
#la fonction demarage apres 0.1 seconde. Cela permet d'afficher le menu lorsque l'on démarre le programme.

##########################################
############### Histoire #################
##########################################
    
def histoire():
    global texte_liste, fond_ecran_histoire, fond_histoire, histoire_can
    menu.destroy()                                                              #Suppression du canvas du menu
    histoire_can = tk.Canvas(fenetre, width=1020, height=750)                   #Crée un canvas nommé histoire utilisé pour cette fonction uniquement
    histoire_can.grid(row=0,column=0,rowspan=100,columnspan=100)                #Affiche le canvas
    fond_histoire = Image.open('images/bg/background.png')                                #Importation de l'image de fond
    fond_histoire = fond_histoire.resize((1022,800), Image.ANTIALIAS)           #On retaille l'image afin qu'elle rentre dans le canvas et occupe ce dernier en entier
    fond_histoire = ImageTk.PhotoImage(fond_histoire)                           #On l'ouvre ensuite
    fond_ecran_histoire = histoire_can.create_image(0,0,anchor='nw',image=fond_histoire)     #Puis on définie l'image sur le canvas, ici on la définie avant tous le reste afin qu'elle soit au dernier plan
    fichier_texte = open('texte/histoire.txt')                                        #On ouvre le fichier texte contenant l'histoire
    fichier_texte = fichier_texte.readlines()                                   #On lit ce texte
    fichier_texte = fichier_texte[0]                                            #On sélectionne le premier paragraphe du texte (soit tout le texte)
    texte_liste = fichier_texte.split("@")                                      #Puis on sépare l'unique terme de la liste en pleins de terme (un terme par lettre), en effet chaque caractère est séparé par un arobase dans le fichier texte.
    testhistoire()                                                              #On lance la fonction qui affiche les lettres 

#Fonction de démarage de l'histoire, elle met en place le canvas et les lettres du texte
    
def testhistoire():
    global num_lettre, texte_histoire, rang, ligne
    if num_lettre == (len(texte_liste)):                                        #Si le texte a entièrement été affiché
        fenetre.after(3000,fin_histoire)                                        #On lance la fonction fin_histoire après 3 secondes
    elif num_lettre == 67 or num_lettre == 130 or num_lettre == 189 or num_lettre == 250 or num_lettre == 306 or num_lettre == 370:         #Si la ligne est finie
        ligne = ligne + 60                                                      #On saute la ligne
        rang = 125                                                              #On remet la position de la première lettre au début de la rangée
        num_lettre=num_lettre + 1                                               #On passe à la lettre suivante
        texte_histoire = histoire_can.create_text(rang,ligne,text=str(texte_liste[num_lettre]),fill='black',font =font_hist)               #On affiche une lettre
        fenetre.after(35,testhistoire)                                          #Après 0.035 secondes, on relance la fonction pour afficher la lettre suivante        
    else:                                                                       #Sinon
        texte_histoire = histoire_can.create_text(rang,ligne,text=str(texte_liste[num_lettre]),fill='black',font =font_hist)               #On affiche une lettre
        rang=rang + 12                                                          #On décalle la position de la prochaine lettre sur la rangée
        num_lettre=num_lettre+1                                                 #On passe à la lettre suivante
        fenetre.after(35,testhistoire)                                          #Après 0.035 secondes, on relance la fonction pour afficher la lettre suivante
        
#Fonction qui tourne jusqu'à ce que toutes les lettres soient affichés, sont rôle est
#d'afficher le texte.
        
def fin_histoire():
    histoire_can.destroy()                                                      #On supprime le canvas de l'histoire    
    demande_tuto()                                                              #On lance la fonction de demande du tutoriel
    
#Le but de cette fonction est d'assurer la liaison entre l'histoire et le tutoriel.
    
##########################################
############### Tutoriel #################
##########################################

def demande_tuto():
    global demande, oui, non, fond_demande, fond_d_ecran
    menu.destroy()                                                  #Détruit le canvas menu et tout ce qui était positionné dessus.
    demande = tk.Canvas(fenetre, width=1020, height=750)            #Crée un canvas nommé demande utilisé pour cette fonction uniquement
    demande.grid(row=0,column=0,rowspan=100,columnspan=100)         #Affiche le canvas
    fond_demande = Image.open('images/bg/foret2.png')                         #Importation de l'image de fond
    fond_demande = fond_demande.resize((1022,800), Image.ANTIALIAS)             #On retaille l'image afin qu'elle rentre dans le canvas et occupe ce dernier en entier
    fond_demande = ImageTk.PhotoImage(fond_demande)                 #On l'ouvre ensuite
    fond_d_ecran = demande.create_image(0,0,anchor='nw',image=fond_demande)     #Puis on définie l'image sur le canvas, ici on la définie avant tous le reste afin qu'elle soit au dernier plan
    oui = tk.Button(demande, text='Oui',command=dem_oui, font = fontttt, bg = "skyblue")        #Création d'un boutton "Oui" éxecutant la fonction dem_oui
    oui.place(relx=.240,rely=.525)                                  #Cette ligne permet de positionner le boutton sur le canvas à des coordonés précises.
    non = tk.Button(demande, text="Non",command=dem_non, font = fontttt, bg = "skyblue")        #Création d'un boutton "Oui" éxecutant la fonction dem_non
    non.place(relx=.700,rely=.525)                                  #Cette ligne permet de positionner le boutton sur le canvas à des coordonés précises.
    
# la fonction ci-dessus est lancé après l'histoire ou bien après avoir appuyer sur le boutton
#permettant de lancer le jeu sans l'histoire (dans le menu de démarrage). Elle consiste en 
#la création d'une image de fond possédant un texte demandant à l'utilisateur s'il veut
#accéder au tutoriel. Afin qu'il puisse répondre, cette fonction met en place deux bouttons
#avec un texte simple "oui" "non". 

def dem_oui():
    demande.destroy()       #Suppression du canvas demande et tout ce qu'il contenait
    start_tuto()            #Lancement de la fonction start_tutoet donc du tutoriel
    
#Fonction de démarage du tutoriel
    
def dem_non():
    demande.destroy()       #Suppression du canvas demande et tout ce qu'il contenait
    grille()                #Lancement de la fonction grille et donc du jeu

#Cette fonction passe le tutoriel et lance directement le jeu.
    
def wait():
    global blocage
    blocage = True
    
#fonction de débloquer l'utilisateur qui pourra à nouveau cliquer sur le canvas 
#et faire avancer le tutoriel

def start_tuto():
    global ex, tuto
    tuto = tk.Canvas(fenetre, width=1020, height=750)           #Création du canvas pour le tutoriel
    tuto.grid(row=0,column=0,rowspan=100,columnspan=100)        #Affichage de ce canvas
    ex = ImageTk.PhotoImage(Image.open('images/tuto/tuto1.png'))            #On ouvre la première image (une sorte de diapositive) du tutoriel
    tuto.create_image(0,0,anchor='nw',image=ex)                 #On affiche cette image
    tuto.bind("<Button-1>",tutoriel)                            #Le programme active la détection de clique sur la canvas tuto et indique que lorsqu'un clique est détécter le programme doit renvoyer la fonction tutoriel.

#Cette fonction démarre le tutoriel en créant le canvas, affichant la première 
#image et installant la détection de clique.
    
def tutoriel(event):
    global pages_tuto, Tuto, blocage, images_tuto
    if blocage == True:                                         #Vérification que le clique n'est pas désactivé
        blocage = False                                         #Désactivation du clique pour fluidifier le programme
        pages_tuto = pages_tuto + 1                             #Passage à la page suivante
        try :                                                   #Fonction try utilisé ici pour ne pas que le programme renvoie une erreur lors du dernier clique.
            Tuto = ImageTk.PhotoImage(Image.open(images_tuto[pages_tuto]))      #On ouvre l'image suivant
            tuto.create_image(0,0,anchor='nw',image=Tuto)                       #On affiche cette image
        except IndexError:                                      #Si on a une erreur de sortie de liste
            None                                                #On ordonne au programme de l'ignorer.
        fenetre.after(500,wait)                                 #Après 0.5 secondes, on renvoie la fonction wait afin de débloquer le clique.
    if pages_tuto == 10 :                                       #Si toutes les pages ont été visionnés, 
        fin_tuto()                                              #On renvoie la fonction fin_tuto
    
#La fonction tutoriel a pour but de faire défiller les images du tutoriel. 
#Et de détecter lorsque toutes les images ont été affichés
        
def fin_tuto():
    tuto.destroy()                                              #Suppression du canvas tuto et tout ce qu'il contenait
    grille()                                                    #Lancement de la fonction grille et donc lance le jeu.
    
#Cette fonction met fin au tutoriel et lance le jeu.    
    
##########################################
##########  Défaite - Rejouer ############
##########################################

def perdu():
    global limite_clic, ll, img, lose, rej, verif_bulle
    global boutique, boutique_verif
    if limite_clic == 0 and degat < pts_de_vie:                                 #Si l'utilisateur n'a plus de coups et que le monstre a encore des points de vie
        verif_bulle = False                                                     #On désactive les animations
        mini_jeu.delete("all")                                                  #On supprime tout ce qu'il y avait sur le canvas mini_jeu
        combat.delete("all")                                                    #On supprime tout ce qu'il y avait sur le canvas combat
        lose = tk.Label(fenetre, text="Vous avez perdu")                        #Le programme affiche au joueur qu'il a perdu
        lose.grid(row=5,column=2,columnspan=10)                                 #Il place ce texte 
        boutique.destroy()                                                      #Il détruit le boutton boutique
        if boutique_verif == True :                                             #Si la boutique est ouverte
            boutique_verif = False                                              #Il indique qu'elle est fermé
            Fermer.destroy()                                                    #Il supprime le bouton Fermer
            shoop.destroy()                                                     #Il supprime le canvas shoop, qui est celui de la boutique
        rej = tk.Button(fenetre, text = 'Rejouer', command = rejouer)           #Création d'un bouton rejouer
        rej.grid(row=31,column=3,rowspan=1,columnspan=1)                        #Positionnement de ce bouton
    elif limite_clic < 0 :                                                      #Si l'utilisateur a moins de 0 coup, c'est à dire s'il s'est amusé à appuyer alors qu'il avait perdu
        mini_jeu.delete("all")                                                  #On veille à ce que le canvas mini_jeu reste vide
        combat.delete("all")                                                    #De même pour le canvas combat
    
#Cette fonction intervient à chaque clique et vérifie que le joueur n'a pas perdu.
#Si ce dernier à perdu, elle ferme le jeu (et pas la fenêtre) et propose deux options
#au joueur, soit quitter, soit rejouer.
        
def rejouer():
    global limite_clic, degat, niveau, pts_de_vie, boutique
    mini_jeu.delete("all")                                                      #On veille à ce que le canvas mini_jeu reste vide
    combat.delete("all")                                                        #De même pour le canvas combat
    limite_clic = 20                                                            #On réinitialise : le nombre de cliques possible,
    niveau = 1                                                                  #le niveau,
    degat = 0                                                                   #les dégâts,
    pts_de_vie = 500                                                            #les points de vie du boss
    lose.destroy()                                                              #suppression du message indiquant au joueur qu'il avait perdu    
    rej.destroy()                                                               #suppression du boutton rejouer
    grille()                                                                    #lance la fonction grille et donc lance le jeu
    
#Cette fonction redémarre le jeu et supprime les créations de la fonction perdu.
    
##########################################
#######  Changement de niveau  ###########
##########################################

def ch_niveau():
    if degat > pts_de_vie :                                                     #Si le monstre est mort (que les dégâts causés par le joueur sont plus importants que les points de vi du boss)    
        jeu2()                                                                  #On lance le second mini-jeu avec l'appel de la fonction jeu2

#Vérifie que le joueur a gagné ou pas et lance le second mini-jeu        
        
def ch_niveau2():
    global degat, niveau, pts_de_vie, limite_clic, argent, bdv
    global boutique, boutique_verif, shoop, verif_bulle, lose, rej
    limite_clic = limite_clic + 20 + random.choice([2,4,6,8,10])                #Augmente le nombre de cliques de 20 + un nombre aléatoire (2,4,6,8,10)
    niveau = niveau + 1                                                         #On passe au niveau supérieur 
    argent = argent + degat - pts_de_vie                                        #Ajout de l'argent gagné au joueur soit les dégâts superflus
    degat = 0                                                                   #On réinitialise les dégâts causé par le joueur à 0
    bdv = 30                                                                    #On réinitialise la barre de vie du boss
    if niveau < 3 :                                                             #Si le niveau est inférieur à 3
        pts_de_vie = 500 + pts_de_vie                                           #Le boss gagne 500 points de vie en plus 
    elif 3 <= niveau < 6 :                                                      #Si le niveau est compris entre 3 et 6        
        pts_de_vie = 250 + pts_de_vie                                           #Le boss gagne 250 points de vie en plus
    else :                                                                      #Sinon
        pts_de_vie = 125 + pts_de_vie                                           #Le boss gagne 125 points de vie en plus
    mini_jeu2.destroy()                                                         #Suppression du canvas du second mini-jeu et tout ce qui était disposé dessus
    boutique.destroy()                                                          #Detruit le boutton boutique
    grille()                                                                    #Relance la création du jeu mais avec un niveau différent défini ci-dessus    
    if boutique_verif == True :                                                 #Si la boutique est ouverte
        boutique_verif = False                                                  #On rentre dans la variable l'information qu'elle est fermée 
        shoop.destroy()                                                         #On supprime le canvas de la boutique et donc on ferme la boutique.
    if niveau == 11 :                                                           #Si le niveau atteint est le 11ème alors le joueur à passé les 10 niveaux et a gagné.
         lose = tk.Label(fenetre, text="Vous avez sauvé l'île ! Bravo")         #Enregistre le message disant au joueur qu'il a gagné
         lose.grid(row=5,column=2,columnspan=10)                                #Dispose ce message sur l'écran        
         verif_bulle = False                                                     #On désactive les animations
         mini_jeu.delete("all")                                                  #On supprime tout ce qu'il y avait sur le canvas mini_jeu
         combat.delete("all")                                                    #On supprime tout ce qu'il y avait sur le canvas combat
         boutique.destroy()                                                      #Il détruit le boutton boutique
         if boutique_verif == True :                                             #Si la boutique est ouverte
             boutique_verif = False                                              #Il indique qu'elle est fermé
             Fermer.destroy()                                                    #Il supprime le bouton Fermer
             shoop.destroy()                                                     #Il supprime le canvas shoop, qui est celui de la boutique
         rej = tk.Button(fenetre, text = 'Rejouer', command = rejouer)           #Création d'un bouton rejouer
         rej.grid(row=31,column=3,rowspan=1,columnspan=1)                        #Positionnement de ce bouton
         mini_jeu.unbind("<Button-1>")                                           #désactivation de la détection de clique 
         

#Cette fonction a pour but de lancer le niveau suppérieur et de vérifier que le
#joueur a gagné ou non.
         
##########################################
############# lancement ##################
##########################################

def grille():
    global photo, img, couleur_gluant, Degats, Nb_coups, liste_gluant, images, verif_bulle
    global l, niveau, japon, monstre, bdv, exex, barre_de_vie, vie, boutique, fermeture, barre
    verif_bulle = True                                                          #On active les animations de clique
    images = []                                                                 #Création d'une liste image qui permettra aux images de ne pas disparaitre
    liste_gluant = []                                                           #Création d'une seconde liste dans laquelle on rentrera l'identité des gluants
    l = []                                                                      #Utilisé uniquement dans cette fonction pour créer des listes de liste afin de pouvoir ranger les gluants en fonction de leurs coordonées    
    bdv = 30                                                                    #Réinitialisation de la barre de vie
    couleur_gluant = []                                                         #Utilisé comme liste de liste pour pouvoir ranger l'identité des gluants de la même sorte que les images                                                        
    fermeture = tk.Button(fenetre, text = 'Quitter', command = quitter)         #Création d'un boutton quitter
    fermeture.grid(row=30,column=3,rowspan=1,columnspan=1)                      #Affichage de ce boutton
    Nb_coups = combat.create_text(25,10,text='Coups :'+str(limite_clic))        #Création d'un texte avec le nombres de coups restants
    x = large/quadrillage                                                       #division d'un côté du carré par le nombre de carrés dans la division du canvas, cela permet de pouvoir positionner les gluants par la suite
    boutique=tk.Button(fenetre, text='Boutique',command=shop)                   #Création d'un boutton boutique
    boutique.place(relx=.750,rely=.950)                                         #Affichage du boutton boutique
    if niveau < 3 :                                                             #Si le niveau est inférieur à 3
        choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png"]      #Le choix peut se faire entre 3 gluants différents
        japon = Image.open('images/bg/asian-bg.jpg')                                      #Importation de l'image de fond
        japon = japon.resize((300,200), Image.ANTIALIAS)                        #On retaille l'image pour qu'elle soit à la bonne taille
        japon = ImageTk.PhotoImage(japon)                                       #On Ouvre l'image
        combat.create_image(150,100,image=japon)                                #On place l'image sur le canvas
        im = Image.open('images/bg/fond.jpg')                                             #Importation de l'image de fond du mini-jeu (fond des gluants)
        photo=ImageTk.PhotoImage(im)                                            #Ouvreture de l'image
        mini_jeu.create_image(0,0,anchor='nw',image=photo)                      #On place l'image sur le canvas
        if niveau==1:                                                           #Si le joueur est au niveau 1
            monstre = Image.open('images/monstres/Giant_hill.png')                              #Importation de l'image du boss
            monstre = monstre.resize((150,200), Image.ANTIALIAS)                #On retaille l'image pour qu'elle soit à la bonne taille
            monstre = ImageTk.PhotoImage(monstre)                               #On ouvre l'image
            exex = combat.create_image(150,118,image=monstre)                   #On place l'image sur le canvas
        if niveau==2:                                                           #Changement de monstre pour le niveau 2    
            monstre = Image.open('images/monstres/monstre2.png')
            monstre = monstre.resize((145,190), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(140,105,image=monstre)
    elif 3 <= niveau < 6 :                                                      #Si le niveau est compris entre 3 et 6
        choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png","gluants\gluant4.png"]        #Le choix peut se faire entre 4 gluants différents
        japon = Image.open('images/bg/fond_boss_feu.jpg')                                 #Importation de l'image de fond
        japon = japon.resize((300,200), Image.ANTIALIAS)                        #On retaille l'image pour qu'elle soit à la bonne taille
        japon = ImageTk.PhotoImage(japon)                                       #On Ouvre l'image
        combat.create_image(150,100,image=japon)                                #On place l'image sur le canvas
        im = Image.open('images/bg/lave.jpg')                                             #Importation de l'image de fond du mini-jeu (fond des gluants)
        photo=ImageTk.PhotoImage(im)                                            #Ouvreture de l'image
        mini_jeu.create_image(0,0,anchor='nw',image=photo)                      #On place l'image sur le canvas
        if niveau==3:                                                           #Changement de monstre pour le niveau 3
            monstre = Image.open('images/monstres/monstre4.png')
            monstre = monstre.resize((150,150), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,110,image=monstre)
        if niveau==4:                                                           #Changement de monstre pour le niveau 4
            monstre = Image.open('images/monstres/monstre lave.png')
            monstre = monstre.resize((150,180), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,118,image=monstre)
        if niveau==5:                                                           #Changement de monstre pour le niveau 5
            monstre = Image.open('images/monstres/monstre poison.png')
            monstre = monstre.resize((200,200), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,118,image=monstre)
    else :                                                                      #Sinon (si l'utilisateur d"passe le niveau 6)
        choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png","gluants\gluant4.png","gluants\gluant5.png"]      #Le choix peut se faire entre 5 gluants différents
        japon = Image.open('images/bg/fond_boss_air.jpg')                                 #Importation de l'image de fond
        japon = japon.resize((300,200), Image.ANTIALIAS)                        #On retaille l'image pour qu'elle soit à la bonne taille
        japon = ImageTk.PhotoImage(japon)                                       #On Ouvre l'image
        combat.create_image(150,100,image=japon)                                #On place l'image sur le canvas
        im = Image.open('images/bg/ciel.jpg')                                             #Importation de l'image de fond du mini-jeu (fond des gluants)
        photo=ImageTk.PhotoImage(im)                                            #Ouvreture de l'image
        mini_jeu.create_image(0,0,anchor='nw',image=photo)                      #On place l'image sur le canvas
        if niveau==6:                                                           #Changement de monstre pour le niveau 6
            monstre = Image.open('images/monstres/boss3.png')
            monstre = monstre.resize((200,150), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,110,image=monstre)
        if niveau==7:                                                           #Changement de monstre pour le niveau 7
            monstre = Image.open('images/monstres/monstre3.png')
            monstre = monstre.resize((150,180), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,118,image=monstre)
        if niveau==8:                                                           #Changement de monstre pour le niveau 8
            monstre = Image.open('images/monstres/boss2.png')
            monstre = monstre.resize((200,200), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,118,image=monstre)
        if niveau==9:                                                           #Changement de monstre pour le niveau 9
            monstre = Image.open('images/monstres/monstre5.png')
            monstre = monstre.resize((200,150), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,110,image=monstre)
        if niveau==10:                                                           #Changement de monstre pour le niveau 10
            monstre = Image.open('images/monstres/monstre6.png')
            monstre = monstre.resize((140,140), Image.ANTIALIAS)
            monstre = ImageTk.PhotoImage(monstre)
            exex = combat.create_image(150,118,image=monstre)    
    barre_de_vie = Image.open('images/jeu/barre_de_vie.png')                               #Importation de limage du contour de la barre de vie du monstre
    barre_de_vie = barre_de_vie.resize((25,175), Image.ANTIALIAS)               #On reataille la barre de vie
    barre_de_vie = ImageTk.PhotoImage(barre_de_vie)                             #On l'ouvre
    combat.create_image(250,100,image=barre_de_vie)                             #On la place au bonne endroit sur le canvas
    vie = combat.create_rectangle(245.5, 170, 255.5, bdv, fill="red", width=0)          #On créer le rectangle
    combat.tag_raise(vie)                                                       #Le rectangle rouge utilisé pour la barre de vie est prioritaire sur les autres images
    barre = Image.open('images/jeu/ndc.png')                                               #Importation de l'image de la barre de nombre de coups    
    barre = barre.resize((120,75), Image.ANTIALIAS)                             #On retaille cette image
    barre = ImageTk.PhotoImage(barre)                                           #On Ouvre l'image
    combat.create_image(8,10,image=barre)                                       #On place l'image sur le canvas 
    for i in range (1,quadrillage):                                             #Pour i allant de 1 à quadrillage (8) (afin de créer les lignes de ce dernier)
        mini_jeu.create_line(x,x*i,large-x,x*i)                                 #création des lignes horizontales du quadrillage
    for i in range (1,quadrillage):                                             #Pour i allant de 1 à quadrillage (8) (afin de créer les lignes de ce dernier)
        mini_jeu.create_line(x*i,x,x*i,large-x)                                 #création des lignes verticales du quadrillage
    for i in range (1,(quadrillage-1)):                                         #première boucle For pour la disposition des gluants
        for j in range (1,(quadrillage-1)):                                     #Seconde boucle For (une par axe x,y)
            gluant = random.choice(choix_gluant)                                #choix aléatoire du gluant à positionner
            img=ImageTk.PhotoImage(Image.open(gluant))                          #Ouverture de l'image
            mini_jeu.create_image(x*j,x*i,anchor='nw',image=img)                #On place l'image 
            l.append(img)                                                       #On rentre cette image dans la liste "l"
            if gluant == "gluants\gluant1.png":                                 #Si l'image du gluant est la première (grise)
                couleur_gluant.append(1)                                        #on ajoute 1 dans la liste couleur_gluant, cela permettra de donner une identité au gluant (cette action sera répété pour tous les gluants existants soit les 5 du jeu)
            elif gluant == "gluants\gluant2.png":                               
                couleur_gluant.append(2)                                        
            elif gluant == "gluants\gluant3.png":                               
                couleur_gluant.append(3)                                        
            elif gluant == "gluants\gluant4.png":                               
                couleur_gluant.append(4)                                        
            elif gluant == "gluants\gluant5.png":                               
                couleur_gluant.append(5)                                        
            if (len(l)) == 6 :                                                  #Si la liste l est pleine (6) car elle remplis la rangée
                images.append(l)                                                #on rentre cette liste dans la liste images afin d'obtenir 6 rangées de 6 pour pouvoir se servir des coordonées
                l = []                                                          #on réinitialise la liste "l"
            if (len(couleur_gluant)) == 6 :                                     #si la liste couleur_gluant (liste de l'identité des gluants) est pleine (6)
                liste_gluant.append(couleur_gluant)                             #on rentre cette liste dans la liste liste_gluant pour la même raison que les images
                couleur_gluant = []                                             #on reinitialise la liste couleur_gluant
            if (len(images)) == 6 :                                             #si la liste images est pleine
                img=ImageTk.PhotoImage(Image.open("images/jeu/debug.png"))                 #on ouvre une image invisible pour que le dernier gluant s'affiche
                mini_jeu.create_image(0,0,anchor='nw',image=img)                #On place cette image
                images.append(img)                                              #on l'ajoute à la liste images
                l.append(img)                                                   #et à la liste "l"
    mini_jeu.bind("<Button-1>",clic)                                            #On active la détection de clique sur la canvas mini_jeu.
    
#Cette fonction grille est le coeur du programme, c'est elle qui affiche les gluants et
#met en place les listes permettants par la suite la gestion des gluants.Elle est
#autant utile au niveau graphique pour la mise en place des boss des fond, des gluants,
#de la grille (en fonction des niveaux) qu'au niveau programme car sans elle il est
#impossible de gérer les gluants, les explosion dans la suite du programme.
    
##########################################
##############   Clique   ################
##########################################

def clic(event):
    global couleur, degat, limite_clic, bdv, vie, debug_clic, Nb_coups
    if debug_clic == True :                                                     #Si le clique est désactivé
        verif = 1                                                               #variable utilisé pour vérifier et compter toutes les cases vides (gluants explosés) et infliger des dégâts
        cad = large/quadrillage                                                 #Variable utilisé pour la position des gluants
        x = int(event.x // cad )                                                #coordoné en x en fonction du quadrillage
        y = int(event.y // cad )                                                #coordoné en y en fonction du quadrillage
        if limite_clic >= 0 :                                                   #Si il reste encore des coups à l'utilisateur
            limite_clic = limite_clic - 1                                       #il perd 1 coup (car il a cliqué)    
        if 1<=x<=6 and 1<=y<=6 :                                                #Si le clique de l'utilisateur est dans la zone des gluants
            y = y-1                                                             #Nouvelle valeur de x qui sera utilisé dans les listes qui commence à partir du terme 0 
            x = x-1                                                             #Nouvelle valeur de x qui sera utilisé dans les listes qui commence à partir du terme 0 
            couleur = liste_gluant[y][x]                                        #Identité des gluants explosés
            explosion(x,y)                                                      #On active la fonction explosion
            propagation()                                                       #Puis la fonction de propagation de cette explosion
            for i in range (0,6):                                               #Boucle for allant de 0 à 6
                for j in range (0,6):                                           #Boucle for allant de 0 à 6 Ces deux boucles permettent de vérifier toutes les cases
                    if liste_gluant[i][j] == " ":                               #Si une case est vide
                        if verif < 5 :                                          #Plus le nombre de gluants explosés en même temps est important, plus les dégâts seront importants
                            verif = verif + 0.8                                 #Les dégâts seront plus important, on ajout 1 à la variable verif    
                        elif 5 <= verif <= 10:                                  
                            verif = verif + 0.9
                        elif 10 < verif <=20 :
                            verif = verif + 1
                        else :
                            verif = verif + 1.35
            if limite_clic < 0 :                                                #Si le joueur n'a plus de coups
                degat = 0                                                       #Les dégâts restent à 0
            else :                                                              #Sinon
                degat = int(degat+((verif**2)/2)*bonus)                         #les dégats augmentent en fonction du nombre de gluants explosés et des bonus achetés dans la boutique
            combat.delete(Nb_coups)                                             #On supprime le texte de nombre de coups
            Nb_coups = combat.create_text(25,10,text='Coups :'+str(limite_clic))             #On le recréer juste après avec la nouvelle valeur
            bdv = 30 + degat // (pts_de_vie/140)                                #On fait chuter la barre de vie en fonction des dégâts.
            if bdv > 170 :                                                      #Si la barre de vie est terminée
                bdv = 170                                                       #Elle reste vide et ne continue pas en se remplissant à l'envers, en dehors de son cadre
            combat.delete(vie)                                                  #On supprime la barre de vie
            vie = combat.create_rectangle(245.5, 170, 255.5, int(bdv), fill="red", width=0)         #Pour la recréer avec les nouvelles coordonés et donc la faire diminuer
            combat.tag_raise(vie)                                               #On redonne sa priorité à la barre de vie
            chute()                                                             #On lance : la fonction de chute
            remplacement()                                                      #Celle de remplacement des gluants explosés
            move_boss()                                                         #L'animation du boss lorsqu'il prend des dégâts    
            ch_niveau()                                                         #La fonction changement de niveau qui lance le second mini-jeu    
            perdu()                                                             #Puis la fonction perdu qui verifie si l'utilisateur a perdu ou non

#La fonction clique permet de gérer tous ce qu'il se passe lors d'un clique.
#Elle renvoie principalement vers d'autres fonction mais a aussi quelques rôles
#à jouer tel que celui des dégâts ou de la barre de vie. C'est aussi elle qui
#récupère la couleur des gluants explosés. Elle intervient à chaque clique 
#lorsque ce dernier est activé
            
##########################################
##########    Explosion    ###############
##########################################

def bulle(x,y):
    global timer, fraguement1, fraguement2, fraguement3, fraguement4, quadrillage, haut, debug_clic
    multi = haut / quadrillage                                                  #Utilisé pour les coordonés
    if timer == 0 :                                                             #Si le timer vient de commencer    
        fraguement1 = mini_jeu.create_image((x+1.5)*multi,(y+1.5)*multi ,image=goutte)          #On place les 4 fraguements qui se disperseront chacun dans un sens
        fraguement2 = mini_jeu.create_image((x+1.5)*multi,(y+1.5)*multi ,image=goutte)
        fraguement3 = mini_jeu.create_image((x+1.5)*multi,(y+1.5)*multi ,image=goutte)
        fraguement4 = mini_jeu.create_image((x+1.5)*multi,(y+1.5)*multi ,image=goutte)
        timer = timer+1                                                         #Le timer augmente de 1
        debug_clic = False                                                      #On interdit le clique        
        stop_bulle(x,y)                                                         #On lance l'autre fonction qui verifie si le timer est fini
    else :                                                                      #Sinon    
        mini_jeu.tag_raise(fraguement1)                                         #On passe les 4 fraguements au premier plan (prioritaires par rapport aux autres images)
        mini_jeu.tag_raise(fraguement2)
        mini_jeu.tag_raise(fraguement3)
        mini_jeu.tag_raise(fraguement4)
        mini_jeu.move(fraguement1, 0, 7)                                        #Bouge les 4 fraguements dans des directions opposées    
        mini_jeu.move(fraguement2, 0, -7)
        mini_jeu.move(fraguement3, 7, 0)
        mini_jeu.move(fraguement4, -7, 0)   
        timer = timer+1                                                         #Le timer augmente de 1
        stop_bulle(x,y)                                                         #On lance l'autre fonction qui verifie si le timer est fini
        
#Cette fonction a pour but la création et le déplacement des fraguements
    
def stop_bulle(x,y):
    global timer, fraguement1, fraguement2, fraguement3, fraguement4, debug_clic
    if  timer < 20 :                                                            #Si le timer est inferieur à 20, qu'on a déplacé les boules moins de 20 fois
        fenetre.after(20,lambda : bulle(x,y))                                   #On relance la fonction bulle après 0.02 secondes    
    else :                                                                      #Sinon (si le timer est écoulé, que l'animation est finie)
        mini_jeu.delete(fraguement1)                                            #Suppression des 4 fraguements    
        mini_jeu.delete(fraguement2)
        mini_jeu.delete(fraguement3)
        mini_jeu.delete(fraguement4)
        timer = 0                                                               #Le timer est réinitialisé
        debug_clic = True                                                       #On réactive le clique
        
#Cette fonction vérifie que le timer n'est pas fini et relance l'animation avec 
#un léger temps d'attente

def explosion(x,y):
    global liste_gluant, images
    for j in range (0,4):                                                       #Boucle for qui se répète 4 fois pour les 4 directions
        try :                                                                   #On essaie de réalisé un morceau de code    
            for i in range (0,4):                                               #Boucle for allant de 0 à 4
                if couleur == liste_gluant[y][x-1]:                             #Si la couleur correspond avec celle du gluant de la case adjacente
                    liste_gluant[y][x-1] = " "                                  #On remplace l'identité par un espace (on la supprime)    
                    images[y][x-1] = " "                                        #De même pour l'image
        except IndexError:                                                      #Si le terme de la liste n'est pas valide
            None                                                                #Il ne se passe rien, il n'y a pas d'erreur    
        try :                                                                   #On refait de même pour les 4 gluants adjacents donc les 4 direction (haut droite bas gauche)
            for i in range (0,4):
                if couleur == liste_gluant[y][x+1]:
                    liste_gluant[y][x+1] = " "
                    images[y][x+1] = " "
        except IndexError:
            None
        try :
            for i in range (0,4):
                if couleur == liste_gluant[y-1][x]:
                    liste_gluant[y-1][x] = " "
                    images[y-1][x] = " "
        except:
            explosion(x,y)
        try :
            for i in range (0,4):
                if couleur == liste_gluant[y+1][x]:
                    liste_gluant[y+1][x] = " "
                    images[y+1][x] = " "
        except IndexError:
            None
    liste_gluant[y][x] = " "                                                    #On supprime l'identité du gluant de base
    images[y][x] = " "                                                          #De même pour son image
    
#Cette fonciton permet la première explosion, par la suite c'est la fonction de 
#propagation qui supprimera les autres gluants adjacents

##########################################
##########   animation du boss    ########
##########################################

def move_boss():
    global var_y,var_x
    if var_x<14:                                                                #Si le boss a bougé moins de 14 fois
        if var_y<0:                                                             #Si ses coordonées verticales sont basses
            combat.move(exex, 0, 10)                                            #On fait bouger le boss vers le haut
            fenetre.after(50,move_boss)                                         #Apres 0.05 secondes on rejoue la fonction (pour créer l'animation)       
            var_y=var_y+1                                                       #Ses coordonées verticales (propre à la fonction) augmentent de 1
            var_x=var_x+1                                                       #Le nombre de mouvements augmente de 1
        else:                                                                   #Sinon    
            combat.move(exex, 0, -10)                                           #On fait bouger le boss vers le bas
            var_y=var_y-1                                                       #Ses coordonées verticales (propre à la fonction) diminuent de 1
            fenetre.after(50,move_boss)                                         #Apres 0.05 secondes on rejoue la fonction (pour créer l'animation)    
            var_x=var_x+1                                                       #Le nombre de mouvements augmente de 1
    else :                                                                      #Sinon
        var_y = 0                                                               #On réinitialise ses coordonées
        var_x = 0                                                               #On réinitialise le nombre de mouvements
    
#Cette fonction permet de faire "souffrir" le boss. Pour ce faire elle le fait
#tout simplement trembler légerement de haut en bas
        
##########################################
##########   Propagation    ##############
##########################################

def propagation():
    for a in range (0,6):                                                       #Première boucle for permettant de faire 6 fois le tour des cases si jamais un gluant a été supprimé tout en bas, il faudra le faire remonter plusieurs fois    
        for i in range (0,6):                                                   #Seconde boucle for pour parcourir toutes les rangées
            for j in range (0,6) :                                              #Troisième boucle for pour parcourir les 6 gluants d'une rangée
                if liste_gluant[i][j] == " ":                                   #Si le gluant à ces coordonées à été explosé (supprimé)
                    explosion(j,i)                                              #On lance la propagation de l'explosion à partir de ces coordonées
                    if verif_bulle == True :                                    #Si les animations sont activés    
                        aleatoire = random.choice([True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False])           #Une chance sur 20 que l'animation se produise
                        if aleatoire == True :                                  #Si la variable aléatoir renvoie True (1 chance sur 20)
                            bulle(j,i)                                          #On lance l'animation 
                            
#Cette fonction a pour but de lancer la propagation de l'explosion et de lancer 
#les animation uniquement 1 fois sur 20 en moyenne afin d'alléger le programme
                    
##########################################
##############   Chute    ################
##########################################

def chute():
    global images, liste_gluant
    dim = large/quadrillage                                                     #Variable utile pour les coordonées dans le quadrillage                                                      
    for i in range (0,36):                                                      #Première boucle for ayant pour but de faire plusieurs fois le tou de toutes les cases afin d'être sur que les gluants soient tous tombés     
        for x in range (0,6):                                                   #Seconde boucle for pour vérifier toutes les rangées
            for y in range (1,6):                                               #Troisième boucle for qui vérifie tous les gluants de la rangée    
                if liste_gluant[y][x] == " ":                                   #si le gluant a été détruit
                    liste_gluant[y][x] = liste_gluant[y-1][x]                   #On descend l'identité de celui du dessus  
                    liste_gluant[y-1][x] = " "                                  #et on la supprimeuniquement pour le gluant de dessus  
                    if liste_gluant[y][x] == 1 :                                #Si le gluant a pour identité 1
                        img=ImageTk.PhotoImage(Image.open("gluants\gluant1.png"))                   #On ouvre l'image correspondant à cette identité
                        mini_jeu.create_image(dim*(x+1),dim*(y+1),anchor='nw',image=img)            #On place l'image aux bonnes coordonées
                        images[y][x] = img                                                          #On rentre l'image dans la liste pour ne pas qu'elle disparaisse
                        images[y-1][x] = " "                                                        #On fait disparaitre l'image du dessus
                    elif liste_gluant[y][x] == 2 :                                                  #On vérifie pour chaque identité, le procédé est le même        
                        img=ImageTk.PhotoImage(Image.open("gluants\gluant2.png"))
                        mini_jeu.create_image(dim*(x+1),dim*(y+1),anchor='nw',image=img)
                        images[y][x] = img
                        images[y-1][x] = " "
                    elif liste_gluant[y][x] == 3 :
                        img=ImageTk.PhotoImage(Image.open("gluants\gluant3.png"))
                        mini_jeu.create_image(dim*(x+1),dim*(y+1),anchor='nw',image=img)
                        images[y][x] = img
                        images[y-1][x] = " "
                    elif liste_gluant[y][x] == 4 :
                        img=ImageTk.PhotoImage(Image.open("gluants\gluant4.png"))
                        mini_jeu.create_image(dim*(x+1),dim*(y+1),anchor='nw',image=img)
                        images[y][x] = img
                        images[y-1][x] = " "
                    elif liste_gluant[y][x] == 5 :
                        img=ImageTk.PhotoImage(Image.open("gluants\gluant5.png"))
                        mini_jeu.create_image(dim*(x+1),dim*(y+1),anchor='nw',image=img)
                        images[y][x] = img
                        images[y-1][x] = " "

#Tel que son nom l'indique, cette fonction a pour but de faire descendre le 
#gluant qui se situe au dessus d'une case vide dans cette case, pour ce faire, 
#On supprime tout du gluant du dessus pour le remettre sur le gluant du dessous.
                        
##########################################
##########   Remplacement    #############
##########################################

def remplacement():
    global images, liste_gluant, niveau
    dim = large/quadrillage                                                     #Utile pour les coordonées dans le quadrillage
    for x in range (len(liste_gluant)):                                         #vérification de toutes les rangés
        for y in range (len(liste_gluant)):                                     #vérification de tous les gluants de la rangé
            if niveau < 3 :                                                     #si le niveau est inférieur à 3
                choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png"]                  #On choisit parmis les 3 premiers gluants
            elif 3 <= niveau < 6 :                                              #Si le niveau est entre 3 et 6
                choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png","gluants\gluant4.png"]            #On choisit parmis les 4 premiers gluants
            else :                                                              #Sinon
                choix_gluant = ["gluants\gluant1.png","gluants\gluant2.png","gluants\gluant3.png","gluants\gluant4.png","gluants\gluant5.png"]              #On choisit parmis les 5 gluants
            if liste_gluant[y][x] == " ":                                       #Si le gluant a été détruit, qu'il a explosé 
                gluant = random.choice(choix_gluant)                            #On tire un gluant au hasard
                img=ImageTk.PhotoImage(Image.open(gluant))                      #On ouvre l'image
                mini_jeu.create_image((x+1)*dim,(y+1)*dim,anchor='nw',image=img)                #On la place sur le canvas
                images[y][x] = img                                              #On la rentre dans la liste images afin qu'elle ne disparaisse pas
                if gluant == "gluants\gluant1.png":                             #On lance la vérification de l'identité du gluant en fonction de sa couleur et on le rentre dans la liste "liste_gluant" On vérifie chaque couleur.    
                    liste_gluant[y][x] = 1
                elif gluant == "gluants\gluant2.png":
                    liste_gluant[y][x] = 2
                elif gluant == "gluants\gluant3.png":
                    liste_gluant[y][x] = 3
                elif gluant == "gluants\gluant4.png":
                    liste_gluant[y][x] = 4
                elif gluant == "gluants\gluant5.png":
                    liste_gluant[y][x] = 5
                    
#Cette fonction permet de remplacer tous les espaces laissés vides par des 
#gluants aléatoires choisient en fonction des niveaux.

##########################################
##############  Boutique  ################
##########################################

def shop():                                                                     #Fonction cérant la boutique
    global shoop, money, Fermer, boutique_verif, boutique, buy1, buy2, buy3, buy4
    global achete_1, achete_2, achete_3, achete_4
    global piece,piece_or,epee0,epee,epee2,potion,potion1,mana,mana1,loterie,loterie1,epuise,epuise1,epuise2,epuise3,epuise4
    global vendeur,vendeur1,shopbackground,shopbackground1,price1,price2,price3,price4,gold
    global gold1,gold2,gold3,gold4,speech_bubble,speech_bubble1,def1,def2,def3,def4,def1_2,def2_2,def3_2,def4_2
    boutique_verif = True                                                       #On définie la boutique comme ouverte
    shoop=tk.Canvas(fenetre,width=large,height=haut*2-100,)                     #On crée le canvas de la boutique
    shoop.grid(row=1, column=24,rowspan=20)                                     #On place ce canvas
    Fermer =tk.Button(fenetre, text='Fermer', command=close)                    #On crée un boutton fermer
    Fermer.place(x=425,y=505)                                                   #On place ce boutton
    shopbackground = Image.open('images/bg/shopbackground.jpg')                           #On importe la photo du fond de la boutique    
    shopbackground = ImageTk.PhotoImage(shopbackground)                         #On ouvre l'image    
    shopbackground1 = shoop.create_image(100,150,image=shopbackground)          #On place l'image
    piece = Image.open('images/shop/moneybar.png')                                          #                         
    piece = piece.resize((125,75), Image.ANTIALIAS)                             #Créartion et plaçement de l'image représentant l'argent
    piece = ImageTk.PhotoImage(piece)                                           #
    piece_or = shoop.create_image(245,16,image=piece)                           #
    vendeur = Image.open('images/shop/vendeur.png')                                         #
    vendeur = vendeur.resize((100,200), Image.ANTIALIAS)                        #Créartion et plaçement de l'image représentant le vendeur
    vendeur = ImageTk.PhotoImage(vendeur)                                       #
    vendeur1 = shoop.create_image(100,125,image=vendeur)                        #
    shoop.create_rectangle(8,220,290,495,fill='grey25',)                        #Création de rectangle de fond dans la boutique
    shoop.create_rectangle(10,225,145,350,fill='grey25',outline= 'gold',width = 3)      #Création de rectangle du fond de "Nouvelle épée"
    shoop.create_rectangle(10,365,145,490,fill='grey25',outline= 'gold',width = 3)      #Création de rectangle du fond de "Potion de mana"
    shoop.create_rectangle(155,225,285,350,fill='grey25',outline= 'gold',width = 3)     #Création de rectangle du fond de "Potion Beserk"
    shoop.create_rectangle(155,365,285,490,fill='grey25',outline= 'gold',width = 3)     #Création de rectangle de
    epee0 = Image.open('images/shop/sword1.png')                                            #
    epee = epee0.resize((35,120), Image.ANTIALIAS)                              #
    epee = ImageTk.PhotoImage(epee)                                             #
    epee2 = shoop.create_image(45,290,image=epee)                               #Création de l'image de "Nouvelle épée"
    potion = Image.open('images/shop/potion.png')                                           #
    potion = potion.resize((100,120), Image.ANTIALIAS)                          #
    potion = ImageTk.PhotoImage(potion)                                         #
    potion1 = shoop.create_image(195,290,image=potion)                          #Création de l'image de "Potion Beserk"
    mana = Image.open('images/shop/mana.png')                                               #
    mana = mana.resize((100,120), Image.ANTIALIAS)                              #
    mana = ImageTk.PhotoImage(mana)                                             #
    mana1 = shoop.create_image(50,425,image=mana)                               #Création de l'image de "Potion de Mana"
    loterie = Image.open('images/shop/loterie.png')                                         #
    loterie = loterie.resize((90,100), Image.ANTIALIAS)                         #
    loterie = ImageTk.PhotoImage(loterie)                                       #
    loterie1 = shoop.create_image(200,440,image=loterie)                        #Création de l'image de "loterie"
    price1 = shoop.create_text(110,310,text='600',fill='white')                 #affichages du prix pour "Nouvelle épée"
    price2 = shoop.create_text(255,450,text='200',fill='white')                 #affichages du prix pour "Loterie"
    price3 = shoop.create_text(110,450,text='150',fill='white')                 #affichages du prix pour "Potion de Mana"
    price4 = shoop.create_text(255,310,text='300',fill='white')                 #affichages du prix pour "Potion Beserk"
    gold = Image.open('images/shop/piece_or.png')                                           #
    gold = gold.resize((15,15), Image.ANTIALIAS)                                #
    gold = ImageTk.PhotoImage(gold)                                             #Création de l'image représentant l'argent dans le jeu(piece d'or a coté du prix)
    gold1 = shoop.create_image(130,310,image=gold)                              #
    gold2 = shoop.create_image(275,450,image=gold)                              #
    gold3 = shoop.create_image(130,450,image=gold)                              #
    gold4 = shoop.create_image(275,310,image=gold)                              #
    speech_bubble = Image.open('images/jeu/rounded-rectangle.png')                         #
    speech_bubble = speech_bubble.resize((180,90), Image.ANTIALIAS)             #
    speech_bubble = ImageTk.PhotoImage(speech_bubble)                           #
    speech_bubble1 = shoop.create_image(200,125,image=speech_bubble)            #Affichage du carrer dèrierre le texte du Vendeur
    paroles()                                                                   #Fonction "Paroles()"qui affiche le texte du Vendeur
    def1 = shoop.create_text(100,240,text='Nouvelle épée',fill='white',font =helv362)                                                       #Affichage du texte décrivant les item et leurs caractéristiques
    def1_2 = shoop.create_text(100,260,text='Augmente vos\n dégâts, ils sont\n multipliés par 2',fill='white',font =helv363)                #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def2 = shoop.create_text(100,375,text="Potion de Mana",fill='white',font =helv362)                                                      #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def2_2 = shoop.create_text(103,400,text="Vous rend de l'énergie\n et permet 20 coups\n supplémentaire",fill='white',font =helv363)      #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def3 = shoop.create_text(240,240,text='Potion Beserk',fill='white',font =helv362)                                                       #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def3 = shoop.create_text(245,260,text='Enragé vos degats\n sont multipliés\n par 2',fill='white',font =helv363)                         #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def4 = shoop.create_text(220,380,text='Loterie du marchand',fill='white',font =helv362)                                                #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def4_2 = shoop.create_text(250,395,text='Quitte ou double',fill='white',font =helv363)                                                  #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    epuise = Image.open('images/shop/outofstock.png')                                      #     
    epuise = epuise.resize((150,125), Image.ANTIALIAS)                         # 
    epuise = ImageTk.PhotoImage(epuise)                                        #Incorporation de l'image "stock epuise" a une variable 
    if achat1 == True :
        buy1=tk.Button(shoop, text='Acheter',bg='red4',fg='gold', command=bcp_plus_de_degats)      #Création du bouton pour acheter "Nouvelle épée"
        buy1.place(x=92,y=320)
    if achat1==False:
        epuise1 = shoop.create_image(80,290,image=epuise)                                          #Affichage de l'image "Stock epuise" si l'objet est deja acheter 
    
    buy2=tk.Button(shoop, text='Acheter',bg='red4',fg='gold', command=lot)                #Création du bouton pour acheter "Loterie" 
    buy2.place(x=232,y=460)
    if achat3 == True :
        buy3=tk.Button(shoop, text='Acheter',bg='red4',fg='gold', command=plus_de_coups)           #Création du bouton pour acheter "Potion de Mana" 
        buy3.place(x=92,y=460)
    if achat3==False:
        epuise3 = shoop.create_image(80,425,image=epuise)                                          #Affichage de l'image "Stock epuise" si l'objet est deja acheter  
    if achat4 == True :
        buy4=tk.Button(shoop, text='Acheter',bg='red4',fg='gold', command=plus_de_degats)          #Création du bouton pour acheter "Poition Beserk"     
        buy4.place(x=232,y=320)    
    if achat4==False:
        epuise4 = shoop.create_image(225,425,image=epuise)                                         #Affichage de l'image "Stock epuise" si l'objet est deja acheter 
    money = shoop.create_text(250,18,text=str(argent),fill='white')                                #Affichage de l'argent du joueur    
    boutique.destroy()                                                         #Destruction du bouton "Boutique" quand la Boutique en elle meme apparait 

def plus_de_coups():                                                           #Fonction pour l'achat de la "Potion de Mana" 
    global achat3, argent, limite_clic
    if argent >= 150 :                                                         #l'argent du joueur dois etre suppérieur au prix de l'item     
        argent = argent - 150
        achat3 = False                                                         #changement de boléen car l'item a été acheter  
        limite_clic = limite_clic + 20                                         #Ajout des coups Acheté 
        buy3.destroy()                                                         #l'objet ne peut que etre acheter une seul fois donc le bouton se détruit apres l'achat 
        close()                                                                #La boutique se ferme automatiquement apres l'achat 

def plus_de_degats():                                                          #Fonction pour l'achat de la "Potion Beserk" 
    global achat4, argent, bonus
    if argent >= 300 :                                                         #l'argent du joueur dois etre suppérieur au prix de l'item                                                             
        argent = argent - 300                                                  # 
        bonus =  bonus * 2                                                     #Ajout des degats acheté(multiplié par 2) 
        achat4 = False                                                         #changement de boléen car l'item a été acheter 
        buy4.destroy()                                                         #l'objet ne peut que etre acheter une seul fois donc le bouton se détruit apres l'achat  
        close()                                                                #La boutique se ferme automatiquement apres l'achat                         

def bcp_plus_de_degats():                                                      #Fonction pour l'achat de la "Nouvelle épée" 
    global achat1, argent, bonus
    if argent >= 600 :                                                         #l'argent du joueur dois etre suppérieur au prix de l'item  
        argent = argent - 600                                                  #         
        bonus = bonus * 3                                                      #Ajout des degats acheté(multiplié pas 3) 
        achat1 = False                                                         #changement de boléen car l'item a été acheter 
        buy1.destroy()                                                         #l'objet ne peut que etre acheter une seul fois donc le bouton se détruit apres l'achat      
        close()                                                                #La boutique se ferme automatiquement apres l'achat     

def lot():                                                                     #Fonction pour l'achat de la "Loterie" 
    global argent
    if argent >= 200:                                                          #l'argent du joueur dois etre suppérieur au prix de l'item      
        tirage = random.choice(["gagne","perdu"])                              #Prise aléatoire          
        if tirage == "gagne":
            argent = argent * 2                                                #     
        elif tirage == "perdu":
            argent = 0                                                         # 
        close()                                                                #La boutique se ferme automatiquement apres l'achat  
        
def close():                                                                   #Fonction pour l'achat de la fermeture de la Boutique     
    global boutique, boutique_verif,lettre,place
    boutique_verif = False                                                     # 
    Fermer.destroy()                                                           #     
    shoop.destroy()                                                            #         
    boutique=tk.Button(fenetre, text='Boutique',command=shop)                  #Quand la Boutique se ferme le bouton pour ouvrire la boutique se recrée 
    boutique.place(relx=.750,rely=.950)                                        # 
    lettre=0                                                                   #réinitialisation des variable du texte du vendeur 
    place=125                                                                  #""""""""""""""""""""""""""""""""""""""""""""""""" 
    
def paroles():                                                                                                               #Fonction de l'affichage du texte du Vendeur               
    global lettre,speech,place,point1,point2,point3
    liste1=['U','n',' ','a','c','h','a','t',' ','j','e','u','n','e',' ','a','v','e','n','t','u','r','i','e','r','?']         #Liste qui est composé du texte du vendeur   
    if boutique_verif == True:                                                                                               #   
        if lettre <=25:                                                                                                      #écriture du texte avec un éspace de 6 pixels entre les lettres   
            speech = shoop.create_text(place,115,text=str(liste1[lettre]),fill='white',font =helv36)
            place=place+6
            lettre=lettre+1
            fenetre.after(50,paroles)                                                                                         #La fionction se réactive       
        if lettre==26:                                                                                                        #Affichage des trois points sous le texte du vendeur  
            point1 = shoop.create_text(190,130,text='.',fill='white',font =helv36)
            point2 = shoop.create_text(196,130,text='.',fill='white',font =helv36)
            point3 = shoop.create_text(202,130,text='.',fill='white',font =helv36)
            lettre=lettre+1
            fenetre.after(50,paroles)

        
##############################################################################
#############################  Gluant sauvage  ###############################
##############################################################################

def jeu2():
    global Cube, mini_jeu2, imgg, start_jeu2, sec, tps, photo, vitesse
    fenetre.unbind("<Button-1>")                                                #désactivation de la détection de clique 
    imgg = []                                                                   #Création d'une variable utilisée pour conserver l'image du gluant
    vitesse = 8*(3 * (niveau*1.2))                                              #Définition de la vitesse du gluant en fonction du niveau
    start_jeu2 = True                                                           #On définie le second mini-jeu comme en route
    sec = 24 - niveau*2                                                         #Définition du temps impartie en fonction du niveau
    mini_jeu2 = tk.Canvas(fenetre, width = 300, height = 300)                   #Création du canvas 
    mini_jeu2.grid(row=20,column=2,columnspan=10, rowspan=10)                   #Affichage du canvas
    if niveau < 3 :                                                             #Si le niveau est inférieur à 3
        im = Image.open('images/bg/fond.jpg')                                             #Importation de l'image de fond sous le thème "nature", "forêt"
        photo=ImageTk.PhotoImage(im)                                            #Ouverture de l'image    
        mini_jeu2.create_image(0,0,anchor='nw',image=photo)                     #Affichage de l'image de fond
    elif 3 <= niveau < 6 :                                                      #Si le niveau du joueur est compris entre 3 et 6
        im = Image.open('images/bg/lave.jpg')                                             #Importation de l'image de fond sous le thème du "feu"
        photo=ImageTk.PhotoImage(im)                                            #Ouverture du fond 
        mini_jeu2.create_image(0,0,anchor='nw',image=photo)                     #Affichage de l'image de fond 
    else :                                                                      #Sinon
        im = Image.open('images/bg/ciel.jpg')                                             #Importation de l'image de fond sous le thème de l'"air"
        photo=ImageTk.PhotoImage(im)                                            #Ouverture du fond
        mini_jeu2.create_image(0,0,anchor='nw',image=photo)                     #Affichage de l'image
    tps=tk.Label(fenetre, text="Temps : "+str(sec))                             #On crée un texte contenant le temps restant 
    tps.grid(row=31,column=4)                                                   #On affiche ce texte
    imggg=ImageTk.PhotoImage(Image.open("gluants\gluant1.png"))                 #On ouvre l'image du gluant gris
    Cube = mini_jeu2.create_image(coord_x,coord_y,anchor='nw',image=imggg)      #On la place au milieu du canvas
    imgg.append(imggg)                                                          #On sauvegarde l'image
    deplacement()                                                               #Lancement de la fonction deplacement 
    temps()                                                                     #Lancement de la fonction temps
    fenetre.bind("<Button-1>",clic2)                                            #On active la détection de clique sur la fenêtre

#Cette fonction sert au démarrage du second mini-jeu. Elle met en place un
#certain nombre de variable tel que la vitesse, le temps restant et s'occupe
#de la mise en place du design du mini-jeu (fond, gluant)
    
def deplacement():
    global coord_x, coord_y, dif_x, dif_y, r, Cube, imgg
    if coord_x+r+dif_x > large:                                                 #Si le gluant touche la bordure droite
        coord_x = 2*(large-r)-coord_x                                           #On affecte les nouvelles coordonnés en x  
        dif_x = -dif_x                                                          #On choisit le sens de mouvement du gluant
    if coord_x-r+dif_x < 0:                                                     #Si le gluant touche la bordure gauche 
        coord_x = 2*r-coord_x                                                   #On affecte les nouvelles coordonnés en x 
        dif_x = -dif_x                                                          #On choisit le sens de mouvement du gluant
    if coord_y+r+dif_y > haut:                                                  #Si le gluant touche la bordure haute
        coord_y = 2*(haut-r)-coord_y                                            #On affecte les nouvelles coordonnés en x 
        dif_y = -dif_y                                                          #On choisit le sens de mouvement du gluant
    if coord_y-r+dif_y < 0:                                                     #Si le gluant touche la bordure droite
        coord_y = 2*r-coord_y                                                   #On affecte les nouvelles coordonnés en x 
        dif_y = -dif_y                                                          #On choisit le sens de mouvement du gluant
    coord_x = coord_x+dif_x                                                     #On affecte les nouvelles coordonnées en x
    coord_y = coord_y+dif_y                                                     #On affecte les nouvelles coordonnées en y
    if sec > 0 :                                                                #Si le temps n'est pas écoulé
        fenetre.after(100,deplacement)                                          #On lance la fonction déplacement
        imgg = []                                                               #On supprime l'image du gluant 
        imggg=ImageTk.PhotoImage(Image.open("gluants\gluant1.png"))             #On ouvre l'image du gluant
        Cube = mini_jeu2.create_image(coord_x,coord_y,image=imggg)              #On replace le gluant aux nouvelles coordonées 
        imgg.append(imggg)                                                      #On enrgistre l'image du nouveau gluant
        
#Fonction de déplacement du gluant, son rôle est de modifier ses coordonées
#et de le replacer aux nouvelles
        
def temps():
    global sec, tps, start_jeu2
    sec = sec - 1                                                               #diminution du temps impartie
    if sec > 0:                                                                 #Si il reste du temps à l'utilisateur
        tps.config(text="Temps : "+str(sec))                                    #On met à jour l'affichage du temps restant
        fenetre.after(1000,temps)                                               #On relance la fonction temps après 1 seconde afin de mettre à jour le temps restant        
    elif sec == 0:                                                              #Si le joueur n'a plus de temps
        tps.destroy()                                                           #On supprime le texte donnant le temps
        sec = -1                                                                #Le timer est réglé sur -1 pour éviter des bugs avec la fonction temps
        start_jeu2 = False                                                      #Le second mini-jeu est définie comme éteint  
        ch_niveau2()                                                            #On lance la fonction de changement de niveau
    
#Fonction mettant à jour le minuteur et vérifiant que ce dernier n'est pas terminé
        
def clic2(event):
    global limite_clic, sec, start_jeu2
    x1 = int(event.x)                                                           #coordonnées en x
    y1 = int(event.y)                                                           #coordonnées en y
    if start_jeu2 == True :                                                     #Si le deuxième mini-jeu est lancé    
        if coord_x - r < x1 < coord_x + r and coord_y - r < y1 < coord_y + r :          #Si le clic est sur le gluant
            limite_clic = limite_clic + 10                                      #On augmente la limite de clique de 10
            sec = -1                                                            #Le timer est réglé sur -1 pour éviter des bugs avec la fonction temps
            tps.destroy()                                                       #On détruit le texte du minuteur
            start_jeu2 = False                                                  #Le second mini-jeu est définie comme éteint
            ch_niveau2()                                                        #On lance la fonction changement de niveau
            
#Fonction amené lors d'un clique, elle a pour but de vérifier que l'utilisateur
#Clique bien sur le gluant et si oui d'engendre le changement de niveau.

##########################################
###########  lancement  ##################
##########################################

fenetre.mainloop()