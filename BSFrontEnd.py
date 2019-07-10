from tkinter import *
import BSBackEnd as backend

def view_command():
    print("command view")
    lb1.delete(0, END)
    for row in backend.view():
        lb1.insert(END,row)

def add_command():
    print("command add")
    backend.insert(e1_var.get(),e2_var.get(),e3_var.get(),e4_var.get())
    view_command()

def exit_command():
    print("command exit")
    sys.exit(1)

def curSelect(event):
    print("selected list")
    global selected_tuple
    index = lb1.curselection()[0]
    selected_tuple = lb1.get(index)
    e1_var.set(lb1.get(index)[1])
    e2_var.set(lb1.get(index)[2])
    e3_var.set(lb1.get(index)[3])
    e4_var.set(lb1.get(index)[4])


def search_command():
    print("command search")
    lb1.delete(0,END)
    for row in backend.search(e1_var.get(),e2_var.get(),e3_var.get(),e4_var.get()):
        lb1.insert(END,row)

def del_command():
    print("command delete")
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    print("command update")
    backend.update(selected_tuple[0],e1_var.get(),e2_var.get(),e3_var.get(),e4_var.get())
    view_command()

window = Tk()
window.title("BookStore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

e1_var = StringVar()
e1 = Entry(window,textvariable=e1_var)
e1.grid(row=0,column=1)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

e2_var = StringVar()
e2 = Entry(window,textvariable=e2_var)
e2.grid(row=0,column=3)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

e3_var = StringVar()
e3 = Entry(window,textvariable=e3_var)
e3.grid(row=1,column=1)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

e4_var = StringVar()
e4 = Entry(window,textvariable=e4_var)
e4.grid(row=1,column=3)

lb1 = Listbox(window,width=35,height=6)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

lb1.configure(yscrollcommand=sb1)
sb1.configure(command=lb1.yview)

lb1.bind('<<ListboxSelect>>',curSelect)

b1 = Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=del_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=exit_command)
b6.grid(row=7,column=3)

view_command()

window.mainloop()