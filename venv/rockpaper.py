import os
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# Get directory where this script is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.title("Game Rock Paper and Scissor")
window.configure(background="black")

# Helper function to get correct image file paths
def get_image_path(filename):
    return os.path.join(BASE_DIR, filename)

# Load images using relative paths
image_rock1 = ImageTk.PhotoImage(Image.open(get_image_path("rock2.png")))
image_paper1 = ImageTk.PhotoImage(Image.open(get_image_path("paper2.png")))
image_scissor1 = ImageTk.PhotoImage(Image.open(get_image_path("scissor2.png")))
image_rock2 = ImageTk.PhotoImage(Image.open(get_image_path("rock1.png")))
image_paper2 = ImageTk.PhotoImage(Image.open(get_image_path("paper1.png")))
image_scissor2 = ImageTk.PhotoImage(Image.open(get_image_path("scissor1.png")))

Label_player = Label(window, image=image_scissor1)
Label_computer = Label(window, image=image_scissor2)
Label_computer.grid(row=1, column=0)
Label_player.grid(row=1, column=4)

computer_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
player_score = Label(window, text=0, font=("arial", 60, "bold"), fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

player_indicator = Label(window, font=("arial", 40, "bold"), text="PLAYER", bg="orange", fg="blue")
computer_indicator = Label(window, font=("arial", 40, "bold"), text="COMPUTER", bg="orange", fg="blue")
computer_indicator.grid(row=0, column=0)
player_indicator.grid(row=0, column=4)

def updateMessage(a):
    final_message["text"] = a

def computer_update():
    final = int(computer_score["text"])    
    final += 1
    computer_score["text"] = str(final)

def player_update():
    final = int(player_score["text"])    
    final += 1
    player_score["text"] = str(final) 

def winner_check(p, c):
    if p == c:
        updateMessage("It's a tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins !")
            computer_update()
        else:
            updateMessage("Player Wins !")
            player_update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins !")
            computer_update()
        else:
            updateMessage("Player Wins !")
            player_update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins !")
            computer_update()  # Fixed: Added missing ()
        else:
            updateMessage("Player Wins !")
            player_update()

to_select = ["rock", "paper", "scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0, 2)]
    
    if choice_computer == "rock":
        Label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        Label_computer.configure(image=image_paper2)
    else:
        Label_computer.configure(image=image_scissor2)

    if a == "rock":
        Label_player.configure(image=image_rock1)
    elif a == "paper":
        Label_player.configure(image=image_paper1)
    else:
        Label_player.configure(image=image_scissor1)

    winner_check(a, choice_computer)

final_message = Label(window, font=("arial", 40, "bold"), bg="red", fg="white")
final_message.grid(row=3, column=2)

button_rock = Button(window, width=16, height=3, text="ROCK", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("rock"))
button_rock.grid(row=2, column=1)

button_paper = Button(window, width=16, height=3, text="PAPER", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("paper"))
button_paper.grid(row=2, column=2)

button_scissor = Button(window, width=16, height=3, text="SCISSOR", font=("arial", 20, "bold"), bg="yellow", fg="red", command=lambda: choice_update("scissor"))
button_scissor.grid(row=2, column=3)

window.mainloop()