import tkinter as tk
import heapq

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe AI")
        self.board = [' '] * 9
        self.current_player = 'O'  # Human plays first
        self.buttons = [tk.Button(self.window, text=' ', font=('Arial', 20), height=3, width=6, 
                                  command=lambda i=i: self.make_move(i)) for i in range(9)]
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i].grid(row=row, column=col)

    def make_move(self, position):
        if self.board[position] == ' ' and self.current_player == 'O':  # Player's move
            self.board[position] = 'O'
            self.buttons[position].config(text='O', state=tk.DISABLED)
            
            if self.is_winner('O'):
                self.display_winner('O')
                return
            elif self.is_draw():
                self.display_winner('Draw')
                return

            self.current_player = 'X'
            self.ai_move()

    def ai_move(self):
        move = self.a_star()
        if move is not None:
            self.board[move] = 'X'
            self.buttons[move].config(text='X', state=tk.DISABLED)

            if self.is_winner('X'):
                self.display_winner('X')
                return
            elif self.is_draw():
                self.display_winner('Draw')
                return

        self.current_player = 'O'

    def is_winner(self, player):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        return ' ' not in self.board

    def display_winner(self, winner):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)  # Disable all buttons
        result = f"Player {winner} wins!" if winner != 'Draw' else "It's a Draw!"
        label = tk.Label(self.window, text=result, font=('Arial', 16))
        label.grid(row=3, column=0, columnspan=3)

    def get_valid_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def heuristic(self, player):
        opponent = 'O' if player == 'X' else 'X'
        return sum(self.board[i] == player for i in range(9)) - sum(self.board[i] == opponent for i in range(9))

    def a_star(self):
        priority_queue = []
        for move in self.get_valid_moves():
            self.board[move] = 'X'
            score = self.heuristic('X')
            heapq.heappush(priority_queue, (-score, move))
            self.board[move] = ' '
        return heapq.heappop(priority_queue)[1] if priority_queue else None

if __name__ == "__main__":
    TicTacToe()