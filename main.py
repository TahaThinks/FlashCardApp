from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI

window = Tk()
window.title("French/English Flash Card Game by TahaLearns")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Buttons
correct_button = Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
