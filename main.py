import sys
import pygame
from pygame.constants import K_RIGHT
from pelota import BallCharacter
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("Juego BALl")
# Comenzamos el bucle del juego
run = True
# Definimos los fps
clock = pygame.time.Clock()
ball = BallCharacter()
# definimos los colores que usaremos en la ventana
black = (0, 0, 0)


while run:
    clock.tick(60)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        # defino la variable que tendra los eventos que captura del teclado
        key = pygame.key.get_pressed()
        # Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False
        

    # ejecuto la funcion que cambia de posicion la pelota
    ball.move_right(screen)

    pygame.display.update()
    screen.fill(black)
    pygame.event.pump()
# Salgo de pygame
pygame.quit()
