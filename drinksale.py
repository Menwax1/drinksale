import tkinter
import gspread


gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1w5IcUmBmAlOJwQCEcyrtSCvH5n7Il30Sy0r725q_B4k/edit?pli=1#gid=0")
root = tkinter.Tk()
root.title("Drink Sale")
#we are making print for graphical invirement
name_prompt=tkinter.Label(root, text="Enter Family Name")
name_prompt.grid(row=0, column=0)

name = tkinter.Entry(root)
name.grid(row=0,column=1)

actual_name=""
ictea_photo=tkinter.PhotoImage(file="assets/ice-tea.png")
photo=tkinter.PhotoImage(file="assets/snow-cone.png")
photolemonade=tkinter.PhotoImage(file="assets/lemonade.png")
photophoto=tkinter.PhotoImage(file="assets/cocoa.png")
go=tkinter.Button(root, text="Go")
def get_name():
   go.destroy()
   actual_name=name.get()
   name_prompt.destroy()
   name.destroy()
   tkinter.Label(root, text=actual_name).grid(row=0,column=0)
   tkinter.Label(root, text='balance: 20$').grid(row=0, column=1)
   tkinter. Button(root, text = 'Click Me !', image = ictea_photo).grid(row=5)   
   tkinter. Button(root, text = 'ClickMe !', image = photo).grid(row=15)
   tkinter. Button(root, text = 'Click Me!', image = photolemonade).grid(column= 1 , row=5)
   tkinter. Button(root, text = 'Click Me ', image = photophoto).grid(column= 1, row=15)

go["command"]=get_name




go.grid(column=2, row=0)



 


# tkinter.Label(root, text="What drink do you want?").grid(column=1)

# drink = tkinter.Entry(root)
# drink.grid(column=1)
# def get_drink():
#    tkinter.Label(root, text=drink.get()).grid(column=1)

# tkinter.Button(root, text="click me (:", command=get_drink).grid(column=1)


root.mainloop()
