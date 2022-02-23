
import pygame
RED = (239, 235, 216)
key_events = {
    'key_d': False,
    'key_a': False,
    'key_space': False,
    'static': False
}

jump_state = False


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
        self.ball_radio = 30
        self.gravity = 2
        # en esta variable se guarda la velocidad del
        self.v_y = 20
        # definimos la variable que definira el estado del salto, para que no salte contunuamente la pelota
        self.jump_state = False
        # Definimos la variable donde se asignara el dibujo de la pelota
        self.ball_rect = None

    # definimos la funcion que hace los tipos de movimientos

    def moves(self, screen, move_type, object_pos, intercept):

        # movimientos
        if intercept == 0 and self.jump_state == False:
            self.y += self.v_y
            self.v_y -= self.gravity
            
        if move_type['key_d']:
            # para hacer que la pelota se mueva, le sumo 1 a la posicion variante
            self.ball_rect = pygame.draw.circle(
                screen, 
                RED, 
                (self.x, self.y), 
                self.ball_radio
            )
            self.x += self.speed

        if move_type['key_a']:
            # para hacer que la pelota se mueva, le sumo 1 a la posicion variante
            self.ball_rect = pygame.draw.circle(
                screen,
                RED, 
                (self.x, self.y), 
                self.ball_radio
            )
            self.x -= self.speed

        # movimiento de salto
        if move_type['key_space']:
            if self.jump_state == False:
                self.y = object_pos - (self.ball_radio)
                intercept = 0
            # una vez que la pelota comienze a elevarse el estavo sera True
            self.jump_state = True
            # la pelota aumenta la altura de acuerdo a v_y
            self.y -= self.v_y
            # mientras la pelota va mas arriba la aceleracion va disminuyendo hasta llegar a su punto maximo
            self.v_y -= self.gravity
            # si la posicion de la pelota es igual a la posicion inicial se resetearan la posicion y aceleracion
            print(intercept)
            if intercept == 1:
                self.y = object_pos - (self.ball_radio - 2)
                self.v_y = 20
                # una vez que la pelota llegue al punto final de su trayectoria el estado sera False para que no sigua saltando
                self.jump_state = False

        # si esta condicion se cumple la pelota sera imprimida sin modificar la posicion
        if move_type['static']:
            print('Static')
            self.ball_rect = pygame.draw.circle(
                screen, 
                RED, 
                (self.x, self.y), 
                self.ball_radio
            )
        
        
        
        

