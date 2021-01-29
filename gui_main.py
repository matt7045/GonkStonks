#! python3
#boxes


#import tkinter as tk
from tkinter import *
import apiWrapper
root = Tk()

#display
canvas_main = Canvas(root, width=400, height=300)
canvas_main.pack()

#background image
stonks_pic = PhotoImage(file="stonks.gif")

#place image
canvas_main.create_image(50, 10, image=stonks_pic, anchor=NW)

#create quantity input box
quantity_entry = Entry(root)
canvas_main.create_window(200, 100, window=quantity_entry)
quantity = quantity_entry.get()

#quantity label
q_label = Label(root, text = 'quantity')
canvas_main.create_window(150, 100, window=q_label)

#create price input box
price_entry = Entry(root)
canvas_main.create_window(200, 140, window=price_entry)
price = price_entry.get()

#price label
p_label = Label(root, text = 'price')
canvas_main.create_window(150, 140, window=p_label)

#buttonCliked button
def buttonClicked():
    quantity           = int(quantity)
    price              = float(price)
    live_api_key_id    = None
    live_secret_key_id = None
    apiWrapper.limitBuy(live_api_key_id, live_secret_key, price, quantity)
button_clicked = Button(text = 'buy stonks', command = buttonClicked)
canvas_main.create_window(200, 180, window=button_clicked)


root.mainloop()
