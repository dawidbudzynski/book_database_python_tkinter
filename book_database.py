from tkinter import *
from tkinter import messagebox

import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    view_command()
    messagebox.showinfo("Entry added", "Entry added")


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()
    messagebox.showinfo("Entry deleted", "Selected entry deleted")


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()
    messagebox.showinfo("Entry updated", "Selected entry updated")


window = Tk()
window.title('Book database')

l1 = Label(window, text='Title', width=50)
l1.grid(row=0, column=0)

l2 = Label(window, text='Author', width=50)
l2.grid(row=0, column=2)

l3 = Label(window, text='Year', width=50)
l3.grid(row=2, column=0)

l4 = Label(window, text='ISBN', width=50)
l4.grid(row=2, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text, width=50)
e1.grid(row=1, column=0)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text, width=50)
e2.grid(row=1, column=2)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text, width=50)
e3.grid(row=3, column=0)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text, width=50)
e4.grid(row=3, column=2)

list1 = Listbox(window, height=10, width=50)
list1.grid(row=4, column=0, rowspan=6)

sb1 = Scrollbar(window)
sb1.grid(row=4, column=1, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='View all', width=47, command=view_command)
b1.grid(row=4, column=2)

b2 = Button(window, text='Search entry', width=47, command=search_command)
b2.grid(row=5, column=2)

b3 = Button(window, text='Add entry', width=47, command=add_command)
b3.grid(row=6, column=2)

b4 = Button(window, text='Update selected', width=47, command=update_command)
b4.grid(row=7, column=2)

b5 = Button(window, text='Delete selected', width=47, command=delete_command)
b5.grid(row=8, column=2)

b6 = Button(window, text='Close', width=47, command=window.destroy)
b6.grid(row=9, column=2)

view_command()
window.mainloop()
