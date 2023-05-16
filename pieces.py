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
        if self.type != "":
            img = pygame.image.load(f"data/assets/{self.type}.png")
            return img

    def draw(self):
        if self.type != "" and self.type != None:
            if self.type[2:] == "pawn":
                if self.pos[1] == 7 or self.pos[1] == 0:
                    self.type = self.type[:2] + "queen"
                    self.image = self.get_image_from_type()
            if not self.captured:
                self.screen.blit(self.image, self.coord)
