from tkinter import *
from tkinter import ttk

root = Tk()

player_turn = StringVar(value="X")
grid_data = [["", "", ""], ["", "", ""], ["", "", ""]]
buttons = []

# Not finished
def check_draw() -> bool:
    for row in grid_data:
        for cell in row:
            if cell == "":
                return False
    
    return True

def check_winner(player_char) -> bool:
    for row in grid_data:
        if row[0] == row[1] == row[2] == player_char:
            return True

    for i in range(3):
        if grid_data[0][i] == grid_data[1][i] == grid_data[2][i] == player_char:
            return True

    if grid_data[0][0] == grid_data[1][1] == grid_data[2][2] == player_char:
        return True

    if grid_data[0][2] == grid_data[1][1] == grid_data[2][0] == player_char:
        return True

    return False

def select_cell(e):
    current_player = player_turn.get()

    e.widget.config(text=current_player, state=["disabled"])
    row = e.widget.grid_info().get("row")
    col = e.widget.grid_info().get("column")

    grid_data[row][col] = current_player

    if check_winner(current_player) == True:
        print(f"Player {current_player} wins!")
        for button in buttons:
            button.config(state=["disabled"])
            button.unbind("<ButtonPress>")
    else:
        # Switch Turn
        print(current_player)
        player_turn.set("O" if current_player == "X" else "X")

for i in range(3):
    for j in range(3):
        new_cell = ttk.Button(root)
        new_cell.bind("<ButtonPress>", select_cell)
        new_cell.grid(row=i, column=j, ipadx=25, ipady=25)
        buttons.append(new_cell)

root.mainloop()