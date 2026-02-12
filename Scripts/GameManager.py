import pygame 

class GameProcess:
    def __init__(self):
        self.current_piece = ""

    def update_moveset(self):
        pass

class BoardGrid:
    def __init__(self, surf_rect,  grid=[8, 8]):
        board_rect = pygame.Rect(0, 0, 600, 600)
        board_rect.center = surf_rect.center

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
    def __init__(self, surf, rect_dict: dict, asset):
        self.surf = surf
        self.asset = asset
        self.rect_dict = rect_dict

    def board(self):
        white = True
        manager = 0

        for rect in self.rect_dict.values():
            pygame.draw.rect(self.surf, "white" if white else "gray", rect)
            white = not white
            manager += 1

            if manager >= 8:
                manager = 0
                white = not white

    def pieces(self, pieces_dict: dict):
        for key, values in pieces_dict.items():
            if values:
                self.surf.blit(self.asset[values.color][values.p_type], self.rect_dict[key].topleft)
