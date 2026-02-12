from .Utils import pos_converter, get_range, str_to_tuple_pos

class Pieces:
    def __init__(self, pos: str, color: str, board: dict, p_type: str):
        self.pos = str_to_tuple_pos(pos)
        self.color = color
        self.board = board
        self.p_type = p_type

        self.moveset = []
        self.can_en_passant = False
        self.has_moved = False
        self.stop = False

    def return_type(self):
        return self.p_type
    
    def calculation(self, move):
        if self.pos_is_enemy(move):
            self.stop = True
            return True
        if self.pos != move and not self.pos_occupied(move):
            return True
        return False

    def append_move(self, move):
        self.moveset.append(pos_converter(move))

    def pos_occupied(self, pos):
        if pos_converter(pos) in self.board:
            return bool(self.board[pos_converter(pos)])
        else:
            return True

    def pos_is_enemy(self, pos):
        if pos_converter(pos) in self.board:
            if self.board[pos_converter(pos)]:
                return self.board[pos_converter(pos)] != self.color
            else:
                return False
        else:
            return False
    
    def check_area(self, king_pos: list):
        check = []
        for pos in self.moveset:
            if pos in king_pos:
                check.append(pos)
        return check

class Pawn(Pieces):
    def __init__(self, pos: str, color: str, board: dict, en_passant_board: dict):
        super().__init__(pos, color, board, "pawn")

        self.en_passant_board = en_passant_board
        self.move = []
        self.letter = "abcdefgh"

        if color == "white":
            self.move = [(0, 2), (0, 1), (-1, 1), (1, 1)]
        if color == "black":
            self.move = [(0, -2), (0, -1), (-1, -1), (1, -1)]

    def current_moveset(self) -> dict:
        dict_move = []

        for i in range(0, 4):
            dict_move.append((self.move[i][0] + self.pos[0], self.move[i][1] + self.pos[1]))

        current_move = dict_move[0]
        if not self.has_moved and not self.pos_occupied(current_move):
            self.append_move(current_move)
            self.en_passant_board[current_move] = True

        current_move = dict_move[1]
        if not self.pos_occupied(current_move):
            self.append_move(current_move)

        if self.pos[0] != 1:
            current_move = dict_move[2]
            can_en_passant = self.en_passant_board[self.color] == current_move[0]
            if self.pos_is_enemy(current_move) or can_en_passant:
                self.append_move(current_move)

        if self.pos[0] != 8:
            current_move = dict_move[3]
            can_en_passant = self.en_passant_board[self.color] == current_move[0]
            if self.pos_is_enemy(current_move) or can_en_passant:
                self.append_move(current_move)
    
        return self.moveset

class Rook(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "rook")
    
    def current_moveset(self):
        self.stop = False
        for x in get_range(self.pos[0], 1):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break

        self.stop = False
        for x in get_range(self.pos[0], 8):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break

        self.stop = False
        for y in get_range(self.pos[1], 1):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
    
        self.stop = False
        for y in get_range(self.pos[1], 8):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break

        return self.moveset

class Bishop(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "bishop")

    def current_moveset(self):
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 1):
            p_y -= 1
            if p_y <= 0:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 1):
            p_y += 1
            if p_y >= 9:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 8):
            p_y -= 1
            if p_y <= 0:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 8):
            p_y += 1
            if p_y >= 9:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        return self.moveset

class Knight(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "knight")
        self.move = [(-1, 2), (-1, -2), (1, 2), (1, -2),
                     (2, 1), (2, -1), (-2, 1), (-2, -1),]
    
    def current_moveset(self):
        for move in self.move:
            if self.calculation((move[0] + self.pos[0], move[1] + self.pos[1])):
                self.append_move((move[0] + self.pos[0], move[1] + self.pos[1]))

class Quenn(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "quenn")
    
    def current_moveset(self):
        self.stop = False
        for x in get_range(self.pos[0], 1):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break

        self.stop = False
        for x in get_range(self.pos[0], 8):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break

        self.stop = False
        for y in get_range(self.pos[1], 1):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
    
        self.stop = False
        for y in get_range(self.pos[1], 8):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 1):
            p_y -= 1
            if p_y <= 0:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 1):
            p_y += 1
            if p_y >= 9:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 8):
            p_y -= 1
            if p_y <= 0:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        p_y = self.pos[1]
        self.stop = False
        for x in get_range(self.pos[0], 8):
            p_y += 1
            if p_y >= 9:
                break
            move = (x, p_y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                print("end")
                break
        
        return self.moveset

class King(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "king")
        self.move = [(1, 1), (1, -1), (-1, 1), (-1, 1),
                     (1, 0), (-1, 0), (0, 1), (0, -1),]
        self.check = False
    
    def current_moveset(self):
        for move in self.move:
            if self.calculation(move):
                self.append_move(move)
    
    def update_check(self, check):
        for move in self.moveset:
            if move in check:
                self.moveset.remove(move)
            if self.pos in check:
                self.check = True

    def is_checkmate(self, defense_list):
        checkmate = False
        if self.check and not self.moveset and not defense_list:
            checkmate = True
        return checkmate
