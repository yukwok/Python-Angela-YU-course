from tkinter import *
from PIL import ImageTk, Image
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
# print(to_learn)
# print(type(to_learn))

def next_card():
    current_item = random.choice(to_learn)
    # print(current_item)
    # print(type(current_item))
    french_word = current_item["French"]
    english_word = current_item["English"]

    print(french_word)
    print(english_word)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)


# ----- UI -----

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.config(padx=50, pady=50)


canvas = Canvas(width=800, height=526)
card_front_img = ImageTk.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150,text="Title", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,250,text="word", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


unknown_img = ImageTk.PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = ImageTk.PhotoImage(file="images/right.png")
known_button = Button(image=check_img,highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)




window.mainloop()
