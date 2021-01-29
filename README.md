# GonkStonks
Lets you buy and sell a stock.
Helps you make an account.
Good stuff. 

# On Program Run...
1) Opens default browser
2) Takes you to Alpaca brokerage "create account" webpage
3) User makes brokerage account. (Can't automate this process because of CAPTCHA)
 ALSO opens the **GUI**

# GUI...
Dead-simple. TKinter!
## Page 1
0) Include screenshot *Key Generation Instructions.png*
1) Text box for entering Secret key
2) Text Box for entering API key ID
3) Login button, that opens **Page 2**
## Page 2
1) Text box for quantity
2) Text box for price
3) Button for buy...Should call a function *buttonClicked( )*
# Inside the buttonClicked() Function...
1) You will import the file *apiWrapper.py*
2) You will call the function *apiWrapper.limitBuy(username, password, quantity, price)*
3) The *apiWrapper.limitBuy(username, password, quantity, price)* function will handle all backend API ish, and place the order. I'll do. 

#Permissions needed
1) Will install python 3.9 (If not already installed)
2) Will pip-install alpaca_trade_api
