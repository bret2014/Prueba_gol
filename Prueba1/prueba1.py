# Importamos la librería
import pygame
from tkinter import*

import sys

# Creamos un reloj
Reloj= pygame.time.Clock()


# Importamos constantes locales de pygame
from pygame.locals import *

# Iniciamos Pygame
pygame.init()

# Creamos una surface (la ventana de juego), asignándole un alto y un ancho
Ventana = pygame.display.set_mode((1200, 956))

# Le ponemos un título a la ventana
pygame.display.set_caption("Mete gol")

# Cargamos las imágenes
Fondo = pygame.image.load("fondo.jpg")
Imagen = pygame.image.load("balon.png")
Arco = pygame.image.load("arco.jpg")

coordX = 0
coordY = 200

coordX1 = 600
coordY1 = 200

Coordenadas = (coordX, coordY)

Coordenadas2 = (coordX1, coordY1)


incrementoX = 0
incrementoY = 0

cont=0

# Bucle infinito para mantener el programa en ejecución
while True:

    Ventana.blit(Fondo, (0, 0))
    Ventana.blit(Imagen, Coordenadas)
    Ventana.blit(Arco, Coordenadas2)
    pygame.display.flip()

   # Manejador de eventos
    for evento in pygame.event.get():
        # Pulsación de la tecla escape
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                sys.exit()
            elif evento.key == pygame.K_RIGHT:
                incrementoX = 5
                cont=cont+5
                print(cont)
            elif evento.key == pygame.K_LEFT:
                incrementoX = -5
                cont=cont-5
                print(cont)
        if cont > 170:
            print("Gano")
            root=Tk()
            etiqueta1=Label(root,text="Usted a metido un gol")
            etiqueta1.pack()
            root.mainloop()
            exit()
                
        if evento.type == pygame.KEYUP:
            incrementoX = 0
            incrementoY = 0

    coordX = coordX + incrementoX
    coordY = coordY + incrementoY

    Coordenadas = (coordX, coordY)
