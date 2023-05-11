import pygame

def get_pos_from_coord(coord):
    if 50 <= coord[0] < 150: x = 1
    if 150 <= coord[0] < 250: x = 2
    if 250 <= coord[0] < 350: x = 3
    if 350 <= coord[0] < 450: x = 4
    if 450 <= coord[0] < 550: x = 5
    if 550 <= coord[0] < 650: x = 6
    if 650 <= coord[0] < 750: x = 7
    if 750 <= coord[0] < 850: x = 8

    if 50 <= coord[1] < 150: y = 0
    if 150 <= coord[1] < 250: y = 1
    if 250 <= coord[1] < 350: y = 2
    if 350 <= coord[1] < 450: y = 3
    if 450 <= coord[1] < 550: y = 4
    if 550 <= coord[1] < 650: y = 5
    if 650 <= coord[1] < 750: y = 6
    if 750 <= coord[1] < 850: y = 7

    try:
        return (x % 9) + y * 8
    except UnboundLocalError:
        return -1

def get_coord_from_pos(pos):
    y = 0
    if 8 >= pos > 0: y = 0
    if 16 >= pos > 8: y = 1
    if 24 >= pos > 16: y = 2
    if 32 >= pos > 24: y = 3
    if 40 >= pos > 32: y = 4
    if 48 >= pos > 40: y = 5
    if 56 >= pos > 48: y = 6
    if 64 >= pos > 56: y = 7
    ret = (((pos - 1) % 8) * 100 + 50, y * 100 + 50)
    return ret

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
