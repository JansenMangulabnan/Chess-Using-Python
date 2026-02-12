import pygame
import os

BASE_IMG_PATH = "Chess-Using-Python/ChessPieces/"

def load_image(path, rect):
    img = pygame.image.load(BASE_IMG_PATH + path)
    scaled = pygame.transform.scale(img, (rect.width, rect.height))
    return scaled

def get_img_rect(img_b, img_w):
    img_dict = {
        "black": {},
        "white": {}
    }
    pieces = ["pawn", "king", "quenn", "knight", "rook", "bishop"]

    for piece in pieces:
        img_dict["black"][piece] = img_b[piece].get_rect()
        img_dict["white"][piece] = img_w[piece].get_rect()

    return img_dict

def pos_converter(pos: tuple) -> str:
    letter = "labcdefgh"
    return letter[pos[0]] + str(pos[1])

def get_range(start, finish):
    range_list = []
    if start == finish:
        return []
    if start < finish:
        while True:
            start += 1
            range_list.append(start)
            if start >= finish:
                return range_list
    if start > finish:
        while True:
            start -= 1
            range_list.append(start)
            if start <= finish:
                return range_list

def str_to_tuple_pos(pos):
    letter = "-abcdefgh"
    output = (letter.index(pos[0]), int(pos[1]))
    return output
    