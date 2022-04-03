"""
Trade bot.
Version 4.
"""
import pip._vendor.requests as requests
import time
import threading
from copy import deepcopy
#from scipy.io.matlab.miobase import arr_dtype_number
"""------------------------------------
Exchange
Superclass for the four exchange subclasses.
------------------------------------"""


class Exchange:
    
    def __init__(self, name):
        """
        ------------------------------------
        Default constructor for an exchange other than
        the four main ones. Will literally never be used.
        
        Args:
            name (str) - name of exchange
        Returns:
            None.
        ------------------------------------
        """
        self.name = name
        self.coins = {}
        return

    def getname(self):
        """
        ------------------------------------
        Returns the name of the exchange.
        
        Args:
            None.
        Returns:
            name (str) - name of exchange
        ------------------------------------
        """
        return self.name

    def setname(self, name):
        """
        ------------------------------------
        Updates the name of the exchange.
        
        Args:
            name (str) - new name of exchange
        Returns:
            None.
        ------------------------------------
        """
        self.name = name
        return
    
    def addCoin(self, coin):
        """
        ------------------------------------
        Adds a coin object to an exchange's
        dictionary of coins.
        
        Args:
            coin (coin) - coin object to be added.
        Returns:
            None.
        ------------------------------------
        """
        self.coins[coin.ticker] = coin
        return

    def removeCoin(self, coin):
        """
        ------------------------------------
        Removes a coin object from an exchange's
        dictionary of coins.
        
        Args:
            coin (coin) - coin object to be removed.
        Returns:
            None.
        ------------------------------------"""
        self.coins.pop(coin.ticker)
        return

    def listCoins(self):
        """
        ------------------------------------
        Lists all coins we trade in a given exchange.
        
        Args:
            None.
        Returns:
            coins (list of coin) - 
        ------------------------------------
        """
        # TODO:
        return

        

"""------------------------------------
Child of Exchange, connects to kraken.com
------------------------------------"""


class Kraken(Exchange):

    def __init__(self):
        """
        ------------------------------------
        Creates a Kraken object
        
        Args:
            None.
        Returns:
            None.
        ------------------------------------
        """
        self.name = "Kraken"
        self.coins = {}
        return 

    def getprice(self, coin):
        """
        ------------------------------------
        Fetches and returns current price of a coin
        
        Args:
            coin (Coin) - coin to look up
        Returns:
            TODO: what are we returning?
        ------------------------------------
        """
        resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=' + coin.ticker)
        resp = resp.text.split("\"")
        buy = float(resp[9])
        sell = float(resp[17])
        return buy, sell
    
    def buycoin(self, coin, volume):
        # TODO:
        return 
    
    def sellcoin(self, coin, volume):
        # TODO:
        return
    
    def queryholdings(self, coin):
        # TODO:
        return
    
    def queryAllHoldings(self):
        # TODO:
        return

"""------------------------------------
Child of Exchange, connects to crypto.com
------------------------------------"""


class CryptoDotCom(Exchange):

    def __init__(self):
        """
        ------------------------------------
        Creates a CryptoDotCom object
        
        Args:
            None.
        Returns:
            None.
        ------------------------------------
        """
        self.name = "CryptoDotCom"
        self.coins = {}
        return 
    
    def getprice(self, coin):
        if "_" not in coin.ticker:
            pair = coin.ticker[:3] + "_" + coin.ticker[3:]
        else:
            pair = coin.ticker
        resp = requests.get("https://api.crypto.com/v2/public/get-ticker?instrument_name=" + pair)
        resp = resp.text.split("\"")
        buy = float(resp[20][1:-1])
        sell = float(resp[24][1:-1])
        return buy,sell
    
    def buycoin(self, coin):
        # TODO:
        return 
    
    def sellcoin(self, coin):
        # TODO:
        return
    
    def queryholdings(self, coin):
        # TODO:
        return
    
    def queryAllHoldings(self):
        # TODO:
        return

"""------------------------------------
Child of Exchange, connects to coinbase.com
------------------------------------"""


class Coinbase(Exchange):

    def __init__(self):
        """
        ------------------------------------
        Creates a Coinbase object
        
        Args:
            None.
        Returns:
            None.
        ------------------------------------
        """
        self.name = "Coinbase"
        self.coins = {}
        return 

    def getprice(self, coin):
        # fix ticker symbol
        if "-" not in coin.ticker:
            pair = coin.ticker[:3] + "-" + coin.ticker[3:]
        else:
            pair = coin.ticker
        # query price
        buy = requests.get("https://api.coinbase.com/v2/prices/" + pair + "/buy")
        sell = requests.get("https://api.coinbase.com/v2/prices/" + pair + "/sell")
        # standardize output
        buy = buy.text.split("\"")
        sell = sell.text.split("\"")
        buy = float(buy[-2])
        sell = float(sell[-2])
        return buy, sell
    
    def getpricetest(self, coin):
        # fix ticker symbol
        if "-" not in coin:
            pair = coin[:3] + "-" + coin[3:]
        else:
            pair = coin.ticker
        # query price
        buy = requests.get("https://api.coinbase.com/v2/prices/" + pair + "/buy")
        sell = requests.get("https://api.coinbase.com/v2/prices/" + pair + "/sell")
        # standardize output
        buy = buy.text.split("\"")
        sell = sell.text.split("\"")
        buy = float(buy[-2])
        sell = float(sell[-2])
        return buy, sell
    
    def buycoin(self, coin):
        # TODO:
        return 
    
    def sellcoin(self, coin):
        # TODO:
        return
    
    def queryholdings(self, coin):
        # TODO:
        return
    
    def queryAllHoldings(self):
        # TODO:
        return

"""------------------------------------
Child of Exchange, connects to kucoin.com
------------------------------------"""


