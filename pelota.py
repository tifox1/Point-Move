import pygame
import numpy as np
import math 

class BallCharacter:
    # definimos la caracteriscitas de la pelota
    def __init__(self):
        # definimos la posicion inicial de la pelota
        self.initial_x = 100
        self.initial_y = 255
        # definimos la posicion de la pelota que ira variando y la velocidad en la que se movera la pelota
        self.x = self.initial_x
        self.y = self.initial_y
        self.speed = float(5)

        #definimos el tiempo que tendra el objeto para hacer sus fisicas
        self.ball_clock = pygame.time.get_ticks()/1000

        #___Propiedades de la fisica___
        #gravedad del objeto 
        self.gravity = float(-9.5)
        #expresamos las velocidades del movimiento parabolico respecto al eje en coordenadas polares
        self.v_x = float(10) * np.cos(math.radians(90))
        self.v_y = float(10) * np.sin(-(math.radians(90)))
        
    # definimos la funcion que hace los tipos de movimientos
    def moves(self, screen, move_type):
        if move_type['key_d']:
            # para hacer que la pelota se mueva, le sumo 1 a la posicion variante
            pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)
            self.x += self.speed

        if move_type['key_a']:
            # para hacer que la pelota se mueva, le sumo 1 a la posicion variante
            pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)
            self.x -= self.speed

        if move_type['static']:
            pygame.draw.circle(screen, (200, 0, 0), (self.x, self.y), 30)

        if move_type['key_space']:
            self.x = (self.x - (self.v_x * self.ball_clock))
            self.y = (self.y + self.v_y * self.ball_clock + 1/2 * (self.gravity * (self.ball_clock)**2))
            

