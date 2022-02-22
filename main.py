
import pygame
from pygame.constants import K_SPACE, K_a, K_d
from pelota import *
from pared import *
from superficie import Surface
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
# Instanciamos los objetos que se mostraran en la pantalla
ball = BallCharacter()

surface = Surface()

wall = Wall()

# definimos los colores que usaremos en la ventana
BLUE = (34, 113, 179)
# object interception
intercept_obj = {
    'intercept': 0,
    'object_position': None,
}


# En esta variable se guardan los estados de las teclas: True si estan presionados y False si no lo estan
key_events = {
    'key_d': False,
    'key_a': False,
    'key_space': False,
    'static': False
}


while run:
    # Actualizacion del estado del salto
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

    # una vez obtenidos los resultados finales de key_events
    # pasamos el estado de los teclados para hacer los moviminentos
    # Dibuja la pared
    surface.rect(screen)
    wall.rect(screen)
    ball.moves(
        screen,
        key_events,
        intercept_obj['object_position'],
        intercept_obj['intercept']
    )
    # Eventos dentro del juego
    if ball.ball_rect.colliderect(wall.wall_rect) == 1:
        intercept_obj['intercept'] = 1
        intercept_obj['object_position'] = wall.initial_y

    elif ball.ball_rect.colliderect(surface.surface_rect) == 1:
        intercept_obj['intercept'] = 1
        intercept_obj['object_position'] = surface.initial_y
        
    elif ball.ball_rect.colliderect(wall.wall_rect) == 0 or ball.ball_rect.colliderect(wall.wall_rect) == 0:
        intercept_obj['intercept'] = 0
        intercept_obj['object_position'] = surface.initial_y

    print(intercept_obj['intercept'])
    # actualiza la ventana, de lo contrario todo quedara estatico
    pygame.display.update()
    screen.fill(BLUE)
    pygame.event.pump()

# Salgo de pygame
pygame.quit()
