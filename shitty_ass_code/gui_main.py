#import tkinter as tk
from tkinter import *
import apiWrapper
root = Tk()

#display
canvas_main = Canvas(root, width=1294, height=744)
canvas_main.pack()

#background image
stonks_pic = PhotoImage(file="stonks.png")

#place image
canvas_main.create_image(0, 0, image=stonks_pic, anchor=NW)

#Account Id Label
ai_label = Label(root, text = 'API Key ID')
canvas_main.create_window(300, 60, window=ai_label)

#Account Id Input Box
api_key_entry = Entry(root)
canvas_main.create_window(400, 60, window=api_key_entry)

#Secret Key Label
s_label = Label(root, text = 'Secret Key')
canvas_main.create_window(300, 100, window=s_label)

#Secret Key input box
secret_key_entry = Entry(root)
canvas_main.create_window(400, 100, window=secret_key_entry)

#create quantity input box
quantity_entry = Entry(root)
canvas_main.create_window(400, 140, window=quantity_entry)


#quantity label
q_label = Label(root, text = 'quantity')
canvas_main.create_window(300, 140, window=q_label)

#create price input box
price_entry = Entry(root)
canvas_main.create_window(400, 180, window=price_entry)

#price label
p_label = Label(root, text = 'price')
canvas_main.create_window(300, 180, window=p_label)

#buttonCliked button
def buttonClicked():
    quantity           = int(quantity_entry.get())
    price              = round(float(price_entry.get()), 2)
    live_api_key_id    = str(api_key_entry.get())
    live_secret_key_id = str(secret_key_entry.get())
    try:
        apiWrapper.limitBuy(live_api_key_id, live_secret_key_id, price, quantity)
        done_label =Label(root, text = 'Placed an order to buy '+str(quantity)+' GME stonks.')
        canvas_main.create_window(370,280, window=done_label)
    except Exception as e:
        done_label =Label(root, text = 'Could not place order to buy '+str(quantity)+' GME stonks. See terminal for details.')
        canvas_main.create_window(370,280, window=done_label)
        print(e)
button_clicked = Button(text = 'buy stonks', command = buttonClicked)
canvas_main.create_window(300, 220, window=button_clicked)


root.mainloop()
