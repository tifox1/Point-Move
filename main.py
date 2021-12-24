import sys
import pygame
from pygame.constants import K_RIGHT, KEYDOWN, K_d
from pelota import BallCharacter
# definimos la variable que contendra la cantidad de fps que tiene el juego
FPS = 60
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

# En esta variable se guardan los estados de las teclas: True si estan presionados y False si no lo estan
key_events = {
    'key_d': False,
    'key_a': False,
    'static': False
}


while run:
    clock.tick(FPS)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        # defino la variable que tendra los eventos que captura del teclado
        key = pygame.key.get_pressed()
        # Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False

        #captamos el evento de la tecla d
        if key[K_d]:
            key_events['key_d'] = True
        else:
            key_events['static'] = True
            key_events['key_d'] = False

        #captamos el evento de la tecla a
        if key[K_d]:
            key_events['key_a'] = True
        else:
            key_events['static'] = True
            key_events['key_a'] = False


    ball.moves(screen, key_events)
    pygame.display.update()
    screen.fill(black)
    pygame.event.pump()
# Salgo de pygame
pygame.quit()
