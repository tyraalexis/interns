import tkinter
from tkinter import *
import tkinter.messagebox
import sqlite3


window = tkinter.Tk()
window.title("Grocery List")


def add_item():
    item = entry_item.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    if quantity == "":
        quantity = 1
        listbox_tasks.insert(tkinter.END, item)
        entry_item.delete(0,tkinter.END)
        listbox_tasks1.insert(tkinter.END, price)
        entry_price.delete(0,tkinter.END)
        listbox_tasks2.insert(tkinter.END, quantity)
        entry_price.delete(0,tkinter.END)
    elif item or price != "":
        listbox_tasks.insert(tkinter.END, item)
        entry_item.delete(0,tkinter.END)
        listbox_tasks1.insert(tkinter.END, price)
        entry_price.delete(0,tkinter.END)
        listbox_tasks2.insert(tkinter.END, quantity)
        entry_price.delete(0,tkinter.END)
    
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="Can not leave space blank.")
    
def delete_item():
    try:
        try:
            item_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(item_index) 
        except:
            price_index = listbox_tasks1.curselection()[0]
            listbox_tasks1.delete(price_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Must select item/price.")
        

    
def load_list():
    class main:
        def __init__(self,item,price):
            self.item = item
            self.price = price
    with open("item_cost.txt","r") as item_cost:
        lines = item_cost.readlines()
        items = []
        
    for l in lines:
        as_list = l.split(",")
        cow = main(as_list[0], as_list[1].replace("\n", ""))
        items.append(cow)
     
    for items in items:
        listbox_tasks.insert(tkinter.END, items.item)
        listbox_tasks1.insert(tkinter.END, items.price)
            
def multiple_yview(*args):
    listbox_tasks .yview(*args)
    listbox_tasks1 .yview(*args)
    listbox_tasks2 .yview(*args)




# Create GUI
frame_tasks = tkinter.Frame(window)
frame_tasks.pack()



listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)


listbox_tasks1 = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks1.pack(side=tkinter.LEFT)

listbox_tasks2 = tkinter.Listbox(frame_tasks, height=10, width=5)
listbox_tasks2.pack(side=tkinter.LEFT)


scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)


listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=multiple_yview)



item_label = tkinter.Label(text ="Item")
item_label.pack()
entry_item = tkinter.Entry(window, width = 50)
entry_item.pack()

price_label = tkinter.Label(text ="Price")
price_label.pack()
entry_price = tkinter.Entry(window, width = 50)
entry_price.pack()

quantity_label = tkinter.Label(text ="Quantity")
quantity_label.pack()
entry_quantity = tkinter.Entry(window, width = 5)
entry_quantity.pack()

button_add_item = tkinter.Button(window, text = "ADD ITEM", width=48, command=add_item)
button_add_item.pack()

button_delete_item = tkinter.Button(window, text = "DELETE ITEM", width=48, command=delete_item)
button_delete_item.pack()

button_load_list = tkinter.Button(window, text = "LOAD LIST", width=48, command=load_list)
button_load_list.pack()


window.mainloop()