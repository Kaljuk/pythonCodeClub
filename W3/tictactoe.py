class TicTacToe():
    def __init__(self):
        self.field = [
            ['', '', ''],  #  Row 0
            ['', '', ''],  #  Row 1
            ['', '', '']   #  Row 2
        ]
        self.state = 3
    # Check the game state, Game is over? Who won? Tie? Game is still unsfinished
    def checkState(self):
        field = self.field
        state = 3
        # Check for both players
        for p in ['O', 'x']:
            win = 0
            # - Horizontal -
            for row in field:
                win = sum([1*(r == p) for r in row]) == 3
            # | Vertical |
            for col in range(3):
                columns = [ field[0][col], field[1][col], field[2][col] ]
                win = sum([1*(c == p) for c in columns]) == 3 or win
            # \ Diagonal /
            diagP = [ field[0][0], field[1][1], field[2][2] ]
            diagS = [ field[0][2], field[1][1], field[2][0] ]
            win = sum([1*(c == p) for c in diagP]) == 3 or win
            win = sum([1*(c == p) for c in diagS]) == 3 or win
            if win:
                self.state = 1*(p == 'x')
                return self.state
        # Check if tie
        tie = (sum([sum(r != '' for r in row) for row in field]) == 9)*2
        self.state = tie if tie else state

    def add_move(self, row, col, player):
        self.field[row][col] = player
        

    # 0 - Player with O's won
    # 1 - Player with X's won
    # 2 - It is a tie 
    # 3 - Game is still unfinished
    def get_state(self):
        self.checkState()
        return self.state

    def showField(self):
        print("Field:", self.field)

# t = TicTacToe()
# t.add_move(0,0,'x')
# t.add_move(0,1,'O')
# t.add_move(0,2,'x')

# t.add_move(1,0,'O')
# t.add_move(1,1,'x')
# t.add_move(1,2,'O')

# t.add_move(2,0,'O')
# t.add_move(2,1,'x')
# t.add_move(2,2,'O')
# t.add_move(2,2,'x')

# t.showField()
# print(t.get_state())