import pygame 
import sys

from Scripts.GameManager import GameProcess, BoardGrid, Render
from Scripts.Board import Board
from Scripts.Utils import load_image, get_img_rect

class Chess:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("CHESS")
        
        self.surface = pygame.display.set_mode((1000, 700))
        self.clock = pygame.time.Clock()

        self.surf_rect = self.surface.get_rect()
        self.board_dict = BoardGrid(self.surf_rect).create_rect()

        self.board = Board()
        self.board.init()

        self.pieces_img = {
            "black": {
                "pawn": load_image("b_pawn.png", self.board_dict["a1"]),
                "king": load_image("b_king.png", self.board_dict["a1"]),
                "quenn": load_image("b_quenn.png", self.board_dict["a1"]),
                "knight": load_image("b_knight.png", self.board_dict["a1"]),
                "bishop": load_image("b_bishop.png", self.board_dict["a1"]),
                "rook": load_image("b_rook.png", self.board_dict["a1"]),
            },
            "white": {
                "pawn": load_image("w_pawn.png", self.board_dict["a1"]),
                "king": load_image("w_king.png", self.board_dict["a1"]),
                "quenn": load_image("w_quenn.png", self.board_dict["a1"]),
                "knight": load_image("w_knight.png", self.board_dict["a1"]),
                "bishop": load_image("w_bishop.png", self.board_dict["a1"]),
                "rook": load_image("w_rook.png", self.board_dict["a1"]),
            }
        }
        self.moveset_img = load_image("moveset.png", self.board_dict["a1"])

        self.pieces_rect = get_img_rect(self.pieces_img["black"], self.pieces_img["white"])
        self.renderer = Render(self.surface, self.board_dict, self.pieces_img)
        self.game = GameProcess()

        self.has_moved = False
        self.pos_clicked = ""

    def run(self):
        while True:
            self.surface.fill((0, 0, 0))
            m_pos = pygame.mouse.get_pos()
            objects = self.board.return_objects()

            if self.has_moved:
                self.game.turn_checker(self.has_moved)
                self.has_moved = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.pos_clicked = self.game.clicked(self.board_dict, m_pos)
            
            self.renderer.board()
            self.renderer.pieces(objects)
            
            if self.pos_clicked and objects[self.pos_clicked]:
                self.renderer.moveset(self.moveset_img, objects[self.pos_clicked])

            pygame.display.update()
            self.clock.tick(60)
    

Chess().run()