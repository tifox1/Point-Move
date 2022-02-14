
import pygame
from pygame.constants import K_RIGHT, K_SPACE, KEYDOWN, K_a, K_d
from pelota import *
# definimos la variable que contendra la cantidad de fps que tiene el juego
FPS = 60
# Inicializamos pygame
pygame.init()

# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)


# Cambio el título de la ventana
pygame.display.set_caption("Simulacion")

# Comenzamos el bucle del juego
run = True

# Definimos los fps
clock = pygame.time.Clock()
# instancia de la pelotad
ball = BallCharacter()

# definimos los colores que usaremos en la ventana
black = (0, 0, 0)

# En esta variable se guardan los estados de las teclas: True si estan presionados y False si no lo estan
key_events = {
    'key_d': False,
    'key_a': False,
    'key_space': False,
    'static': False
}


while run:
    #Actualizacion del estado del salto
    key_events['key_space'] = ball.jump_state
    clock.tick(FPS)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        # defino la variable que tendra los eventos que captura del teclado
        key = pygame.key.get_pressed()
        # Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT:
            run = False

        # captamos el evento de la tecla d
        if key[K_d]:
            key_events['key_d'] = True
        else:
            key_events['static'] = True
            key_events['key_d'] = False

        # captamos el evento de la tecla a
        if key[K_a]:
            key_events['key_a'] = True
        else:
            key_events['static'] = True
            key_events['key_a'] = False

        if key[K_SPACE]:
            key_events['key_space'] = True
        else:
            key_events['static'] = True

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         key_events['key_space'] = True
        #     else:
        #         key_events['static'] = True
        #         key_events['key_spac'] = False

    # una vez obtenidos los resultados finales de key_events
    # pasamos el estado de los teclados para hacer los moviminentos
    # print(ball.jump)
    ball.moves(screen, key_events)
    # actualiza la ventana, de lo contrario todo quedara estatico
    pygame.display.update()
    screen.fill(black)
    pygame.event.pump()

# Salgo de pygame
pygame.quit()

