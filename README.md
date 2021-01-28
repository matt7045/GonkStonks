# GonkStonks
Lets you buy and sell a stock.
Helps you make an account.
Good stuff. 


# On Program Run...
1) Opens default browser
2) Takes you to brokerage "create account" webpage
3) User makes brokerage account. (Can't automate this process because of CAPTCHA)
 ALSO opens the **GUI**

# GUI...
Dead-simple. TKinter?
## Page 1
1) Text box for username
2) Text box for password
3) Text box for LOGIN...Login saves USERNAME and PASSWORD to variables
## Page 2
1) Text box for quantity
2) Text box for price
3) Button for buy...Should call a function *buttonClicked( )*
    

# Inside the buttonClicked() Function...
1) You will import the file *apiWrapper.py*
2) You will call the function *apiWrapper.limit_buy(username, password, quantity, price)
3) The *apiWrapper.limit_buy(username, password, quantity, price)* function will handle all backend API ish, and place the order. I'll do. 