class Kucoin(Exchange):
   
    def __init__(self):
        """
         ------------------------------------
        Creates a Kucoin object
        
        Args:
            None.
        Returns:
            None.
        ------------------------------------
        """
        self.name = "Kucoin"
        self.coins = {}
        return 
    
    def getprice(self, coin):
        if "-" not in coin.ticker:
            pair = coin.ticker[:3] + "-" + coin.ticker[3:]
        else:
            pair = coin.ticker
        resp = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=" + pair)  
        resp = resp.text.split("\"")
        buy = float(resp[15])
        return buy, buy
    
    def buycoin(self, coin):
        # TODO:
        return 
    
    def sellcoin(self, coin):
        # TODO:
        return
    
    def queryholdings(self, coin):
        # TODO:
        return
    
    def queryAllHoldings(self):
        # TODO:
        return


class Coin:

    def __init__(self, ticker):
        # assert len(ticker) == 6 and "-" not in ticker, "ERROR (Coin.init): Ticker must be 6 chars, no dash."
        # coin pair can be more than 6 chars
        self.ticker = ticker
        return 
        
'''
cb = Coinbase()
btc_usd = Coin("BTCUSD")
btc_usdt = Coin("BTCUSDT")
cb.addCoin(btc_usd)

k = Kraken()
k.addCoin(btc_usd)
c = CryptoDotCom()
c.addCoin(btc_usdt)
ku = Kucoin()
ku.addCoin(btc_usdt)

t1 = time.time()
print("coinbase: " + cb.getprice(btc_usd))
print("kraken:   " + k.getprice(btc_usd))
print("cdc:      " + c.getprice(btc_usdt))
print("kucoin:   " + ku.getprice(btc_usdt))
t2 = time.time()
print("lag: " + str(t2 - t1))
'''
def getGreatestSpread(coin=None):
    """
    ------------------------------------
    Queries all 4 exchanges to find the largest price differential
    Args:
        coin (Coin object) - specific coin to query, if no coin specified query for all coins
    Returns:
        coin (Coin object) - coin with the largest spread
        min_buy (float) - minimum purchase price
        max_sell (float) - maximum sell price
        low_exchange (Exchange object) - exchange with the low price
        high_exchange(Exchange object) - exchange with the high price
    ------------------------------------
    """
    # create exchange objects
    coinbase = Coinbase()
    kraken = Kraken()
    cryptodotcom = CryptoDotCom()
    kucoin = Kucoin()
    # add coin to exchange object
    btc_usd = Coin("BTCUSD")
    btc_usdt = Coin("BTCUSDT")
    coinbase.addCoin(btc_usd)
    kraken.addCoin(btc_usd)       
    cryptodotcom.addCoin(btc_usdt)       
    kucoin.addCoin(btc_usdt)
    
    # query prices
    # t1 = time.time()
    # cb_buy_price, cb_sell_price = coinbase.getprice(btc_usd)
    # kr_buy_price, kr_sell_price = kraken.getprice(btc_usd)
    # cr_buy_price,cr_sell_price = cryptodotcom.getprice(btc_usdt)
    # ku_buy_price, ku_sell_price = kucoin.getprice(btc_usdt)  
    # t2 = time.time()
    
    #query prices with multithreading
    t1 = time.time()
    tuple1 = ("btc_usd",)
    cb_buy_price, cb_sell_price = _thread.start_new_thread(coinbase.getprice, tuple1)
    kr_buy_price, kr_sell_price = _thread.start_new_thread(kraken.getprice, (btc_usd))
    cr_buy_price,cr_sell_price = _thread.start_new_thread(cryptodotcom.getprice, (btc_usd))
    ku_buy_price, ku_sell_price = _thread.start_new_thread(kucoin.getprice, (btc_usd))
    t2 = time.time()
    
    #query prices with multithreading again.
    # t1 = time.time()
    # tuple1 = ("btc_usd",)
    # cb_buy_price, cb_sell_price = _thread.start_new_thread(coinbase.getprice, tuple1)
    # kr_buy_price, kr_sell_price = _thread.start_new_thread(kraken.getprice, (btc_usd))
    # cr_buy_price,cr_sell_price = _thread.start_new_thread(cryptodotcom.getprice, (btc_usd))
    # ku_buy_price, ku_sell_price = _thread.start_new_thread(kucoin.getprice, (btc_usd))
    # t2 = time.time()
    
    
    #print prices, lag will be fixes once multithreading is implemented
    print("Coinbase - buy: {} sell: {}".format(cb_buy_price, cb_sell_price))
    print("Kraken - buy: {} sell: {}".format(kr_buy_price, kr_sell_price))
    print("Crypto.com - buy: {} sell: {}".format(cr_buy_price, cr_sell_price))
    print("Kucoin - buy: {} sell: {}".format(ku_buy_price, ku_sell_price))
    print("lag: " + str(t2 - t1))
    
    #find largest difference
    buy_prices = [cb_buy_price,kr_buy_price,cr_buy_price,ku_buy_price]
    sell_prices = [cb_sell_price,kr_sell_price,cr_sell_price,ku_sell_price]
    min_buy = min(buy_prices)
    max_sell = max(sell_prices)
    exchanges = [coinbase,kraken,cryptodotcom,kucoin]
    low_exchange_index = buy_prices.index(min_buy)
    high_exchange_index = sell_prices.index(max_sell)
    
    low_exchange = exchanges[low_exchange_index]
    high_exchange = exchanges[high_exchange_index]
    print()
    print("Buy on {} for {}".format(low_exchange.name,min_buy))
    print("Sell on {} for {}".format(high_exchange.name,max_sell))
    print("Profit: {:.2f}".format(max_sell-min_buy))

getGreatestSpread()