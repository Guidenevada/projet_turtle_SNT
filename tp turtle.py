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

    le programme est doit se lancer avec 4 possibilitées : 0 le programme ne se lance pas
                                                           1 il execute la fonction main1()
                                                           2 il execute la fonction main2()
                                                           3 il execute la fonction main3()





"""
# importation des biibliothèques




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
long = screensize[0]              
haut = screensize[1]
middle = long /2, haut /2
spd = 2
r = randint(0, 255)
g = randint(0, 255)                             
b = randint(0, 255)
ray = 50

tt.speed(0)
tt.colormode(255)
#*****************************************************************************************************************


def setscreen(long, haut): # on définit la taille de l'écran
    tt.setup(long, haut, 0, 0) # on définit la taille de l'écran 
    tt.setworldcoordinates(0, 0, long, haut) # on définit la taille de l'écran




def setpos(coo): # on définit la position de la tortue sans ecrire avec le crayon
    tt.penup()
    tt.goto(coo)
    tt.pendown()



def squareandcircle(ray):
   
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

def triangle(segment):
    for i in range(3):
        tt.forward(segment)
        tt.left(120)

def main2(ray):
    ray = ray + 1
    setpos((0,0))
    tt.forward(long /2)
    tt.left(90)
    tt.forward(haut /2)
    tt.color("red")
    tt.circle(ray)
    tt.color("black")
    tt.forward(haut /2)
    tt.left(180)
    tt.forward(haut /2)
    tt.right(90)
    tt.forward(ray)



def main3(ray):
    segment = ray
    angle = 360
    setpos(middle)
    tt.begin_fill()
    triangle(segment)
    tt.end_fill()
    for i in range(5):
        angle = 120
        tt.circle(ray, angle)
        ray = ray + ray / 2
    tt.forward(ray)
    setpos(middle)
    tt.forward(ray /2)
    tt.left(90)
    tt.forward(haut / 2)
    tt.left(90)
    tt.forward(long /3)
    tt.left(90)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tt.pencolor((r, g, b))
    tt.forward(ray)
    tt.right(90)
    tt.forward(long /3)
    tt.left(180)
    tt.forward(long /3)
    tt. left(35)
    tt.forward(long /2)

    tt.done()
    






def main1(ray):

    setpos(middle) # on définit la position de la tortue au milieu de l'écran    
    squareandcircle(ray)
    setpos(middle)
    tt.begin_fill()
    triangle(100)
    tt.end_fill()
    tt.done()

if __name__ == '__main__': # on lance le programme
    setscreen(long, haut)
    tt.reset()
    ch = randint(0,3) # on choisit un nombre aléatoire entre 1 et 3 pour lancer un programme aléatoire
    print("tirage au sort")
    sleep(0.5)
    print("le nombre tiré est ",ch)
    if ch == 1:
        main1(ray)
    if ch == 2:
        main2(ray)
    if ch == 3:
        main3(ray)  
    else:
        print("pas de chance, vous avez tiré le mauvais nombre")

    tt.exitonclick()
    
     # on ferme la fenêtre
#************************************************************************************************************************