import tkinter as tk
import random
from time import sleep

class SnakeLadderGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake and Ladder")
        
        # Board size
        self.board_size = 10
        self.cell_size = 50
        
        # Snakes and Ladders
        self.snakes = {97: 78, 95: 56, 88: 24, 62: 18, 36: 6}
        self.ladders = {2: 38, 4: 14, 8: 30, 28: 76, 58: 84}
        
        # Player Positions
        self.player_positions = {"Player": 1, "AI": 1}
        self.current_turn = "Player"
        
        # UI Setup
        self.canvas = tk.Canvas(self.window, width=500, height=550)
        self.canvas.pack()
        self.draw_board()
        
        # Dice Roll Button
        self.dice_label = tk.Label(self.window, text="Roll: ?", font=("Arial", 16))
        self.dice_label.pack()
        self.roll_button = tk.Button(self.window, text="Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack()

        self.window.mainloop()

    def draw_board(self):
        """ Draws a 10x10 board with numbers """
        self.canvas.delete("all")
        color1, color2 = "#DDDDDD", "#FFFFFF"
        for row in range(self.board_size):
            for col in range(self.board_size):
                num = (self.board_size - row - 1) * self.board_size + (col + 1) if row % 2 == 0 else (self.board_size - row) * self.board_size - col
                color = color1 if (row + col) % 2 == 0 else color2
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.canvas.create_text(x1 + 25, y1 + 25, text=str(num), font=("Arial", 12))
        
        # Draw Player and AI positions
        self.update_positions()

    def update_positions(self):
        """ Update player markers on the board """
        for player, pos in self.player_positions.items():
            row, col = self.get_coordinates(pos)
            color = "blue" if player == "Player" else "red"
            self.canvas.create_oval(col * self.cell_size + 10, row * self.cell_size + 10,
                                    col * self.cell_size + 40, row * self.cell_size + 40,
                                    fill=color, tags=player)

    def get_coordinates(self, pos):
        """ Converts board number to (row, col) position """
        row = 9 - (pos - 1) // 10
        col = (pos - 1) % 10 if row % 2 != 9 % 2 else 9 - (pos - 1) % 10
        return row, col

    def roll_dice(self):
        """ Roll a dice and move the player """
        roll = random.randint(1, 6)
        self.dice_label.config(text=f"Roll: {roll}")
        self.move_player(roll)

    def move_player(self, roll):
        """ Moves the player based on dice roll """
        current_pos = self.player_positions[self.current_turn]
        new_pos = current_pos + roll
        if new_pos > 100:
            return  # Don't move if out of bounds

        # Check for Snakes or Ladders
        if new_pos in self.snakes:
            new_pos = self.snakes[new_pos]
        elif new_pos in self.ladders:
            new_pos = self.ladders[new_pos]

        self.player_positions[self.current_turn] = new_pos
        self.draw_board()

        # Check for win
        if new_pos == 100:
            self.roll_button.config(state=tk.DISABLED)
            self.dice_label.config(text=f"{self.current_turn} Wins!")
            return
        
        # Switch turn
        self.current_turn = "AI" if self.current_turn == "Player" else "Player"

        # AI Move
        if self.current_turn == "AI":
            self.window.after(1000, self.ai_move)

    def ai_move(self):
        """ AI plays automatically """
        roll = random.randint(1, 6)
        self.dice_label.config(text=f"AI Rolls: {roll}")
        self.move_player(roll)

if __name__ == "__main__":
    SnakeLadderGame()