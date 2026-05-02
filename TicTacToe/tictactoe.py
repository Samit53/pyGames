import tkinter as tk
from tkinter import messagebox

board = [""] * 9
current_player = "X"
scores = {"X": 0, "O": 0, "Draw": 0}

root = tk.Tk()
root.title("Tic Tac Toe")

score_label = tk.Label(root, text="", font=("Arial", 14))
score_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

def update_scoreboard():
    score_label.config(
        text=f"X: {scores['X']}   O: {scores['O']}   Draws: {scores['Draw']}"
    )

def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def on_click(i):
    global current_player

    if board[i] == "":
        board[i] = current_player

        # 🎨 Set color based on player
        color = "red" if current_player == "X" else "green"

        buttons[i].config(text=current_player, fg=color)

        result = check_winner()
        if result:
            if result == "Draw":
                scores["Draw"] += 1
                messagebox.showinfo("Result", "It's a Draw!")
            else:
                scores[result] += 1
                messagebox.showinfo("Result", f"Player {result} wins!")

            update_scoreboard()
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", fg="black")  # reset color

for i in range(9):
    btn = tk.Button(frame, text="", width=6, height=3,
                    font=("Arial", 24),
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Restart Game", command=reset_board)
reset_btn.pack(pady=10)

update_scoreboard()

root.mainloop()