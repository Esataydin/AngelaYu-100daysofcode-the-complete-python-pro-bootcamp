from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN: int = 25
SHORT_BREAK_MIN: int = 5
LONG_BREAK_MIN: int = 20
check_mark: str = '✔'
reps: int = 0
timer: Misc = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() -> None:
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer() -> None:
    global reps
    reps += 1

    work_sec: int = WORK_MIN * 60
    short_break_sec: int = SHORT_BREAK_MIN * 60
    long_break_sec: int = LONG_BREAK_MIN * 60

    # After time's up 4 times it'll give a long break
    if reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    # After time's up once it'll give a short break
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int) -> None:
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks.config(text=check_mark * (int(reps / 2)))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# It's for window icon
window.iconbitmap("tomato.ico")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(99.5, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 32, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# starts timer when it's clicked
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# resets timer when it's clicked
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
