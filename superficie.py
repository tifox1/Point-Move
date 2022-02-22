import pygame 
GREEN = (53, 94, 59)
class Surface:
    def __init__(self):
        self.initial_x = 0
        self.initial_y = 285
        self.width = 500
        self.length = 1200 
        self.surface_rect = None
    
    def rect(self, surface):
        self.surface_rect = pygame.draw.rect(surface, GREEN, (
                self.initial_x, 
                self.initial_y, 
                self.length, 
                self.width, 
            )
        )
