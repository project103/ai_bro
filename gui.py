from Board import Board
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("4x4x4 Tic Tac Toe")

        self.board = Board()
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[[tk.Button(self.master, text='', width=4, height=2, command=lambda layer=l, row=r, col=c: self.make_move(layer, row, col))
                         for c in range(4)] for r in range(4)] for l in range(4)]

        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].grid(row=row + layer * 4, column=col + layer * 4, padx=5, pady=0)

        self.status_label = tk.Label(self.master, text=f"Current Player: {self.board.current_player}")
        self.status_label.grid(row=16, columnspan=4)
        self.reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=17, columnspan=4)
    def reset_game(self):
        self.board.reset_board()
        for layer in range(4):
            for row in range(4):
                for col in range(4):
                    self.buttons[layer][row][col].config(text='')
        self.update_status()

    def make_move(self, layer, row, col):
        if self.board.get_value(layer, row, col) == '':
            self.board.set_value(layer, row, col)
            self.buttons[layer][row][col].config(text=self.board.current_player)
            self.board.turn()
            self.update_status()

            if self.board.is_win('x') or self.board.is_win('O'):  # Corrected 'O' to 'o
                winner = 'Player X' if self.board.is_win('x') else 'Player O'
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.board.reset_board()

            if self.board.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.board.reset_board()

    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.board.current_player}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
