from tkinter import *

window = Tk()

'''
def km_to_miles():
    print("convert")
    miles = float(e1_var.get()) * 1.6
    t1.insert(END,miles)

b1 = Button(window,text="Run",command=km_to_miles)
#b1.pack()
b1.grid(row=0,column=0)

e1_var = StringVar()
e1 = Entry(window,textvariable=e1_var)
e1.grid(row=1,column=0)

t1 =  Text(window,width=20,height=1)
t1.grid(row=2,column=0)
'''

#l1_var=StringVar()
#l1 = Label(window,textvariable=l1_var)
l1 = Label(window,text="Kg")
l1.grid(row=0,column=0)
#l1_var.set("Kg")

e1_var = StringVar()
e1 = Entry(window,textvariable=e1_var)
e1.grid(row=0,column=1)


def kg_to_other():
    print("kgs")
    t1.delete("1.0",END)
    t1.insert(END,float(e1_var.get()) * 1000)
    t2.delete("1.0", END)
    t2.insert(END,float(e1_var.get()) * 2.20462)
    t3.delete("1.0", END)
    t3.insert(END,float(e1_var.get()) * 35.274)


b1 = Button(window,text="Run",command=kg_to_other)
b1.grid(row=0,column=2)


t1 = Text(window,width=20,height=1)
t1.grid(row=1,column=0)

t2 = Text(window,width=20,height=1)
t2.grid(row=1,column=1)

t3 = Text(window,width=20,height=1)
t3.grid(row=1,column=2)


window.mainloop()

