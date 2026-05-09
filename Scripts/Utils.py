import pygame

BASE_IMG_PATH = "ChessPieces/"

def load_image(path, rect=None):
    img = pygame.image.load(BASE_IMG_PATH + path)
    if rect:
        img = pygame.transform.scale(img, (rect.width, rect.height))
    return img

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
    