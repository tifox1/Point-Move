import pygame 

RED = (255,69,0)
#esta clase rempresentara un tipo de superficie
class Wall:
    def __init__(self):
        self.initial_x = 600
        self.initial_y = 190
        self.width = 10
        self.height = 200 
        self.wall_rect = None
    
    def rect(self, surface):
        self.wall_rect = pygame.draw.rect(surface, RED, (
                self.initial_x, 
                self.initial_y, 
                self.height, 
                self.width, 
            )
        )


        