from tkinter import *               #Importer les bon outils
from random import randint


nb = 0                              #Definir le nombre de tour
a=randint(1,10)                     #Choisir la place du baton pour le premier tour
b=randint(1,10)
global drapeau                      #Globaliser le drappeau pour la boucle
drapeau=0                           #Remettre la boucle à zéro

def tour():                         #Fonction pour afficher le nombre de tours
    global nb
    nb = nb+1                           #Permettre à chaque evenement ajouter 1 au numéo
    Texte.set('Tours n° ' + str(nb))    #Afficher les tours

def Nouveaulance():                     #fonction pour Rénitialiser le jeu
    global a,b
    global drapeau
    global nb
    nb=0
    tour()
    a=randint(1,10)
    b=randint(1,10)
    drapeau=0
    Canevas.create_image(0,0,anchor=NW, image=photo)        #Reafficher la fenetre tèl quel


def Clic(event):                                                        #Crée l'evenement graphique
    """ Gestion de l'événement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    global drapeau
    if drapeau==0:

        Xpixels = event.x                               #Definir l'evenement pour les calculs
        Ypixels = event.y

        xcase = int((Xpixels-30)/52)+1                  #Trouver le numéro de la case

        xcentre = (xcase-1)*52+(30+52/2)
                                                            # x pour horizontal et y pour vertical
        ycase = int((Ypixels-20)/53)+1

        ycentre = (ycase-1)*53+(20+53/2)                #Placé au centre de la case l'evenement


        # on dessine un carré
        r = 25                                              # Rayon du carré


        if xcase==a and  ycase==b:                          # Definition pour le bateau

            Texte2.set('Coulé')                             #Afficher la caractéristique de curré en fonction du bateau
            Canevas.create_rectangle(xcentre-r, ycentre-r, xcentre+r, ycentre+r, outline='black',fill='red')      #Afficher la couleur et l'emplacement du carré la où l'on clique en fonction de la caractéristique du bateau
            tour()                                              #afficher la definition tour
            drapeau=1



        elif (xcase==a-1 or xcase==a or xcase==a+1) and (ycase==b-1 or ycase==b or ycase==b+1):
            Texte2.set('Touché')
            Canevas.create_rectangle(xcentre-r, ycentre-r, xcentre+r, ycentre+r, outline='black',fill='orange')
            tour()

        elif xcase==a or ycase==b:

                Texte2.set('En vue')
                Canevas.create_rectangle(xcentre-r, ycentre-r, xcentre+r, ycentre+r, outline='black',fill='yellow')
                tour()
        else:
            Texte2.set("A l'eau")
            Canevas.create_rectangle(xcentre-r, ycentre-r, xcentre+r, ycentre+r, outline='black',fill='blue')
            tour()

Mafenetre = Tk()
Mafenetre.title("Bataille Navale")

Mafenetre.geometry('700x550+200+200')





Boutonlance =Button(Mafenetre, text ='Nouveau lancé',fg = 'White',bg="Black",command = Nouveaulance,activebackground="red",font = 5,activeforeground="blue",relief = "groove",height= 2)
Boutonlance.grid(row=2,column=1)

BoutonQuitter =Button(Mafenetre, text ='Quitter',fg = 'White',bg="Black",command = Mafenetre.destroy,activebackground="red",font = 5,activeforeground="blue",relief = "groove",height= 2)
BoutonQuitter.grid(row=3,column=1)

Texte = StringVar()


Labeltour = Label(Mafenetre, textvariable = Texte, fg ='White', bg ='Gray',font = 5,height= 2)
Labeltour.grid(row=0,column=1)

Texte2 = StringVar()

LabelResultat = Label(Mafenetre, textvariable = Texte2, fg ='White', bg ='Gray',font = 5,height= 2)
LabelResultat.grid(row=1,column=1)



photo = PhotoImage(file="grille.png")

Largeur = 550
Hauteur = 550
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
Canevas.bind('<Button-1>', Clic)
Canevas.grid(row=0,column=0,rowspan=4)




Mafenetre.mainloop ()