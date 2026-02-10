from Pieces import Pawn, Rook, Bishop, Knight, Quenn, King

def create_board():
    board = {}
    letter = "abcdefgh"
    for i in range(0, 8):
        board[letter[i] + str(i + 1)] = None
    return board

class Board:
    def __init__(self):
        self.letter = "abcdefgh"
        self.colors = create_board()
        self.objects = create_board()

        self.can_en_pessant = {
            "black": None,
            "white": None,
        }
    
    def init(self):
        for i in range(0, 8):
            self.colors[self.letter[i] + "1"] = "white"
            self.colors[self.letter[i] + "2"] = "white"
            self.colors[self.letter[i] + "7"] = "black"
            self.colors[self.letter[i] + "8"] = "black"
        
        for i in range(0, 8):
            pos = self.letter[i] + "2"
            self.objects[pos] = Pawn(pos, "white", self.colors, self.can_en_pessant)
            pos = self.letter[i] + "7"
            self.objects[pos] = Pawn(pos, "black", self.colors, self.can_en_pessant)
        
        self.objects["a1"] = Rook("a1", "white", self.colors)
        self.objects["h1"] = Rook("h1", "white", self.colors)
        self.objects["a8"] = Rook("a8", "black", self.colors)
        self.objects["h8"] = Rook("h8", "black", self.colors)

        self.objects["c1"] = Bishop("c1", "white", self.colors)
        self.objects["f1"] = Bishop("f1", "white", self.colors)
        self.objects["c8"] = Bishop("c8", "black", self.colors)
        self.objects["f8"] = Bishop("f8", "black", self.colors)

        self.objects["b1"] = Knight("b1", "white", self.colors)
        self.objects["g1"] = Knight("g1", "white", self.colors)
        self.objects["b8"] = Knight("b8", "black", self.colors)
        self.objects["g8"] = Knight("g8", "black", self.colors)

        self.objects["d1"] = Quenn("d1", "white", self.colors)
        self.objects["d8"] = Quenn("d8", "black", self.colors)

        self.objects["e1"] = King("d1", "white", self.colors)
        self.objects["e8"] = King("d8", "black", self.colors)
        
test = Board()
test.init()

print(test.objects, test.colors)