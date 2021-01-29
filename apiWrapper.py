import alpaca_trade_api as tradeapi

def limitBuy(LIVE_API_KEY_ID, LIVE_SECRET_KEY, price, quantity):  
    api = tradeapi.REST(LIVE_API_KEY_ID, LIVE_SECRET_KEY, api_version='v2')
    api.submit_order("GME", quantity, 'buy', 'limit', 'gtc', limit_price = price)
