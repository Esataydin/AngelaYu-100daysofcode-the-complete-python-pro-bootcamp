import tkinter


window = tkinter.Tk()
window.title("Disappearing Text App ")
window.minsize(width=1500, height=700)
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

text1, text2 = "", ""
# Configure as, after how many seconds you want text to get deleted.
TIME_LIMIT = 10
count_sec = TIME_LIMIT
timer = None


canvas = tkinter.Canvas(width=1500, height=700, bg=GREEN, highlightthickness=0)
text_label = canvas.create_text(750, 320, text="WRITE", fill='white', font=(FONT_NAME, 16, 'bold'))
timer_text = canvas.create_text(750, 280, text=f"Timer:{count_sec}", fill='darkgreen', font=(FONT_NAME, 16, 'bold'))
canvas.grid(column=1, row=1)

entry1 = tkinter.Entry(window, width=100)
entry1.grid(column=1, row=1, columnspan=500)


def count_down() -> None:
    global timer, text1, text2, count_sec

    # Timer doesn't count down until user writes anything.
    if entry1.get() == "":
        count_sec = TIME_LIMIT

    else:
        text1 = text2
        text2 = entry1.get()
        if count_sec > 0:
            # If user doesn't write anything in a short time, timer starts to count down and keeps track of any action from user.
            if text1 == text2:
                count_sec -= 1
            # If any action occurs, timer resets itself
            else:
                count_sec = TIME_LIMIT

    # If user doesn't write anything new in 5 seconds, the text in input gets deleted and timer resets.
    if count_sec == 0:
        entry1.delete(0, 'end')
        count_sec = TIME_LIMIT

    count_text = f'{count_sec}'
    canvas.itemconfig(timer_text, text=f'Timer:{count_text}')
    timer = window.after(1000, count_down)


def main() -> None:
    window.after(1000, count_down)
    window.mainloop()


if __name__ == '__main__':
    main()
