"""
Command Line Chess
2022 August 
Alexander Michael Pommer Alba
"""

BOARD = [] # 1d board that stores instances of Squares or Pieces
UCI_map = {} # Universal Chess Interface dictionary to map player input
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
counter = 0
for number in range(1,9):
    for letter in LETTERS:
        UCI_map[f'{letter}{number}'] = counter
        counter += 1

class Square:

    def __init__(self, position: int, color: str, type_: str) -> None:
        self.position = position # 0 to 63
        self.color = color # 'Black', 'White' or 'Empty'
        self.type_ = type_

    def is_empty(self) -> bool:
        return self.color == "Empty"

class Pawn(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)

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
            # Not in far right column 'h' and enemy piece in position
            if self.position % 8 != 7 and BOARD[capture_right].is_empty() == False and BOARD[capture_right].color != self.color:
                legal.append(capture_right)
            
            capture_left = self.position + 7
            # Not in far left column 'a' and enemy piece in position
            if self.position % 8 != 0 and BOARD[capture_left].is_empty() == False and BOARD[capture_left].color != self.color:
                legal.append(capture_left)

            # TODO promotion
                
            return legal    

        if self.color == 'Black':

            one_step = self.position - 8
            if one_step >= 0 and BOARD[one_step].is_empty():
                legal.append(one_step)

            two_steps = self.position - 16
            if self.position in range(48, 56) and BOARD[two_steps].is_empty():
                legal.append(two_steps)
                # TODO en passant

            capture_right = self.position - 7
            # Not in far right column 'h' and enemy piece in position
            if self.position % 8 != 7 and BOARD[capture_right].is_empty() == False and BOARD[capture_right].color != self.color:
                legal.append(capture_right)

            capture_left = self.position - 9
            # Not in far left column 'a' and enemy piece in position
            if self.position % 8 != 0 and BOARD[capture_left].is_empty() == False and BOARD[capture_left].color != self.color:
                legal.append(capture_left)
            
            # TODO promotion

            return legal  

class King(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)

class Queen(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)

class Rook(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)

    def legal_moves(self):
        legal = []

        for up in range(self.position - 8, 0, -8):

            if BOARD[up].color != self.color:
                legal.append(up)
            
            if BOARD[up].is_empty() == False:
                break

        for down in range(self.position + 8, 64, 8):

            if BOARD[down].color != self.color:
                legal.append(down)
            
            if BOARD[down].is_empty() == False:
                break

        for left in range(self.position, ((self.position//8) * 8) - 1, -1):
            
            if BOARD[left].color != self.color:
                legal.append(left)

            if BOARD[left].is_empty == False:
                break

        for right in range(self.position, (self.position//8) * 8 + 8):
            
            if BOARD[right].color != self.color:
                legal.append(right)

            if BOARD[right].is_empty == False:
                break

        return legal

class Knight(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)

class Bishop(Square):

    def __init__(self, position: int, color: str, type_: str) -> None:
        super().__init__(position, color, type_)


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

    print('\n'*24) # clear screen

    files = '   |' # columns header
    for letter in LETTERS:
        files += f' {letter} |'
    print(files)

    for rank in range(1, 9): # rows
        ranks = f' {rank} |'
        for sq in range(rank * 8 - 8, rank * 8):
            ranks += f' {BOARD[sq].type_} |'
        print('------------------------------------')
        print(ranks)
    print('   ---------------------------------')
    print('\n'*4)

def player_input(turn_color):

    while True:
        try:
            
            input_text = input(f"{turn_color} player move (e.g. 'c2c4'): ")
            print("test0", input_text, UCI_map[input_text[:2]])
            selected_piece = BOARD[UCI_map[input_text[:2]]]
            print("test1", selected_piece)

            if turn_color == selected_piece.color:
                
                move_from = selected_piece.position
                move_to = BOARD[UCI_map[input_text[-2:]]].position
                legal = selected_piece.legal_moves()
                print("test3", 'from:', move_from, 'to:', move_to, 'legal:', legal)
                if move_to in legal:
                    print("test4 is legal")
                    
                    if move_to == 'castle':
                        # TODO 
                        pass

                    elif move_to == 'promotion':
                        # TODO
                        pass

                    # TODO check if king is threatened
                    
                    else:
                        BOARD[move_from], BOARD[move_to] = Square(move_from, 'Empty', ' '), type(selected_piece)(move_to, selected_piece.color, selected_piece.type_)
                    
                    display_board()

                    if turn_color == 'White':
                        return player_input('Black')
                    else:
                        return player_input('White')

        except:
            pass

# Start the game
initialize_board()
display_board()
player_input('White')
