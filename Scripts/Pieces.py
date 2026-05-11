from .Utils import pos_converter, get_range, str_to_tuple_pos

class Pieces:
    def __init__(self, pos: str, color: str, board: dict, p_type: str):
        self.pos = str_to_tuple_pos(pos)
        self.color = color
        self.board = board
        self.p_type = p_type

        self.moveset = []
        self.stop = False

    def change_pos(self, pos):
        self.pos = str_to_tuple_pos(pos)
        
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
        return bool(self.board[pos_converter(pos)])

    def pos_is_enemy(self, pos):
        if self.board[pos_converter(pos)]:
            return self.board[pos_converter(pos)] != self.color
        else:
            return False
    
    def check_area(self, king_pos: list):
        check = []
        for pos in self.moveset:
            if pos in king_pos:
                check.append(pos)
        return check
    
    def check_inbound(self, pos: tuple):
        return pos[0] > 0 and pos[0] < 9 and pos[1] > 0 and pos[1] < 9

    def return_pos(self):
        return pos_converter(self.pos)
    
    def reset_moveset(self):
        self.moveset = []

class Pawn(Pieces):
    def __init__(self, pos: str, color: str, board: dict, en_passant_board: dict):
        super().__init__(pos, color, board, "pawn")

        self.en_passant_board = en_passant_board
        self.move = []
        self.can_en_passant = False
        self.has_moved = False

        if color == "white":
            self.move = [(0, 2), (0, 1), (-1, 1), (1, 1)]
        if color == "black":
            self.move = [(0, -2), (0, -1), (-1, -1), (1, -1)]

    def update_has_moved():
        self.has_moved = True

    def current_moveset(self) -> dict:
        self.reset_moveset()
        move_list = []

        for i in range(0, 4):
            move_list.append((self.move[i][0] + self.pos[0], self.move[i][1] + self.pos[1]))

        current_move = move_list[0]
        if not self.has_moved and not self.pos_occupied(current_move):
            self.append_move(current_move)
            self.en_passant_board[current_move] = True

        current_move = move_list[1]
        if not self.pos_occupied(current_move):
            self.append_move(current_move)

        if self.pos[0] != 1:
            current_move = move_list[2]
            can_en_passant = self.en_passant_board[self.color] == current_move[0]
            if self.pos_is_enemy(current_move) or can_en_passant:
                self.append_move(current_move)

        if self.pos[0] != 8:
            current_move = move_list[3]
            can_en_passant = self.en_passant_board[self.color] == current_move[0]
            if self.pos_is_enemy(current_move) or can_en_passant:
                self.append_move(current_move)
    
        return self.moveset

class Rook(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "rook")
    
    def current_moveset(self):
        self.reset_moveset()
        self.stop = False
        for x in get_range(self.pos[0], 1):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break

        self.stop = False
        for x in get_range(self.pos[0], 8):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break

        self.stop = False
        for y in get_range(self.pos[1], 1):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break
    
        self.stop = False
        for y in get_range(self.pos[1], 8):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break

        return self.moveset

class Bishop(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "bishop")

    def current_moveset(self):
        self.reset_moveset()
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
                break
        
        return self.moveset

class Knight(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "knight")
        self.move = [(-1, 2), (-1, -2), (1, 2), (1, -2),
                     (2, 1), (2, -1), (-2, 1), (-2, -1),]
    
    def current_moveset(self):
        self.reset_moveset()
        for move in self.move:
            moving = (move[0] + self.pos[0], move[1] + self.pos[1])
            if self.check_inbound(moving):
                if self.calculation(moving):
                    self.append_move(moving)

class Quenn(Pieces):
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "quenn")
    
    def current_moveset(self):
        self.reset_moveset()
        self.stop = False
        for x in get_range(self.pos[0], 1):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break

        self.stop = False
        for x in get_range(self.pos[0], 8):
            move = (x, self.pos[1])
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break

        self.stop = False
        for y in get_range(self.pos[1], 1):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
                break
    
        self.stop = False
        for y in get_range(self.pos[1], 8):
            move = (self.pos[0], y)
            if self.calculation(move):
                self.append_move(move)
            elif self.stop or not self.calculation(move):
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
                break
        
        return self.moveset

class King(Pieces): 
    def __init__(self, pos: str, color: str, board: dict):
        super().__init__(pos, color, board, "king")
        self.move = [(1, 1), (1, -1), (-1, 1), (-1, 1),
                     (1, 0), (-1, 0), (0, 1), (0, -1),]
        self.check = False
    
    def current_moveset(self):
        self.reset_moveset()
        for move in self.move:
            moving = (move[0] + self.pos[0], move[1] + self.pos[1])
            if self.check_inbound(moving):
                if self.calculation(moving):
                    self.append_move(moving)
    
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
