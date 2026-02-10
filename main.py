import pygame 
import sys

from Scripts.GameManager import BoardGrid, Render
from Scripts.Utils import load_image, get_img_rect

class Game:
    def __init__(self):
        pygame.init()

        self.screen = (1000, 700)
        self.surface = pygame.display.set_mode(self.screen)
        pygame.display.set_caption("CHESS")
        self.clock = pygame.time.Clock()

        self.surf_rect = self.surface.get_rect()

        self.pieces_img = {
            "black": {
                "pawn": load_image("b_pawn.png"),
                "king": load_image("b_king.png"),
                "quenn": load_image("b_quenn.png"),
                "knight": load_image("b_knight.png"),
                "bishop": load_image("b_bishop.png"),
                "rook": load_image("b_rook.png"),
            },
            "white": {
                "pawn": load_image("w_pawn.png"),
                "king": load_image("w_king.png"),
                "quenn": load_image("w_quenn.png"),
                "knight": load_image("w_knight.png"),
                "bishop": load_image("w_bishop.png"),
                "rook": load_image("w_rook.png"),
            }
        }

        self.pieces_rect = get_img_rect(self.pieces_img["black"], self.pieces_img["white"])

        self.board_rect = pygame.Rect(0, 0, 600, 600)
        self.board_rect.center = self.surf_rect.center

        self.board_dict = BoardGrid(self.board_rect).create_rect()
        self.renderer = Render(self.surface)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.renderer.board(self.board_dict)

            pygame.display.update()
            self.clock.tick(60)
    

Game().run()