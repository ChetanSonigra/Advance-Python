from tkinter import Tk, Button, Label, StringVar, Listbox, Scrollbar, Entry, W,E,S,N,END
from tkinter import ttk,messagebox
from sql_server_class import BookDB

db = BookDB()
selected_tuple = ''

def get_selected_row(event):
    global selected_tuple
    if books_list.curselection():
        index = books_list.curselection()[0]
        selected_tuple = books_list.get(index).split()
        print(selected_tuple)
        title_input.delete(0,END)
        title_input.insert('end',string=selected_tuple[1])
        author_input.delete(0,END)
        author_input.insert('end',string=selected_tuple[2])
        isbn_input.delete(0,END)
        isbn_input.insert('end',string=selected_tuple[3])
    

def view_records():
    books_list.delete(0,END)
    for row in db.view():
        books_list.insert(END,f"{row[0]}  {row[1]}  {row[2]}  {row[3]}")

def add_book():
    title = title_text.get()
    author = author_text.get()
    isbn = isbn_text.get()
    if title and author and isbn:
        db.insert(title,author,isbn)
    clear_screen()
    view_records()


def update_record():
    if books_list.curselection():
        title = title_text.get()
        author = author_text.get()
        isbn = isbn_text.get()
        index = selected_tuple[0]
        db.update(index,title,author,isbn)
        title_input.delete(0,END)
        author_input.delete(0,END)
        isbn_input.delete(0,END)
        view_records()
    else:
        messagebox.showinfo(title='Book Database',message='Select a record to modify')


def delete_record():
    if books_list.curselection():
        db.delete(selected_tuple[0])
    else:
        messagebox.showinfo(title='Book Database',message='Select a record to delete!')
    clear_screen()
    view_records()

def clear_screen():
    books_list.delete(0,END)
    title_input.delete(0,END)
    author_input.delete(0,END)
    isbn_input.delete(0,END)

def on_closing():
    global db
    if messagebox.askokcancel('Quit',"Do you want to quit?"):
        root.destroy()
        del db

root = Tk()
root.title('My Book Store')
root.config(background="light green",padx=20,pady=20)
root.geometry("850x500")

title = ttk.Label(root,text='Title',background="light green",font=("TkDefaultFont",16))
title.grid(row=0,column=0,sticky=E)
title_text = StringVar()
title_input = ttk.Entry(root,width=24,textvariable=title_text)
title_input.grid(row=0,column=1,sticky=W)

author = ttk.Label(root,text='Author',background="light green",font=("TkDefaultFont",16))
author.grid(row=0,column=2,sticky=E)
author_text = StringVar()
author_input = ttk.Entry(root,width=24,textvariable=author_text)
author_input.grid(row=0,column=3,sticky=W)

isbn = ttk.Label(root,text='ISBN',background="light green",font=("TkDefaultFont",16))
isbn.grid(row=0,column=4,sticky=E)
isbn_text = StringVar()
isbn_input = ttk.Entry(root,width=24,textvariable=isbn_text)
isbn_input.grid(row=0,column=5,sticky=W)

add_button = Button(root,text='ADD Book',bg='blue',fg='white',font="helvetica 10 bold",command=add_book)
add_button.grid(row=0,column=6)

books_list = Listbox(root,width=40,height=16,font="helvetica 13",bg="light blue",highlightthickness=0,selectmode='single')
books_list.grid(row=1,column=0,columnspan=12,sticky=W+E,padx=15,pady=40)
books_list.bind("<<ListboxSelect>>",get_selected_row)

scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1,column=8,rowspan=14,sticky=W)

books_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=books_list.yview)

view_btn = Button(root,text='View All Records',bg='black',fg='white',font='helvetica 10 bold',width=13,command=view_records)
view_btn.grid(row=15,column=1)

clear_btn = Button(root,text='Clear Screen',bg='maroon',fg='white',font='helvetica 10 bold',width=13,command=clear_screen)
clear_btn.grid(row=15,column=2)

exit_btn = Button(root,text='Exit Application',bg='blue',fg='white',font='helvetica 10 bold',width=13,command=on_closing)
exit_btn.grid(row=15,column=3)

modify_btn = Button(root,text='Modify Record',bg='purple',fg='white',font='helvetica 10 bold',width=13,command=update_record)
modify_btn.grid(row=15,column=4)

delete_btn = Button(root,text='Delete Record',bg='red',fg='white',font='helvetica 10 bold',width=13,command=delete_record)
delete_btn.grid(row=15,column=5)

root.resizable(False,False)
root.mainloop()