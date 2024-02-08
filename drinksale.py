import tkinter

root = tkinter.Tk()
root.title("Drink Sale")
#we are making print for graphical invirement
tkinter.Label(root, text="Enter your name").grid(row=0, column=0)

name = tkinter.Entry(root)
name.grid(row=0,column=1)

def get_name():
   label_to_be_deleted = tkinter.Label(root, text=name.get())
   label_to_be_deleted.grid(row=5, column=4)
tkinter.Button(root, text="click me (:", command=get_name).grid(column=2, row=0)



tkinter.Label(root, text="What drink do you want?").grid(column=1)

drink = tkinter.Entry(root)
drink.grid(column=1)
def get_drink():
   tkinter.Label(root, text=drink.get()).grid(column=1)

tkinter.Button(root, text="click me (:", command=get_drink).grid(column=1)

root.mainloop()
