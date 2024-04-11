from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# --------------------PASSWORD GENERATOR------------------------#
def generate_password() -> None:
    password_entry.delete(0, 'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters: int = random.randint(8, 10)
    nr_symbols: int = random.randint(2, 4)
    nr_numbers: int = random.randint(2, 4)

    password_list_letters: list[str] = [random.choice(letters) for _ in range(nr_letters)]
    password_list_symbols: list[str] = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list_numbers: list[str] = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list_letters + password_list_symbols + password_list_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # It copies the password you created with code. You can just ctrl+v and paste it from anywhere you want
    pyperclip.copy(password)


# ----------------------SAVE PASSWORD----------------------------#
def save() -> None:
    website = website_entry.get().capitalize()
    email = email_entry.get().lower()
    password = password_entry.get()
    new_data: dict[str, dict[str, str]] = {
        website: {'email': email,
                  'password': password
                  }
    }
    if website == '' or email == '' or password == '':
        messagebox.showwarning(title='Oops', message='Please don\'t leave any fields empty.')
    else:
        is_ok: bool = messagebox.askokcancel(title=website,
                                             message=f'These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it okay to save?')
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------FIND PASSWORD-------------------#
def find_password() -> None:
    website: str = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data: dict[str, dict[str, str]] = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message='No data file found.')
    else:
        if website in data:
            email: str = data[website]["email"]
            password: str = data[website]["password"]
            messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                       f'Password: {password}')
        else:
            messagebox.showwarning(title=website, message='No details for the website.')


# -----------------------UI DESIGN-------------------#

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'YOUR EMAIL/USERNAME')

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Generates a password when it's clicked
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3)

# Writes details on data.json when it's clicked
add_button = Button(text='Add', width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Searches password for written website when it's clicked
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()