import random
from tkinter import *

root = Tk()
root.title('Password Generator')
root.geometry('500x450')
root.configure(bg="beige")
root.resizable(False, False)

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbol = '!@#$%^&*_-+='

characters = alpha + numbers + symbol

Title = Label(root, text='Password Generator', bg='beige', fg='Black', font=('Arial', 25, 'bold'))
Title.pack(anchor="center", pady="20px")

Label_characters = Label(root, text='Select the Length of your Password : ', font=('Arial', 12 ), fg='blue', bg='beige')
Label_characters.place(x='20px', y='70px')
characters_length = Entry(root, font=('Arial', 12 , 'bold'))
characters_length.place(x='220px', y='70px')

def generate_password():
    length = characters_length.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text="Generator Password: " + password)


Button(root, text='Generate Password', command=generate_password , font=('Arial', 12 ), bg='orange').pack(pady=50)
label_password = Label(root, font=('Arial', 15 , 'bold'),fg='red', bg='beige')
label_password.pack(padx=10)

root.mainloop()