import pygame 
from .Board import Board
from .Pieces import Pieces, Pawn

class GameProcess:
    def __init__(self):
        self.king_moveset = {
            "white": [],
            "black": []
        }
        self.whites_turn = True
    
    def move_piece(self, board: Board, object_piece: Pieces, target_pos: str):
        if object_piece.return_pos() != target_pos:
            if (type(object_piece) is Pawn):
                object_piece.update_has_moved()
            temp = object_piece.return_pos()
            object_piece.change_pos(target_pos)
            board.objects[target_pos] = object_piece
            board.objects[temp] = None
    
    def clicked(self, grid_rect: dict[str, pygame.Rect], m_pos: tuple[int, int]) -> str:
        for key, rect in grid_rect.items():
            if rect.collidepoint(m_pos):
                return key
        return ""
    
    def update_moveset(self, object_dict: dict[str, Pieces]):
        for value in object_dict.values():
            if value:
                value.update_board(object_dict)
                value.current_moveset()

                if value.p_type == "king":
                    self.king_moveset[value.color] = value.moveset


        
    def can_move(self, piece: Pieces, target_pos) -> bool:
        if piece and target_pos in piece.moveset:
            return True
        return False

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
    
    def moveset(self, img, piece, color: str):
        piece.current_moveset()
        if color == piece.color:
            for move in piece.moveset:
                self.surf.blit(img, self.rect_dict[move].topleft)
