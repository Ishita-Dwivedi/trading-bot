from binance.client import Client
from config import API_KEY, API_SECRET

class BinanceClient:

    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)

        # VERY IMPORTANT for Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **params):
        return self.client.futures_create_order(**params)
    
    def set_leverage(self, symbol, leverage):
        return self.client.futures_change_leverage(symbol=symbol, leverage=leverage)