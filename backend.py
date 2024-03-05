import tkinter
import gspread

root = tkinter.Tk()
root.title("Drink Sale")
gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")


sh = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1uRiz65hyUq0bcF1FSpKUb0coWActURXMXKHfB9hiLDg/"
    )


def refresh():
    root.destroy()
    root.__init__()

ws = sh.get_worksheet(0)
# orders = ws.col_values(1)[2::]
buttons = []
def refresh():
    for b in buttons:
        b.destroy()
    # root.destroy()
    # root.__init__()
    index  = 2
    orders = ws.col_values(1)[2::]
    for order in orders:
        check = tkinter.Button(text=order)
        def delete(): 
            check.destroy();
            ws.delete_rows(index)
            index = 2
            refresh()
   
        buttons.append(check)
        check["command"]= delete
        check.pack()

        index+=1
    


root.after(1, refresh)

root.mainloop()
