import pygame


class BallCharacter:
    # definimos la caracteriscitas de la pelota
    def __init__(self):
        # definimos la posicion inicial de la pelota
        self.initial_x = 0
        self.initial_y = 255
        # definimos la posicion de la pelota que ira variando y la velocidad en la que se movera la pelota
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed = 1

    # definimos la funcion que hara un movimiento recto hacia la derecha
    def move_right(self, screen):
        # para hacer que la pelota se mueva, le sumo 1 a la posicion variante
        pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)
        self.x += 1
    # esta funcion hara que la pelta vaya para la izquierdad de 1 en uno en el plano cartesiano

    def move_left(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)
        self.x -= 1
    # esta funcion muestra cuando la pelota esta cuando no tiene movimiento

    def static_move(self, screen):
        pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)
