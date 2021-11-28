"""
    tuto pour Théo:
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
    setcolor() s'utilise avec les valeurs RGB
                par exemple pour une couleur rouge
                on utilise r = 255 et g = 0 et b = 0
                pour une couleur bleu
                on utilise r = 0 et g = 0 et b = 255
                pour une couleur noir
                on utilise r = 0 et g = 0 et b = 0
                pour une couleur blanc
                on utilise r = 255 et g = 255 et b = 255
    main() doit être modifié et toujours à la fin




"""
# importation des biibliothèques


import turtle as tt # importation de turtle                                                                       
import ctypes # importation de ctypes                                                                             
from time import sleep # importation de sleep                                                                     
from random import randint # importation de randint
import sys   # importation de sys
sys.path.append('__init__') # on ajoute le chemin de __init__
from dep import * # on importe une dépendance
    # setres() # on définit la taille de l'écran
    # setpos(x, y) # on définit la position de la tortue au milieu de l'écran
    # setcolor(r, g, b) # on définit la couleur de la tortue







def main():
    tt.reset()
    dep.setres() # on définit la taille de l'écran
    dep.setpos(x, y) # on définit la position de la tortue au milieu de l'écran
    
    tt.done()

if __name__ == '__main__': # on lance le programme
    main() # on lance la fonction main
    tt.exitonclick() # on ferme la fenêtre