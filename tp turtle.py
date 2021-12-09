baptiste
#6360

[10:11] baptiste:
[10:11] Virtua:
[10:16] baptiste: https://github.com/Guidenevada/projet_turtle_SNT
GitHub
GitHub - Guidenevada/projet_turtle_SNT
Contribute to Guidenevada/projet_turtle_SNT development by creating an account on GitHub.

[10:16] baptiste:
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
Afficher plus
tp_turtle.py
6 Ko
[16:47] baptiste:
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
Afficher plus
tp_turtle.py
7 Ko
[16:48] baptiste: https://github.com/Guidenevada/projet_turtle_SNT
GitHub
GitHub - Guidenevada/projet_turtle_SNT
Contribute to Guidenevada/projet_turtle_SNT development by creating an account on GitHub.

[18:35] Virtua: Merci 😁😁
[13:47] baptiste:
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
Afficher plus
tp_turtle.py
7 Ko
[13:50] baptiste: nouvelle update, plus d'optimisation
[16:15] baptiste: mise à jour: ajout du choix de la vitesse et ajout de la vitesse par defaut
[16:15] baptiste: correction d'un bug avec la vitesse
[16:15] baptiste:
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
Afficher plus
tp_turtle.py
7 Ko
[20:31] baptiste: je vais bientot upload la version finale du TP
[20:34] Virtua: Ah oki 😁😁
[20:50] baptiste:
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
Afficher plus
tp_turtle_Yvon_Nathan_Brenet_Baptiste.py
7 Ko
﻿
"""
    tuto pour mon binome:
    setres()  ne doit pas être modifié
    setpos(x, y) s'utilise avec les coordonnées
                avec x qui est la largeur de l'écran
                et y qui est la hauteur de l'écran
                par exemple un écran de 1920x1080
                avec x = 1920 et y = 1080
                0.0 est le milieu de l'écran (x = 960, y = 540) et la tortue est placée par défaut au milieu donc à (x = 960 y = 540)
                si on veut placer la tortue en haut à gauche de l'écran
                on utilise x = 0 et y = 0 donc : setpos(0, 0)
                si on veut placer la tortue en bas à droite de l'écran
                on utilise x = 1920 et y = 1080 donc : setpos(1920, 1080)
                mais il est préférable de ne pas utiliser x = 1920 et y = 1080 mais x = setpos(screensize[0] - screensize[0] /2, screensize[1] - screensize[1] /2)
                pour que la tortue soit placée au milieu de l'écran car si on utilise un écran non standard 1920x1080, la tortue ne sera pas placée au milieu de l'écran
                ou x = screensize[0] et y = screensize[1]
                setpos(x - x / 2, y - y / 2)
                position par défault de 0,0 est en bas à gauche





"""
# importation des biibliothèques




import time
import turtle as tt # importation de turtle                                                                       
import ctypes # importation de ctypes                                                                             
from time import sleep # importation de sleep                                                                     
from random import randint # importation de randint
import sys
from typing import AsyncGenerator   # importation de sys

    # setres() # on définit la taille de l'écran
    # setpos(x, y) # on définit la position de la tortue au milieu de l'écran
    # setcolor(r, g, b) # on définit la couleur de la tortue



#*************************************//écrit par Baptiste//*******************************************************

#******************************************configuration des variables**********************************************
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1) # on récupère la taille de l'écran 
long = screensize[0]  # on définie la longueur de l'écran
haut = screensize[1] # on définie la hauteur de l'écran
middle = long /2, haut /2 # defini le milieur de l'écran
spd = 0
r = 0 
g = 0                            
b = 0   # mettre la couleur à noir
ray = 50

tt.speed(spd)
tt.colormode(255)
#*****************************************************************************************************************


def setscreen(long, haut): # on définit la taille de l'écran
    tt.setup(long, haut, 0, 0) # on définit la taille de l'écran 
    tt.setworldcoordinates(0, 0, long, haut) # on définit la taille de l'écran




def setpos(coo): # on définit la position de la tortue sans ecrire avec le crayon
    tt.penup()
    tt.goto(coo)
    tt.pendown()



def squareandcircle(ray):  # on définit la fonction qui permet de faire un carré et des cercles de plus en plus grands
   

    for i in range(4):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        tt.pencolor((r, g, b))
        tt.forward(100)
        tt.left(90)    
    for x in range(5):
        tt.penup()
        tt.goto(0, 0)
        tt.pendown()
        tt.circle(ray)
        ray = ray + ray / 2
        tt.penup()

def triangle(segment): # on définit la fonction qui permet de faire un triangle
    for i in range(3):
        tt.forward(segment)
        tt.left(120)
def square(ray): # on définit la fonction qui permet de faire un carré
        for i in range(4):
            tt.forward(ray)
            tt.right(90)



def main1(ray): #premiere frize
    setpos((long -long, haut / 3))
    
    tt.left(45)
    for i in range(25):
        
        
        tt.forward(ray)
        tt.right(90)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        tt.pencolor((r, g, b))
        tt.forward(ray)
        tt.left(90)
    setpos((long -long, haut / 2))
    tt.right(45)

def main2(ray): # 2nd frise
    setpos((long -long, haut / 2))

    for x in range(32):
        square(ray)
        triangle(ray)
        tt.forward(ray)
#*************************************************************************************************************************     
#*********************************************************// écrit par Nathan Yvon****************************************



def main3(ray):# 3 eme frize
    
    setpos((ray, haut / 1.25))
    for c in range(15):
        tt.circle(ray)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        tt.pencolor((r, g, b))
        tt.forward(100)
    setpos(middle)



    
    

def main4(ray): # 4 eme frize
    setpos((0 , 150))
    for c in range(20):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        tt.pencolor((r, g, b))
        tt.forward(ray)
        tt.right(90)
        tt.forward(ray)
        tt.left(90)
        tt.forward(ray)
        tt.left(90)
        tt.forward(ray)
        tt.right(90)
        


 


    
#**********************************************//écrit par baptiste*****************************************************
if __name__ == '__main__': # on lance le programme
    try:
        setscreen(long, haut)
        tt.reset()
        print("la vitesse par defaut est de 0")
        spd = input("Veuillez entrer la vitesse de la tortue [1-10]\n: ")
        if spd == '':
            spd = 0
        else:
            spd =int(spd)
        
        print(spd)
        tt.speed(spd)

        main1(ray)
        main2(ray)
        main3(ray)
        main4(ray)
        setpos(middle)
        for i in range(10):
            sleep(0.1)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            tt.bgcolor((r, g, b))
        tt.done()
        tt.exitonclick()
        
    
    except:
        print('Erreur')
        time.sleep(5)
        sys.exit()

     # on ferme la fenêtre
#************************************************************************************************************************
tp_turtle_Yvon_Nathan_Brenet_Baptiste.py
7 Ko
