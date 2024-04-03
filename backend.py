import tkinter
import gspread
import re

root = tkinter.Tk()
root.title("Drink Sale")
#gc = gspread.service_account(filename=r"C:\Users\waksm\Downloads\drinksaleapp.json")
gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")

Keep_pick = tkinter.PhotoImage(file="assets/buttons for ds.png").subsample(16, 16)
cancel_pick = tkinter.PhotoImage(file="assets/buttons for ds (1).png").subsample(16, 16)
Reload = tkinter.PhotoImage(file="assets/buttons for ds (2).png").subsample(16,16)
marsch = tkinter.PhotoImage(file="assets/marsh.png").subsample(16,16)

sh = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1uRiz65hyUq0bcF1FSpKUb0coWActURXMXKHfB9hiLDg/"
    )

real_spread_sheet = gc.open_by_url(
        #"https://docs.google.com/spreadsheets/d/1w5IcUmBmAlOJwQCEcyrtSCvH5n7Il30Sy0r725q_B4k/edit?pli=1#gid=0"
        #real real
        #"https://docs.google.com/spreadsheets/d/1OgOKaxaLQMC1VgilqXOLMHad2Vlk0i4TgEzaXvT5464/edit#gid=0"
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
    orders = [f for f in enumerate(ws.col_values(1))][1::]
    # tuple is an index into the spreadsheet and the corresponding data for the order
    # return button to delete the order
    def make_order(tuple):
        order = tuple[1]
            # Split the string on either a space or ':-'
            # order: name | type | index
        order_type = order.split('|')
        print(order_type)
        print(f"searching to {order_type[0]}, {order_type[1]}")
        index = order_type[2]
        def marhmellow_order():
            previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"H{index}")
            real_spread_sheet.get_worksheet(0).update_acell(
            f"H{index}", previous_hcs.numeric_value + 1
            )   

            previous_hcs = real_spread_sheet.get_worksheet(0).acell(f"G{index}")
            real_spread_sheet.get_worksheet(0).update_acell(
            f"G{index}", previous_hcs.numeric_value + 1
            )
            ws.delete_rows(tuple[0]+1) 
            refresh()
            print(f"Adding to {order_type[0]}, {order_type[1]}")
        if order_type[1] == "hotcocoa":
            marshmallow_button = tkinter.Button(image=marsch, command= marhmellow_order)
            marshmallow_button.grid(row=(tuple[0]-1), column=2)
            buttons.append(marshmallow_button)
        def order_done():
            print(f"order done {tuple[1]}")
     

            if order_type[1] == "hotcocoa":

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
        def cancel():
            ws.delete_rows(tuple[0]+1) 
            refresh()
        order_button = tkinter.Button(text=tuple[1],  command=order_done)
        shut_up_button = I_dont_like_FORTNITE = tkinter.Button(image=cancel_pick,  command=cancel)
        
        return (order_button, shut_up_button)
    # lets say we have [1, 2 , 3]
    # lets say we have a function that takes in a number and adds 1 to it (add1)
    # [1,2,3].map(add1) = [2, 3, 4]

    orders = map(make_order, orders)
    button_row = 0
    for order in orders:
        # pack the confrim button
        buttons.append(order[0]) # we use brackets to get things from a tuple
        order[0].grid(row=button_row, column=0)
        # pack the cancel button for this order
        buttons.append(order[1]) # we use brackets to get things from a tuple
        order[1].grid(row=button_row, column=1)
        button_row = button_row +1
    brawl_stars_rocks = REALOAD = tkinter.Button(image=Reload,  command=refresh)
    STARCREDITS = tkinter.Label(text= real_spread_sheet.get_worksheet(0).acell(f"M6").value)
    buttons.append(STARCREDITS)
    REALOAD.grid(row=button_row)
    STARCREDITS.grid(row=button_row, column=1)
    buttons.append(REALOAD)

refresh()
    


root.after(1, refresh)

root.mainloop()