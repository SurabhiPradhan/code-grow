"""
A program that stores all the books/novels information.
LABELS: [Title, Year, Author,
Identification number(IDN), Rating,Summary/review]

Functions(Buttons) it can perform:
Search,
View(Listbox),
Add,
Update,
Delete,
Close

Scrollbar for Listbox
Scrollbar for Summary
"""

from tkinter import *
import bookdb

                                   #Wrapper Functions
def get_selected_row(event):           # special parameter'event' that holds info about the type of event.
    try:
        global selected_entry
        index=booklist.curselection()[0]
        selected_entry=booklist.get(index)
        Et.delete(0,END)
        Et.insert(END,selected_entry[0])
        Ey.delete(0,END)
        Ey.insert(END,selected_entry[1])
        Er.delete(0,END)
        Er.insert(END,selected_entry[2])
        Ea.delete(0,END)
        Ea.insert(END,selected_entry[3])
        Ei.delete(0,END)
        Ei.insert(END,selected_entry[4])
        Es.delete(0,END)
        Es.insert(END,selected_entry[5])
    except IndexError:
        pass


def view_command():
    booklist.delete(0,END)
    for row in bookdb.view():
        booklist.insert(END,row)

def search_command():
    booklist.delete(0,END)
    for row in bookdb.search(title_text.get(),year_text.get(),author_text.get(),ISBN_text.get()):
        booklist.insert(END,row)

def add_command():
    bookdb.insert(title_text.get(),year_text.get(),rating_text.get(),author_text.get(),ISBN_text.get(),sum_text.get())
    booklist.delete(0,END)
    booklist.insert(END,(title_text.get(),year_text.get(),rating_text.get(),author_text.get(),ISBN_text.get(),sum_text.get()))

def delete_command():
    bookdb.delete(selected_entry[4])

def update_command():
    bookdb.update(title_text.get(),year_text.get(),rating_text.get(),author_text.get(),sum_text.get(),ISBN_text.get())


window = Tk()
window.wm_title("Library")
                                          # Creating 6 LABELS(static widgets)
Lt = Label(window,text="Title")
Lt.grid(row=0,column=0)

Ly = Label(window,text="Year")
Ly.grid(row=0,column=2)

Lr = Label(window,text="Rating")
Lr.grid(row=0,column=4)

La = Label(window,text="Author")
La.grid(row=1,column=0)

Li = Label(window,text="ISBN")
Li.grid(row=1,column=2)

Ls = Label(window,text="Summary")
Ls.grid(row=1,column=4)

                                          #Creating Entry
title_text = StringVar()             #function that creates spatial object for the datatype.
Et = Entry(window,textvariable=title_text,borderwidth=5)
Et.grid(row=0,column=1)

year_text = StringVar()
Ey = Entry(window,textvariable=year_text,borderwidth=5)
Ey.grid(row=0,column=3)

rating_text = StringVar()
Er = Entry(window,textvariable=rating_text,borderwidth=5)
Er.grid(row=0,column=5)

author_text = StringVar()
Ea = Entry(window,textvariable=author_text,borderwidth=5)
Ea.grid(row=1,column=1)

ISBN_text = StringVar()
Ei = Entry(window,textvariable=ISBN_text,borderwidth=5)
Ei.grid(row=1,column=3)

sum_text = StringVar()
Es = Entry(window,textvariable=sum_text,width=20,borderwidth=5)
Es.grid(row=1,column=5)

                                           #Creating Listbox and scrollbar
                                          # Applying configure method to the Listbox and Scrollbar object
                                          # 'y' depicts vertical view or along y-axis
booklist = Listbox(window,height=15,width=55,borderwidth=2)
booklist.grid(row=2,column=0,rowspan=10,columnspan=4)
scb = Scrollbar(window)
scb.grid(row=2,column=4,rowspan=10)


booklist.configure(yscrollcommand=scb.set)
scb.configure(command=booklist.yview)

                                       # bind() binds the widget event to a function, takes two parameters: event type and the function that we want to bind
booklist.bind('<<ListboxSelect>>',get_selected_row)

                                               # Creating Buttons
B1 = Button(window,text="View All",height=2,width=20,command=view_command)
B1.grid(row=2,column=5)

B2 = Button(window,text="Search",height=2,width=20,command=search_command)
B2.grid(row=3,column=5)

B3 = Button(window,text="Add",height=2,width=20,command=add_command)
B3.grid(row=4,column=5)

B4 = Button(window,text="Update",height=2,width=20,command=update_command)
B4.grid(row=5,column=5)

B5 = Button(window,text="Delete",height=2,width=20,command=delete_command)
B5.grid(row=6,column=5)

B6 = Button(window,text="Close",height=2,width=20,command=window.destroy)
B6.grid(row=7,column=5)


window.mainloop()
