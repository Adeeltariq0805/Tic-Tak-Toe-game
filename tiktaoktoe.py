import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]["text"] != " ":
            button[combo[0]].config(bg="green")
            button[combo[1]].config(bg="green")
            button[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {button[combo[0]]['text']} wins!")
            break

def btn_clicked(index):
    global current_player
    if button[index]["text"] == " " and not winner:
        button[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s Turn")

def reset_game():
    global winner
    winner = False
    for btn in button:
        btn.config(text=" ", bg="SystemButtonFace")
    label.config(text="Player X's Turn")
    current_player = "X"

root = tk.Tk()
root.title("Tic-Tac-Toe")

button = [tk.Button(root, text=" ", font=("normal", 25), width=6, height=2, command=lambda i=i: btn_clicked(i)) for i in range(9)]

for i, btn in enumerate(button):
    btn.grid(row=i // 3, column=i % 3)

label = tk.Label(root, text="Player X's Turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

current_player = "X"
winner = False

reset_button = tk.Button(root, text="Restart Game", font=("normal", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
