from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()
