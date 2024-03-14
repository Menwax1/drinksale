import tkinter
import gspread

root = tkinter.Tk()
root.title("Drink Sale")
#gc = gspread.service_account(filename=r"C:\Users\waksm\Downloads\drinksaleapp.json")
gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")

sh = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1uRiz65hyUq0bcF1FSpKUb0coWActURXMXKHfB9hiLDg/"
    )


def refresh():
    root.destroy()
    root.__init__()

ws = sh.get_worksheet(0)
tuple = (1, 2)

# orders = ws.col_values(1)[2::]
buttons = []
def refresh():
    print("data")
    for b in buttons:
        b.destroy()
    # root.destroy()
    # root.__init__()
    # index  = 2
    # enumarate
    # lets say we have ["a", "b", "c"]
    # calling enumerate 
    # [.. (2, "c")]
    orders = [f for f in enumerate(ws.col_values(1))][2::]
    # tuple is an index into the spreadsheet and the corresponding data for the order
    # return button to delete the order
    def make_order(tuple):
        def order_done():
            print(f"order done {tuple[1]}")

            ws.delete_rows(tuple[0]+1)
            refresh()
        order_button = tkinter.Button(text=tuple[1],  command=order_done)
        return order_button
    # lets say we have [1, 2 , 3]
    # lets say we have a function that takes in a number and adds 1 to it (add1)
    # [1,2,3].map(add1) = [2, 3, 4]
    orders = map(make_order, orders)
    for order in orders:
        buttons.append(order)
        order.pack()

    


root.after(1, refresh)

root.mainloop()
