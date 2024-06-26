from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Read Data using Pandas
data = pandas.read_csv("data/french_words.csv")
data_dic = pandas.DataFrame.to_dict(data)
print(data_dic)

# UI

window = Tk()
window.title("French/English Flash Card Game by TahaLearns")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Add Text to the Canvas
canvas.create_text(400,150, font=LANGUAGE_FONT, text="French")
canvas.create_text(400,263, font=WORD_FONT, text=data_dic["French"][0])

correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Buttons

correct_button = Button(image=correct_image, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0)

correct_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)


window.mainloop()
