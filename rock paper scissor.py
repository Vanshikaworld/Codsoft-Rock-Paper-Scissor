import random
import tkinter as tkk


def game(choice):
    comp = random.randint(1, 3)
    result = ""
    comp_choice = ""
    comp_art = ""

    if comp == 1:
        comp_choice = "Rock"
        comp_art = rock_art
    elif comp == 2:
        comp_choice = "Paper"
        comp_art = paper_art
    else:
        comp_choice = "Scissors"
        comp_art = scissors_art

    if comp == choice:
        result = "It's a Tie"
    elif (comp == 1 and choice == 3) or (comp == 2 and choice == 1) or (comp == 3 and choice == 2):
        result = "You lose"
    else:
        result = "You won"
        game.count += 1

    result_text.set(f"Computer chose: {comp_choice}\n{comp_art}\n\n{result}\nYour total score is {game.count}")

def select_choice(choice):
    game(choice)


def calculate_window_height(num_elements):
    # Height of each element (buttons, ASCII art, labels, etc.)
    element_height = 180  # Adjust this value as needed

    # Padding between elements
    padding = 20

    # Additional space for score displnay
    score_height = 50

    # Calculate the total height required for all elements including score
    total_height = (num_elements * (element_height + padding)) + score_height

    return total_height


window = tkk.Tk()
window.title("Rock Paper Scissors Game")

# ASCII Art for Rock, Paper, Scissors
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)______
          _________)
       __________)
      (____)
---.__(___)
"""

choices = [("Rock", rock_art, 1), ("Paper", paper_art, 2), ("Scissors", scissors_art, 3)]
game.count = 0

result_text = tkk.StringVar()

# Calculate the required height of the window based on the number of choices
num_choices = len(choices)
window_height = calculate_window_height(num_choices)

# Set the window size to accommodate all elements without resizing
window.geometry(f"400x{window_height}")

# Fix window size and disable resizing
window.resizable(False, False)

# Create choice buttons with ASCII art
for choice, art, val in choices:
    button_frame = tkk.Frame(window)
    button_frame.pack(fill=tkk.X, padx=20, pady=5)

    label = tkk.Label(button_frame, text=choice, font=("Courier", 12))
    label.pack(side=tkk.LEFT, padx=10)

    canvas = tkk.Canvas(button_frame, width=100, height=100)
    canvas.pack(side=tkk.LEFT, padx=10)
    canvas.create_text(50, 50, text=art, anchor=tkk.CENTER)

    button = tkk.Button(button_frame, text="Choose", command=lambda val=val: select_choice(val))
    button.pack(side=tkk.RIGHT, padx=10)

# Create result label
result_label = tkk.Label(window, textvariable=result_text, font=("Courier", 12), justify=tkk.LEFT)
result_label.pack(pady=20)

window.mainloop()
