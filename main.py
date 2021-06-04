# Password manager start

from tkinter import *
from PIL import ImageTk, Image


# ----------------- password generateor---------



# --------  save passrowrd ---------




#---- --------- UI  -------------
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)




canvas = Canvas(width=400, height=400)
tomato_img = ImageTk.PhotoImage(Image.open("lock.png"))
canvas.create_image(200, 200, image=tomato_img)
canvas.grid(row=0, column=1)


# Label
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
email_username_label = Label(text='Email/Username')
email_username_label.grid(row=2, column=0)
password_label = Label(text='Password')
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate password")
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()