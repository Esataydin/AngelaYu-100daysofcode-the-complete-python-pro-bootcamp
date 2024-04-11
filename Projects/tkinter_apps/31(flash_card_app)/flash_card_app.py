import pandas

from tkinter import *
import random


try:
    data: pandas.core.frame.DataFrame = pandas.read_csv('data/words_to_learn.csv')
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data: pandas.core.frame.DataFrame = pandas.read_csv('data/french_words.csv')

words: pandas.core.frame.DataFrame = data.copy()
words_list: list[dict[str, str]] = words.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"
timer: Misc = None
word: dict[str, str] = {}


# ----------------------CREATE NEW CARDS----------------#
def new_card() -> None:
    global timer, word, words_list
    window.after_cancel(timer)
    canvas.itemconfig(card, image=card_back_photo)
    word = random.choice(words_list)
    canvas.itemconfig(language_text, text='French', fill='white')
    canvas.itemconfig(word_text, text=word['French'], fill='white')
    timer = window.after(3000, flip_card)


def known() -> None:
    global word, words_list
    words_list.remove(word)
    df_words_list = pandas.DataFrame(words_list)
    df_words_list.to_csv('data/words_to_learn.csv', index=False)
    new_card()


# -------------------------FLIP CARDS---------------------#
def flip_card() -> None:
    canvas.itemconfig(card, image=card_front_photo)
    canvas.itemconfig(language_text, text='English', fill='black')
    canvas.itemconfig(word_text, text=word['English'], fill='black')


# -----------------------------UI---------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_photo = PhotoImage(file='images/card_front.png')

card_back_photo = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=card_back_photo)

language_text = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

wrong_photo = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_photo, highlightthickness=0, bd=0, command=new_card)
wrong_button.grid(column=0, row=1)

right_photo = PhotoImage(file='images/right.png')
right_button = Button(image=right_photo, highlightthickness=0, bd=0, command=known)
right_button.grid(column=1, row=1)

timer = window.after(3000, flip_card)
new_card()

window.mainloop()