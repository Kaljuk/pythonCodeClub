class TicTacToe():

    def __init__(self):
        self.field = [
            ['', '', ''], # Row 0
            ['', '', ''], # Row 1
            ['', '', '']  # Row 2
        ]

    def add_move(self, row, col, player):
        self.field[row][col] = player

    # 0 - Player with O's won
    # 1 - Player with X's won
    # 2 - It is a tie 
    # 3 - Game is still unfinished
    def get_state(self):
        state = 3
        # Rows
        for row in self.field:
            state = 0 if (set(row) == {'O'}) else 1 if (set(row) == {'x'}) else state
        # Columns
        for col in range(len(self.field)):
            state = 0 if (self.field[0][col] == 'O' and self.field[1][col] == 'O' and self.field[2][col] == 'O') else state
            state = 1 if (self.field[0][col] == 'x' and self.field[1][col] == 'x' and self.field[2][col] == 'x') else state
        # Diagonals O
        state = 0 if (self.field[0][0] == 'O' and self.field[1][1] == 'O' and self.field[2][2] == 'O') else state
        state = 0 if (self.field[2][0] == 'O' and self.field[1][1] == 'O' and self.field[0][2] == 'O') else state
        # Diagonals x
        state = 1 if (self.field[0][0] == 'x' and self.field[1][1] == 'x' and self.field[2][2] == 'x') else state
        state = 1 if (self.field[2][0] == 'x' and self.field[1][1] == 'x' and self.field[0][2] == 'x') else state
        
        # Check if TIE
        if (state == 3):
            if (('' not in self.field[0]) and ('' not in self.field[1]) and ('' not in self.field[2])):
                state = 2
        return state

# t = TicTacToe()
# t.add_move(0,0,'O')
# t.add_move(0,1,'x')
# t.add_move(0,2,'O')
# t.add_move(1,0,'x')
# t.add_move(1,1,'O')
# t.add_move(1,2,'x')
# t.add_move(2,0,'x')
# t.add_move(2,1,'O')
# t.add_move(2,2,'x')
# print(t.get_state())