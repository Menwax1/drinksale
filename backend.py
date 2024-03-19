import tkinter
import gspread
import re

root = tkinter.Tk()
root.title("Drink Sale")
#gc = gspread.service_account(filename=r"C:\Users\waksm\Downloads\drinksaleapp.json")
gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")

sh = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1uRiz65hyUq0bcF1FSpKUb0coWActURXMXKHfB9hiLDg/"
    )

real_spread_sheet = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1w5IcUmBmAlOJwQCEcyrtSCvH5n7Il30Sy0r725q_B4k/edit?pli=1#gid=0"
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
            order = tuple[1]
            # Split the string on either a space or ':-'
            # order: name | type | index
            order_type = order.split('|')
            print(order_type)
            print(f"searching to {order_type[0]}, {order_type[1]}")
            index = order_type[2]
            if order_type[1] == "hotcocoa":
                print(f"Adding to {order_type[0]}, {order_type[1]}")
                previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"H{index}")
                real_spread_sheet.get_worksheet(0).update_acell(
                    f"H{index}", previous_hcs.numeric_value + 1
                )
            
            elif order_type[1] == "lemonade":
                print(f"Adding to {order_type[0]}, {order_type[1]}")
                previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"C{index}")
                real_spread_sheet.get_worksheet(0).update_acell(
                    f"C{index}", previous_hcs.numeric_value + 1
                )
            elif order_type[1] == "icetea":
                print(f"Adding to {order_type[0]}, {order_type[1]}")
                previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"E{index}")
                real_spread_sheet.get_worksheet(0).update_acell(
                    f"E{index}", previous_hcs.numeric_value + 1
                )
            elif order_type[1] == "special":
                print(f"Adding to {order_type[0]}, {order_type[1]}")
                previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"F{index}")
                real_spread_sheet.get_worksheet(0).update_acell(
                    f"F{index}", previous_hcs.numeric_value + 1
                )
            elif order_type[1] == "snocone":
                print(f"Adding to {order_type[0]}, {order_type[1]}")
                previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"H{index}")
                real_spread_sheet.get_worksheet(0).update_acell(
                    f"H{index}", previous_hcs.numeric_value + 1
                )

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
