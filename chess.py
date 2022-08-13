"""
Command Line Chess
2022 August 
Alexander Michael Pommer Alba
"""

BOARD = [] # 1d board that stores instances of Squares or Pieces
UCI_map = {} # Universal Chess Interface dictionary to map player input
counter = 0
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for letter in LETTERS:
    for number in range(1,9):
        UCI_map[f'{letter}{number}'] = counter
        counter += 1

class Square:

    def __init__(self, position: int, color: str, type: str) -> None:
        self.position = position # 0 to 63
        self.color = color # 'Black', 'White' or 'Empty'
        self.type = type

    def is_empty(self) -> bool:
        return self.color == "Empty"

class Pieces(Square):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

class Pawn(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

    def legal_moves(self):
        legal = []

        if self.color == 'White':
            
            one_step = self.position + 8
            if one_step < 64 and BOARD[one_step].is_empty():
                legal.append(one_step)
            
            two_steps = self.position + 16
            if self.position in range(8, 16) and BOARD[two_steps].is_empty():
                legal.append(two_steps)
                # TODO en passant

            capture_right = self.position + 9
            # Not in far right column a
            if self.position % 8 != 7 and BOARD[capture_right].is_empty() == False:
                legal.append(capture_right)
            
            capture_left = self.position + 7
            # Not in far left column h
            if self.position % 8 != 0 and BOARD[capture_left].is_empty() == False:
                legal.append(capture_left)
                
            return legal    

        if self.color == 'Black':
            one_step = self.position - 8
            if one_step >= 0 and BOARD[one_step].is_empty():
                legal.append(one_step)
            two_steps = self.position - 16
            if self.position in range(43, 55) and BOARD[two_steps].is_empty():
                legal.append(two_steps)
                # TODO en passant
            capture_left = self.position - 7
            if self.position % 8 != 7 and BOARD[capture_left].is_empty() == False:
                legal.append(capture_left)
            capture_right = self.position - 9
            if self.position % 8 != 0 and BOARD[capture_right].is_empty() == False:
                legal.append(capture_right)
            return legal  
            
            pass
        if self.color == 'Empty': #TODO refactor
            return []

    # TODO promotion

class King(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

class Queen(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

class Rook(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

class Knight(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)

class Bishop(Pieces):

    def __init__(self, position: int, color: str, type: str) -> None:
        super().__init__(position, color, type)


def initialize_board():
    BOARD.append(Rook(0, 'White', 'R'))
    BOARD.append(Knight(1, 'White', 'N'))
    BOARD.append(Bishop(2, 'White', 'B'))
    BOARD.append(Queen(3, 'White', 'Q'))
    BOARD.append(King(4, 'White', 'K'))
    BOARD.append(Bishop(5, 'White', 'B'))
    BOARD.append(Knight(6, 'White', 'N'))
    BOARD.append(Rook(7, 'White', 'R'))
    for sq in range(8, 16):
        BOARD.append(Pawn(sq, 'White', 'P'))
    for sq in range(16, 48):
        BOARD.append(Square(sq, 'Empty', ' '))
    for sq in range(48, 56):
        BOARD.append(Pawn(sq, 'Black', 'p'))
    BOARD.append(Rook(56, 'Black', 'r'))
    BOARD.append(Knight(57, 'Black', 'n'))
    BOARD.append(Bishop(58, 'Black', 'b'))
    BOARD.append(Queen(59, 'Black', 'q'))
    BOARD.append(King(60, 'Black', 'k'))
    BOARD.append(Bishop(61, 'Black', 'b'))
    BOARD.append(Knight(62, 'Black', 'n'))
    BOARD.append(Rook(63, 'Black', 'r'))

def display_board():
    print ('\n'*30 )
    cols = '   |'
    for letter in LETTERS:
        cols += f' {letter} |'
    counter = 63
    column = 8
    row = cols
    while counter >= -1:  
        if counter % 8 == 7:
            print(row)
            print('------------------------------------')
            row = f' {column} |'
            column -= 1
        row += f' {BOARD[counter].type} |'
        counter -= 1


initialize_board()
display_board()
print(BOARD[8].legal_moves())
