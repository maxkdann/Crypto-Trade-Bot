"""
Trade bot.
Version 4.
"""


import pip._vendor.requests as requests

"""------------------------------------
Exchange
Superclass for the four exchange subclasses.
------------------------------------"""
class Exchange:
    """------------------------------------
    Default constructor for an exchange other than
    the four main ones. Will literally never be used.
    
    Args:
        name (str) - name of exchange
    Returns:
        None.
    ------------------------------------"""
    def __init__(self, name):
        self.name = name
        self.coins = {}
        return
    
    """------------------------------------
    Returns the name of the exchange.
    
    Args:
        None.
    Returns:
        name (str) - name of exchange
    ------------------------------------"""
    def getname(self):
        return self.name

    """------------------------------------
    Updates the name of the exchange.
    
    Args:
        name (str) - new name of exchange
    Returns:
        None.
    ------------------------------------"""
    def setname(self, name):
        self.name = name
        return

    """------------------------------------
    Adds a coin object to an exchange's
    dictionary of coins.
    
    Args:
        coin (coin) - coin object to be added.
    Returns:
        None.
    ------------------------------------"""
    def addCoin(self, coin):
        self.coins[coin.ticker] = coin
        return

    """------------------------------------
    Removes a coin object from an exchange's
    dictionary of coins.
    
    Args:
        coin (coin) - coin object to be removed.
    Returns:
        None.
    ------------------------------------"""
    def removeCoin(self, coin):
        self.coins.pop(coin.ticker)
        return

    """------------------------------------
    Lists all coins we trade in a given exchange.
    
    Args:
        None.
    Returns:
        coins (list of coin) - 
    ------------------------------------"""
    def listCoins(self):
        #TODO:
        return

"""------------------------------------
Child of Exchange, connects to kraken.com
------------------------------------"""
class Kraken(Exchange):
    """------------------------------------
    Creates a Kraken object
    
    Args:
        None.
    Returns:
        None.
    ------------------------------------"""
    def __init__(self):
        self.name = "Kraken"
        self.coins = {}
        return 
    
    """------------------------------------
    Fetches and returns current price of a coin
    
    Args:
        coin (Coin) - coin to loo up
    Returns:
        TODO: what are we returning?
    ------------------------------------"""
    def getprice(self, coin):
        resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=' + coin.ticker)
        #TODO: instead of returning entire response,
        #figure out what we need from ABCV etc...
        return resp.text
    
    def buycoin(self, coin, volume):
        #TODO:
        return 
    
    def sellcoin(self, coin, volume):
        #TODO:
        return
    
    def queryholdings(self, coin):
        #TODO:
        return
    
    def queryAllHoldings(self):
        #TODO:
        return

"""------------------------------------
Child of Exchange, connects to crypto.com
------------------------------------"""
class CryptoDotCom(Exchange):
    """------------------------------------
    Creates a CryptoDotCom object
    
    Args:
        None.
    Returns:
        None.
    ------------------------------------"""
    def __init__(self):
        self.name = "CryptoDotCom"
        self.coins = {}
        return 
    
    def getprice(self, coin):
        #TODO:
        return
    
    def buycoin(self, coin):
        #TODO:
        return 
    
    def sellcoin(self, coin):
        #TODO:
        return
    
    def queryholdings(self, coin):
        #TODO:
        return
    
    def queryAllHoldings(self):
        #TODO:
        return

"""------------------------------------
Child of Exchange, connects to coinbase.com
------------------------------------"""
class Coinbase(Exchange):
    """------------------------------------
    Creates a Coinbase object
    
    Args:
        None.
    Returns:
        None.
    ------------------------------------"""
    def __init__(self):
        self.name = "Coinbase"
        self.coins = {}
        return 
    

    def getprice(self, coin, transaction):
        if "-" not in coin.ticker:
            pair = coin.ticker[:3] + "-" + coin.ticker[3:]
        else:
            pair = coin.ticker
        resp = requests.get("https://api.coinbase.com/v2/prices/" + pair + "/buy")
        
        return resp.text
    
    def buycoin(self, coin):
        #TODO:
        return 
    
    def sellcoin(self, coin):
        #TODO:
        return
    
    def queryholdings(self, coin):
        #TODO:
        return
    
    def queryAllHoldings(self):
        #TODO:
        return

"""------------------------------------
Child of Exchange, connects to kucoin.com
------------------------------------"""
class Kucoin(Exchange):
    """------------------------------------
    Creates a Kucoin object
    
    Args:
        None.
    Returns:
        None.
    ------------------------------------"""
    def __init__(self):
        self.name = "Kucoin"
        self.coins = {}
        return 
    
    def getprice(self, coin):
        #TODO:
        return
    
    def buycoin(self, coin):
        #TODO:
        return 
    
    def sellcoin(self, coin):
        #TODO:
        return
    
    def queryholdings(self, coin):
        #TODO:
        return
    
    def queryAllHoldings(self):
        #TODO:
        return

class Coin:
    def __init__(self, ticker):
        assert len(ticker) == 6 and "-" not in ticker, "ERROR (Coin.init): Ticker must be 6 chars, no dash."
        self.ticker = ticker
        return 

cb = Coinbase()
btc = Coin("BTCUSD")
cb.addCoin(btc)
print(cb.getprice(btc))
k = Kraken()
k.addCoin(btc)
print(k.getprice(btc))