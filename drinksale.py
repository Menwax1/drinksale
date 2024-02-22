import tkinter
import gspread

root = tkinter.Tk()
root.title("Drink Sale")
gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")
sh = gc.open_by_url(
        "https://docs.google.com/spreadsheets/d/1w5IcUmBmAlOJwQCEcyrtSCvH5n7Il30Sy0r725q_B4k/edit?pli=1#gid=0"
    )

ictea_photo = tkinter.PhotoImage(file="assets/ice-tea.png")
photo = tkinter.PhotoImage(file="assets/snow-cone.png")
photolemonade = tkinter.PhotoImage(file="assets/lemonade.png")
photophoto = tkinter.PhotoImage(file="assets/cocoa.png")
def make_order():
    print("in make order")

    # sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1OgOKaxaLQMC1VgilqXOLMHad2Vlk0i4TgEzaXvT5464/edit?pli=1#gid=0")

    # we are making print for graphical invirement

    count = 2
    button_list = []

    def get_name(name, index):
        def inner():
            print(name, index)
            for button in button_list:
                button.destroy()


            def delete_buttons():
                # destory button and labels
                hot_cocoa_buttom.destroy()
                name_label.destroy()
                balance_label.destroy()
                iced_tea_button.destroy()
                snow_cone_button.destroy()
                lemonade_button.destroy()
                # and restart
                make_order()

            def hotcocoa():
                previous_hcs = sh.get_worksheet(0).acell(f"H{index+1}")
                sh.get_worksheet(0).update_acell(
                    f"H{index+1}", previous_hcs.numeric_value + 1
                )
                delete_buttons()

            def PINKLEMONADE():
                previous_hcs = sh.get_worksheet(0).acell(f"C{index+1}")
                sh.get_worksheet(0).update_acell(
                    f"C{index+1}", previous_hcs.numeric_value + 1
                )
                delete_buttons()

            def ICETEA():
                print(index+1)
                previous_hcs = sh.get_worksheet(0).acell(f"E{index+1}")
                sh.get_worksheet(0).update_acell(
                    f"E{index+1}", previous_hcs.numeric_value + 1
                )
                delete_buttons()

            def SnoconeSpecial():
                previous_hcs = sh.get_worksheet(0).acell(f"F{index+1}")
                sh.get_worksheet(0).update_acell(
                    f"F{index+1}", previous_hcs.numeric_value + 1
                )
                delete_buttons()

            name_prompt.destroy()
            name_label = tkinter.Label(root, text=name)
            name_label.grid(row=0, column=0)
            balance = sh.get_worksheet(0).acell(f"J{index+1}")
            balance_label = tkinter.Label(root, text=f"balance: {balance.value}")
            balance_label.grid(row=0, column=1)
            iced_tea_button = tkinter.Button(
                root, text="Click Me !", image=ictea_photo, command=ICETEA
            )
            iced_tea_button.grid(row=5)
            snow_cone_button = tkinter.Button(
                root, text="ClickMe !", image=photo, command=SnoconeSpecial
            )
            snow_cone_button.grid(row=15)
            lemonade_button = tkinter.Button(
                root, text="Click Me!", image=photolemonade, command=PINKLEMONADE
            )
            lemonade_button.grid(column=1, row=5)
            hot_cocoa_buttom = tkinter.Button(
                root, text="Click Me ", image=photophoto, command=hotcocoa
            )
            hot_cocoa_buttom.grid(column=1, row=15)

        return inner

    families = sh.get_worksheet(0).col_values(1)[2::]
   #  families.sort()
    name_prompt = tkinter.Label(root, text="Click on YOUR Family Name")
    name_prompt.grid(row=0, column=0)
    count = 2
    for i in range(40 // 5):
        for j in range(5):
            index = i * 5 + j
            if len(families) > index:
               go = tkinter.Button(root, text=families[index], command=get_name(families[index], count))
               go.grid(row=i+1, column=j)
               button_list.append(go)
               count += 1




   #  go.grid(column=2, row=0)


# tkinter.Label(root, text="What drink do you want?").grid(column=1)

# drink = tkinter.Entry(root)
# drink.grid(column=1)
# def get_drink():
#    tkinter.Label(root, text=drink.get()).grid(column=1)

# tkinter.Button(root, text="click me (:", command=get_drink).grid(column=1)


root.after(1,make_order)
root.mainloop()

