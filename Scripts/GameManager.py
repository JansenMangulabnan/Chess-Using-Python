import pygame 

class BoardGrid:
    def __init__(self, board_rect: pygame.Rect,  grid=[8, 8]):
        self.board_pos = board_rect.topleft
        self.board_size = board_rect.size
        self.grid_size = (self.board_size[0] / grid[0], self.board_size[1] / grid[1])
        self.pos_name = [
            "abcdefgh",
            "12345678"
        ]

    def create_rect(self):
        rect_dict = {}
        pos = list(self.board_pos)
        space = 0

        for letter in self.pos_name[0]:
            for number in self.pos_name[1]:
                rect_dict[letter + number] = pygame.Rect(pos[0] + space , pos[1] + space, self.grid_size[0] - space, self.grid_size[1] - space)
                pos[1] += self.grid_size[1]
            pos[1] = self.board_pos[1]
            pos[0] += self.grid_size[0]
            
        return rect_dict

class Render:
    def __init__(self, surf):
        self.surf = surf

    def board(self, rect_dict: dict):
        white = True
        manager = 0

        for rect in rect_dict.values():
            pygame.draw.rect(self.surf, "white" if white else "gray", rect)
            white = not white
            manager += 1

            if manager >= 8:
                manager = 0
                white = not white

    def pieces(self, surf):
        pass
