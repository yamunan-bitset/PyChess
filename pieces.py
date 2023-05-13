import pygame
from board import get_coord_from_pos

class Piece:
    def __init__(self, screen, type, pos):
        self.screen = screen
        self.type = type
        self.pos = pos
        self.coord = get_coord_from_pos(self.pos)
        self.image = self.get_image_from_type()
        self.captured = False

    def get_image_from_type(self):
        img = pygame.image.load(f"data/assets/{self.type}.png")
        return img

    def draw(self):
        if not self.captured:
            self.screen.blit(self.image, self.coord)
