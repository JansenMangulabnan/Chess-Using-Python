from .Pieces import Pieces, Pawn, Rook, Bishop, Knight, Quenn, King

def create_board():
    board = {}
    letter = "abcdefgh"
    for i in range(0, 8):
        for j in range(0, 8):
            board[letter[i] + str(j + 1)] = None
    return board

class Board:
    def __init__(self):
        self.letter = "abcdefgh"
        self.objects = create_board()

        self.can_en_pessant = {
            "black": None,
            "white": None,
        }

    def init(self):     
        for i in range(0, 8):
            pos = self.letter[i] + "2"
            self.objects[pos] = Pawn(pos, "white", self.can_en_pessant)
            pos = self.letter[i] + "7"
            self.objects[pos] = Pawn(pos, "black", self.can_en_pessant)
        
        self.objects["a1"] = Rook("a1", "white")
        self.objects["h1"] = Rook("h1", "white")
        self.objects["a8"] = Rook("a8", "black")
        self.objects["h8"] = Rook("h8", "black")

        self.objects["c1"] = Bishop("c1", "white")
        self.objects["f1"] = Bishop("f1", "white")
        self.objects["c8"] = Bishop("c8", "black")
        self.objects["f8"] = Bishop("f8", "black")

        self.objects["b1"] = Knight("b1", "white")
        self.objects["g1"] = Knight("g1", "white")
        self.objects["b8"] = Knight("b8", "black")
        self.objects["g8"] = Knight("g8", "black")

        self.objects["d1"] = Quenn("d1", "white")
        self.objects["d8"] = Quenn("d8", "black")

        self.objects["e1"] = King("d1", "white")
        self.objects["e8"] = King("d8", "black")