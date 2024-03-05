import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("800x600")
        self.root.config(bg="#121212")  # Set background color to dark gray

        self.frame = tk.Frame(self.root, bg="#121212")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

        # Initialize game variables
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game_over = False

    def create_widgets(self):
        self.label = tk.Label(self.frame, text="Tic Tac Toe", font=("Helvetica", 24), fg="white", bg="#121212")
        self.label.pack(pady=20)

        self.board_frame = tk.Frame(self.frame, bg="#121212")
        self.board_frame.pack()

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.board_frame, text=" ", font=("Helvetica", 20), width=6, height=3,
                                   command=lambda x=i, y=j: self.make_move(x, y),
                                   bg="#1f1f1f", fg="white", activebackground="#3a3a3a", activeforeground="white")
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.frame, text="Restart", font=("Helvetica", 16), command=self.restart,
                                      bg="#1f1f1f", fg="white", activebackground="#3a3a3a", activeforeground="white")
        self.reset_button.pack(pady=10)

    def make_move(self, x, y):
        if self.board[x][y] == " " and not self.game_over:
            self.board[x][y] = self.current_player
            self.buttons[x][y]['text'] = self.current_player
            if self.check_win(x, y):
                messagebox.showinfo("Winner", f"{self.current_player} Wins!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, x, y):
        # Check row
        if self.board[x][0] == self.board[x][1] == self.board[x][2] != ' ':
            return True
        # Check column
        if self.board[0][y] == self.board[1][y] == self.board[2][y] != ' ':
            return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ') or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j]['text'] = " "
        self.label.config(text="Tic Tac Toe")
        self.current_player = 'X'
        self.game_over = False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
