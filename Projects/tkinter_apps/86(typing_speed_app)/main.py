import tkinter
import random

with open("words.txt", "r") as words_txt:
    words = words_txt.read().split("\n")

random.shuffle(words)
words_quarter = words[0:250]

window = tkinter.Tk()
window.title("Typing Speed Test")
window.minsize(width=1500, height=700)
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

count_sec = 60
space_number = 0
timer: int = None
words_to_display: str = ""


def change_text() -> None:
    global space_number
    words_to_display = ""
    # Gets next 10 words to display on screen while writing
    for word in words_quarter[space_number:space_number + 10]:
        words_to_display += word + " "
    canvas.itemconfig(text_label, text=words_to_display)


def count_spaces() -> None:
    global space_number
    window.after(300, count_spaces)
    space_number_ins = 0
    x1 = entry1.get()
    for letter in x1:
        if letter == " ":
            space_number_ins += 1
    space_number = space_number_ins
    if space_number % 10 == 0 and space_number != 0:
        change_text()


def count_down(count_sec: int):
    count = count_sec
    if count_sec == 0 or count_sec < 10:
        count = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'Timer:{count}')
    if count_sec > 0:
        global timer
        timer = window.after(1000, count_down, count_sec - 1)

    if count_sec == 0:
        score = 0
        # Disables input area when time is up
        entry1.config(state="disabled")
        text_entered = entry1.get()
        text_entered_array = text_entered.split()
        for index in range(len(text_entered_array)):
            if words_quarter[index] == text_entered_array[index]:
                score += 1
        # Changes timer text to score
        canvas.itemconfig(timer_text, text=f"Score:{score}")


canvas = tkinter.Canvas(width=1500, height=700, bg=GREEN, highlightthickness=0)
text_label = canvas.create_text(750, 320, text="", fill='white', font=(FONT_NAME, 16, 'bold'))
# Gets first 10 words
change_text()
timer_text = canvas.create_text(750, 280, text="Timer:60", fill='darkgreen', font=(FONT_NAME, 16, 'bold'))
canvas.grid(column=1, row=1)

entry1 = tkinter.Entry(window, width=100)
entry1.grid(column=1, row=1, columnspan=500)

window.after(3000, count_spaces)
window.after(1000, count_down, count_sec - 1)
window.mainloop()
