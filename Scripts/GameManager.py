import pygame 

class GameProcess:
    def __init__(self, object_dict: dict):
        self.object_dict = object_dict
        self.current_piece = ""
        self.defense_list = []
        self.whites_turn = True
    
    def move_piece(self, init_pos, target_pos):
        self.object_dict[target_pos] = self.object_dict[init_pos]
        self.object_dict[init_pos] = None
    
    def clicked(self, grid_rect: dict, m_pos) -> str:
        for key, rect in grid_rect.items():
            if rect.collidepoint(m_pos):
                return key
        return ""          

    def turn_checker(self, turn_has_moved: bool) -> bool:
        if turn_has_moved:
            self.whites_turn = not self.whites_turn
        
        return self.whites_turn
    
    def update_moveset(self, king_pos: dict, object_dict: dict):
        object_dict[king_pos["white"]].current_moveset()
        object_dict[king_pos["black"]].current_moveset()

        for key, value in object_dict.items():
            if value.p_type != "king":
                value.current_moveset()
                if value.color == "white":
                    object_dict[king_pos["black"]].update_check(value.moveset)
                if value.color == "black":
                    object_dict[king_pos["white"]].update_check(value.moveset)

class BoardGrid:
    def __init__(self, surf_rect,  grid=[8, 8]):
        board_rect = pygame.Rect(0, 0, 600, 600)
        board_rect.center = surf_rect.center

        self.board_pos = board_rect.topleft
        self.board_size = board_rect.size
        self.grid_size = (self.board_size[0] / grid[0], self.board_size[1] / grid[1])
        self.pos_name = [
            "abcdefgh",
            "87654321"
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
    
    def moveset(self, img, piece):
        piece.current_moveset()
        for move in piece.moveset:
            self.surf.blit(img, self.rect_dict[move].topleft)
