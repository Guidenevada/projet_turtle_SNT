#*************************************//écrit par Baptiste//*******************************************************


import ctypes
import turtle as tt





def setres(): #  on définit la taille de l'écran

    user32 = ctypes.windll.user32 # user32 est une fonction de ctypes 
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) # on récupère la taille de l'écran 
    x = screensize[0]
    y = screensize[1]

    
def setpos(x, y): # on définit la position de la tortue sans ecrire avec le crayon
    tt.setup(x, y, 0, 0) # on définit la taille de l'écran 
    tt.setworldcoordinates(0, 0, x, y) # on définit la taille de l'écran
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

def setcolor(r, g, b): # on définit la couleur du crayon
    tt.pencolor(r, g, b)

    






#************************************************************************************************************************    

