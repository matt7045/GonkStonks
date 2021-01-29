#! python3

from tkinter import *
root = Tk()

class Window:
    def __init__(self, name):
        self.name = name

    def createWindow(self):
        self.name = Canvas(root, width=400, height=300)
        self.name.pack()

    def addImage(self, pic_name, pic_file):
        pic_name = Window(pic_file, pic_name)
        self.name.create_image(50, 10, image=pic_file, anchor=NW)

    def makeInputBox(self, input_name, input_var):
        label_name = Entry(root)
        self.name.create_window(200, 100, window=quantity_entry)
        label_var = label_name.get()

    def makeLabel(label_name, label_text):
        label_name = Label(root, text = label_text)
        canvas_main.create_window(150, 100, window=q_label)

    def createButton(self, button_name, button_text):
        button_name = Button(text = button_text)# , command = buttonClicked)
        self.name.create_window(200, 180, window=button_name)


canvas_stocks = Window('stonks')


#/-----Stock Page-----\
def createStockCanvas():
    #destroy login page

    canvas_stocks.createWindow()
    canvas_stocks.addImage('stonks_pic', 'stonks.gif')
    canvas_stocks.makeInputBox(quantity_entry, quantity)
    canvas_stocks.makeInputBox(price_entry, price)
    canvas_stocks.makeLabel(q_label, 'quantity')
    canvas_stocks.makeLabel(p_label, 'price')
    canvas_stocks.makeButton(button_cliked, 'big red button')



#/-----Login Page-----\
def createLoginCanvas():



    #display
    canvas_login = Canvas(root, width=400, height=300)
    canvas_login.pack()

    #background image
    login_pic = PhotoImage(file="login.gif")

    #place image
    canvas_login.create_image(50, 10, image=login_pic, anchor=NW)

    #create quantity input box
    user_entry = Entry(root)
    canvas_login.create_window(200, 100, window=user_entry)
    username = user_entry.get()

    #quantity label
    u_label = Label(root, text = 'username')
    canvas_login.create_window(130, 100, window=u_label)

    #create price input box
    pass_entry = Entry(root)
    canvas_login.create_window(200, 140, window=pass_entry)
    password = pass_entry.get()

    #price label
    p_label = Label(root, text = 'password')
    canvas_login.create_window(130, 140, window=p_label)

    #buttonCliked button
    button_clicked = Button(text = 'login')# , command = buttonClicked)
    canvas_login.create_window(200, 180, window=button_clicked)

#def buttonClicked():
    #createStockCanvas

#createLoginCanvas()
createStockCanvas()

root.mainloop()
