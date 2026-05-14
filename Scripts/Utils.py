import pygame

BASE_IMG_PATH = "ChessPieces/"

def load_image(path, rect=None):
    img = pygame.image.load(BASE_IMG_PATH + path)
    if rect:
        img = pygame.transform.scale(img, (rect.width, rect.height))
    return img

def get_img_rect(img_b: dict, img_w: dict) -> dict[str, dict[str, pygame.Rect]]:
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

def get_range(start, finish) -> list:
    range_list = []
    while start < finish:
        start += 1
        range_list.append(start)
    while start > finish:
        start -= 1
        range_list.append(start)
    return range_list

def str_to_tuple_pos(pos) -> tuple:
    letter = "-abcdefgh"
    output = (letter.index(pos[0]), int(pos[1]))
    return output
    
def reverse_color(color: str):
    if color == "white":
        return "black"
    return "white"