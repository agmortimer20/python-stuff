from tkinter import *
from random import randint

root = Tk()
root.geometry("640x480")
root.minsize(width=640, height=480)

round = IntVar(value=1)
point = IntVar()
images = []

for i in range(6):
    images.append(PhotoImage(file=f"./dice_pics/die-{i + 1}.png"))

def set_font(size = 12):
    return ("Times New roman", size)

def get_die_image(number):
    return images[number - 1]

def roll():
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    total_roll = roll1 + roll2

    
    die1_image.config(image=get_die_image(roll1))
    die2_image.config(image=get_die_image(roll2))

    if round.get() == 1:
        if total_roll == 7 or total_roll == 11:
            game_text.config(text=f"You rolled a {total_roll}. You WIN!")
        elif total_roll == 2 or total_roll == 12:
            game_text.config(text=f"You rolled a {total_roll}. You LOSE!")
        else:
            point.set(total_roll)
            round.set(2)
            game_text.config(text=f"You rolled a {total_roll}. The point is {point.get()}")
    elif round.get() == 2:
        pass


# Heading
heading = Frame(root)
heading.pack(pady=20)

Label(heading, text="Craps", font=set_font(24)).pack()
game_text = Label(heading, text="Click roll to start", font=set_font(16))
game_text.pack()
point_text = Label(heading, text="Point: -", font=set_font(16))
point_text.pack()
# End Heading

# Dice
dice_area = Frame(root)
dice_area.pack()

die1_image = Label(dice_area, image=get_die_image(1))
die1_image.pack(side="left", padx=5)

die2_image = Label(dice_area, image=get_die_image(1))
die2_image.pack(side="left", padx=5)
# End dice

# Controls
controls = Frame(root)
controls.pack(side="bottom", pady=25)

die_icon = PhotoImage(file="./dice_pics/die-icon.png")
play_button = Button(controls, text="Roll", image=die_icon, compound="left", font=set_font(16), command=roll)
play_button.pack(side="left", padx=5)
reset_button = Button(controls, text="New Game", state=["disabled"], font=set_font(16))
reset_button.pack(side="left", padx=5)
# End Controls

root.mainloop()