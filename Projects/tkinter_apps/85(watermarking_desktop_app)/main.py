from PIL import Image, ImageTk, ImageDraw

from tkinter import filedialog
from tkinter import *


window = Tk()
window.title('Watermarking app')
window.minsize(width=400, height=200)
window.config(padx=35, pady=50)

my_font1 = ('times', 18, 'bold')
l1 = Label(window, text='Add The Photo You Want to Make Watermarked', width=50, font=my_font1)
l1.grid(row=1, column=1)
b1 = Button(window, text='Upload File', width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)


def upload_file() -> None:
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    width, height = img.width(), img.height()
    l2 = Label(window, text='Photo Watermarked', width=50, font=my_font1)
    l2.grid(row=3, column=1)
    watermarked_img = watermarker_maker(filename, size=(width, height))
    watermarked_img.show()


def watermarker_maker(image_path: str, size: tuple[int, int]) -> Image:
    filename = image_path.split("/")[-1]
    # Open an Image
    img = Image.open(image_path)

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    # TODO: use width and height to make watermark to scale to the picture
    # It's making watermark too small for now. It's a problem for big pictures
    width, height = size

    # Add Text to an image
    I1.text(xy=(10, 10), text="TEST", fill=(153, 255, 255))

    # Save the edited image
    img.save(f"watermarked_photos/{filename}")
    return img


def main() -> None:

    window.mainloop()


if __name__ == '__main__':
    main()
