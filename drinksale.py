import tkinter
import gspread


gc = gspread.service_account(filename=r"C:\Users\mhdsc\Downloads\drinksaleapp.json")
sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1w5IcUmBmAlOJwQCEcyrtSCvH5n7Il30Sy0r725q_B4k/edit?pli=1#gid=0")
# sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1OgOKaxaLQMC1VgilqXOLMHad2Vlk0i4TgEzaXvT5464/edit?pli=1#gid=0")
root = tkinter.Tk()
root.title("Drink Sale")
#we are making print for graphical invirement
name_prompt=tkinter.Label(root, text="Enter Family Name")
name_prompt.grid(row=0, column=0)

count = 2
button_list = []
def get_name(name, index):
   def inner():
      
      for button in button_list:
         button.destroy()
      def delete_buttons():
         pass
      def hotcocoa(): 
         previous_hcs = sh.get_worksheet(0).acell(f'H{index+1}')
         sh.get_worksheet(0).update_acell(f'H{index+1}', previous_hcs.numeric_value+1)
      def PINKLEMONADE(): 
         previous_hcs = sh.get_worksheet(0).acell(f'C{index+1}')
         sh.get_worksheet(0).update_acell(f'C{index+1}', previous_hcs.numeric_value+1)
      def ICETEA(): 
         previous_hcs = sh.get_worksheet(0).acell(f'E{index+1}')
         sh.get_worksheet(0).update_acell(f'E{index+1}', previous_hcs.numeric_value+1)
      def SnoconeSpecial(): 
         previous_hcs = sh.get_worksheet(0).acell(f'F{index+1}')
         sh.get_worksheet(0).update_acell(f'F{index+1}', previous_hcs.numeric_value+1)
      name_prompt.destroy()
      balance = sh.get_worksheet(0).acell(f"J{index+1}")
      tkinter.Label(root, text=name).grid(row=0,column=0)
      tkinter.Label(root, text=f'balance: {balance.value}').grid(row=0, column=1)
      tkinter. Button(root, text = 'Click Me !', image = ictea_photo, command= ICETEA).grid(row=5)   
      tkinter. Button(root, text = 'ClickMe !', image = photo, command=SnoconeSpecial).grid(row=15)
      tkinter. Button(root, text = 'Click Me!', image = photolemonade, command= PINKLEMONADE).grid(column= 1 , row=5)
      tkinter. Button(root, text = 'Click Me ', image = photophoto, command=hotcocoa).grid(column= 1, row=15
      )
   return inner
for i in sh.get_worksheet(0).col_values(1)[2::]:
   go=tkinter.Button(root, text=i, command=get_name(i, count))
   go.grid(row=count-1)
   button_list.append(go)
   count += 1

ictea_photo=tkinter.PhotoImage(file="assets/ice-tea.png")
photo=tkinter.PhotoImage(file="assets/snow-cone.png")
photolemonade=tkinter.PhotoImage(file="assets/lemonade.png")
photophoto=tkinter.PhotoImage(file="assets/cocoa.png")

go.grid(column=2, row=0)



 


# tkinter.Label(root, text="What drink do you want?").grid(column=1)

# drink = tkinter.Entry(root)
# drink.grid(column=1)
# def get_drink():
#    tkinter.Label(root, text=drink.get()).grid(column=1)

# tkinter.Button(root, text="click me (:", command=get_drink).grid(column=1)


root.mainloop()
