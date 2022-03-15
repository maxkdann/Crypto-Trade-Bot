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
        #TODO:
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
        #assert len(ticker) == 6 and "-" not in ticker, "ERROR (Coin.init): Ticker must be 6 chars, no dash."
        #coin pair can be more than 6 chars
        self.ticker = ticker
        return 

cb = Coinbase()
btc_usd = Coin("BTCUSD")
btc_usdt = Coin("BTCUSDT")
cb.addCoin(btc_usd)

k = Kraken()
k.addCoin(btc_usd)
c = CryptoDotCom()
c.addCoin(btc_usdt)
print(cb.getprice(btc_usd))
print(k.getprice(btc_usd))
print(c.getprice(btc_usdt))