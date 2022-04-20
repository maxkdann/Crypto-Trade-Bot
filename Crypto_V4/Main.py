"""
Trade bot.
Version 4.
"""
import pip._vendor.requests as requests
import time
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
        self.maker_fee = -1
        self.taker_fee = -1
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
        print("Error (" + self.name + ".addCoin): No method to add coin to this exchange yet.")
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
        self.coins.pop(coin)
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
    
    def getFees(self):
        """
        ------------------------------------
        Returns the maker and taker fees of a given exchange
        Args:
            None.
        Returns:
            maker fee and taker fee
        ------------------------------------
        """
        return self.maker_fee, self.taker_fee
    
    def calculateFees(self, volume):
        """
        ------------------------------------
        calculate the fees for a given trade
        Args:
            volume (float) - amount of a certain coin to be traded
        Returns:
            maker_fee (float) - fee for being the maker of this trade
            taker_fee (float) - fee for being the taker of this trade
        ------------------------------------
        """
        maker_fee, taker_fee = self.getFees()
        return maker_fee * volume, taker_fee * volume

"""------------------------------------
Child of Exchange, connects to gemini.com
------------------------------------"""


class Gemini(Exchange):

    def __init__(self):
        """
        ------------------------------------
        Creates a Gemini object
        
        Args:
            None.
        Returns:
            None.
        ------------------------------------
        """
        self.name = "Gemini"
        self.coins = {}
        self.maker_fee = 0.21
        self.taker_fee = 0.41
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
        try:
            resp = requests.get('https://api.gemini.com/v1/pubticker/' + coin)
        except:
            print("Error occured fetching Gemini prices for "+ coin)
        resp = resp.text.split("\"")
        if resp[7]=="Bad Request":
            print("The pair "+ coin+" does not exist on Gemini")
            buy = -1
            sell = -1
        else:
            buy = float(resp[3])
            sell = float(resp[7])
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
    
    def addCoin(self, coin):
        assert isinstance(coin, str), "Error (" + self.name + ".addCoin): coin must be string"
        self.coins[coin] = (-1, -1)
        print("Added " + coin + " to " + self.name)
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
        self.maker_fee = 0.2
        self.taker_fee = 0.2
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
        try:
            resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=' + coin)
        except:
            print("Error occured fetching Kraken prices for "+ coin)
        resp = resp.text.split("\"")
        buy = float(resp[9])
        sell = float(resp[17])
        return buy, sell
    
    
   
    def getFees(self):
        return self.maker_fee, self.taker_fee
    
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
    
    def addCoin(self, coin):
        assert isinstance(coin, str), "Error (" + self.name + ".addCoin): coin must be string"
        self.coins[coin] = (-1, -1)
        print("Added " + coin + " to " + self.name)
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
        self.maker_fee = 0.4
        self.taker_fee = 0.4
        return 
    
    def getprice(self, coin):
        try:
            resp = requests.get("https://api.crypto.com/v2/public/get-ticker?instrument_name=" + pair)
        except:
            print("Error occured fetching Crypto.com prices for "+ pair)
        resp = resp.text.split("\"")
        buy = float(resp[20][1:-1])
        sell = float(resp[24][1:-1])
        return buy, sell
    
    def getFees(self):
        return self.maker_fee, self.taker_fee
    
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
    
    def addCoin(self, coin):
        assert isinstance(coin, str), "Error (" + self.name + ".addCoin): coin must be string"
        
        if coin[-4:].lower() == "usdt":
            newcoin = coin[:-4] + "_" + coin[-4:]
        elif coin[-3:].lower() == "usd":
            newcoin = coin[:-3] + "_" + coin[-3:]
        else:
            print("Error: coin name: " + coin)
        
        self.coins[newcoin] = (-1, -1)
        print("Added " + newcoin + " to " + self.name)
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
        self.maker_fee = 0.4
        self.taker_fee = 0.6
        return 

    def getprice(self, coin):
        # query price
        try:
            buy = requests.get("https://api.coinbase.com/v2/prices/" + coin + "/buy")
            sell = requests.get("https://api.coinbase.com/v2/prices/" + coin + "/sell")
        except:
            print("Error occured fetching Coinbase prices for "+ coin)
        # standardize output
        buy = buy.text.split("\"")
        sell = sell.text.split("\"")
        if buy[-2] or sell[-2]=="Invalid Currency":
            print("The pair "+ coin +" does not exist on Coinbase")
            buy = -1
            sell = -1
        else:
            buy = float(buy[-2])
            sell = float(sell[-2])
        return buy, sell
    
    def buycoin(self, coin):
        # TODO:
        return 
    
    def getFees(self):
        return self.maker_fee, self.taker_fee
    
    def sellcoin(self, coin):
        # TODO:
        return
    
    def queryholdings(self, coin):
        # TODO:
        return
    
    def queryAllHoldings(self):
        # TODO:
        return

    def addCoin(self, coin):
        assert isinstance(coin, str), "Error (" + self.name + ".addCoin): coin must be string"
        
        if coin[-4:].lower() == "usdt":
            newcoin = coin[:-4] + "-" + coin[-4:]
        elif coin[-3:].lower() == "usd":
            newcoin = coin[:-3] + "-" + coin[-3:]
        else:
            print("Error: coin name: " + coin)
        
        self.coins[newcoin] = (-1, -1)
        print("Added " + newcoin + " to " + self.name)
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
        self.maker_fee = 0.1
        self.taker_fee = 0.1
        return 
    
    def getprice(self, coin):
        try:
            resp = requests.get("https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=" + coin)  
        except:
            print("Error occured fetching Kucoin prices for "+ coin)
        resp = resp.text.split("\"")
        buy = float(resp[15])
        return buy, buy
    #TODO: wait why does kucoin not have a buy and a sell?
    
    def getAllPrices(self):
        """
        ----------------------------------------------------------
        Kucoin allows you to get ticker information for all the coins listed on their
        site at once by calling allTickers
        ----------------------------------------------------------
        """
        resp = requests.get("https://api.kucoin.com/api/v1/market/allTickers")
        resp = resp.text
        resp = resp[66:]
        resp = resp.split("\"")
        parsedData = self.parseData(resp)
        return parsedData
    
    def parseData(self, raw_data):
        """
        parses the data returned by getAllPrices into a nice list of coins and buy/sell prices
        """
        parsedData = []
        i = 0
        temp = []
        while i < len(raw_data):
            if raw_data[i] == "symbolName":
                temp.append(raw_data[i + 2])
                temp.append(raw_data[i + 6])
                temp.append(raw_data[i + 10])
                parsedData.append(temp)
                temp = []
            i += 1
            
        return parsedData
    
    def getFees(self):
        return self.maker_fee, self.taker_fee
    
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

    def addCoin(self, coin):
        assert isinstance(coin, str), "Error (" + self.name + ".addCoin): coin must be string"
        
        if coin[-4:].lower() == "usdt":
            newcoin = coin[:-4] + "-" + coin[-4:]
        elif coin[-3:].lower() == "usd":
            newcoin = coin[:-3] + "-" + coin[-3:]
        else:
            print("Error: coin name: " + coin)
        
        self.coins[newcoin] = (-1, -1)
        print("Added " + newcoin + " to " + self.name)
        return


def getGreatestSpread(coin=None):
    """
    ------------------------------------
    Queries all 5 exchanges to find the largest price differential
    Args:
        coin (string) - ticker to check spread
    Returns:
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
    gemini = Gemini()
    
    # add coin to exchange objects
    coinbase.addCoin(coin)
    kraken.addCoin(coin)       
    cryptodotcom.addCoin(coin)       
    kucoin.addCoin(coin)
    gemini.addCoin(coin)
    
    
    # query prices
    t1 = time.time()
    cb_buy_price, cb_sell_price = coinbase.getprice(coin)
    kr_buy_price, kr_sell_price = kraken.getprice(coin)
    cr_buy_price, cr_sell_price = cryptodotcom.getprice(coin)
    ku_buy_price, ku_sell_price = kucoin.getprice(coin)  
    g_buy_price,g_sell_price = gemini.getprice(coin)
    t2 = time.time()
    
    # display prices
    print("Coinbase - buy: {} sell: {}".format(cb_buy_price, cb_sell_price))
    print("Kraken - buy: {} sell: {}".format(kr_buy_price, kr_sell_price))
    print("Crypto.com - buy: {} sell: {}".format(cr_buy_price, cr_sell_price))
    print("Kucoin - buy: {} sell: {}".format(ku_buy_price, ku_sell_price))
    print("Gemini - buy: {} sell: {}".format(g_buy_price, g_sell_price))
    print("lag: " + str(t2 - t1))
    
    # find largest difference
    buy_prices = [kr_buy_price, cr_buy_price, ku_buy_price]
    sell_prices = [kr_sell_price, cr_sell_price, ku_sell_price]
    min_buy = min(buy_prices)
    max_sell = max(sell_prices)
    exchanges = [coinbase, kraken, cryptodotcom, kucoin,gemini]
    low_exchange_index = buy_prices.index(min_buy)
    high_exchange_index = sell_prices.index(max_sell)
    
    low_exchange = exchanges[low_exchange_index]
    high_exchange = exchanges[high_exchange_index]
    
    # output greatest spread
    print()
    print("Buy on {} for {}".format(low_exchange.name, min_buy))
    print("Sell on {} for {}".format(high_exchange.name, max_sell))
    print("Profit: {:.2f}".format(max_sell - min_buy))
    
    return min_buy, max_sell, low_exchange, high_exchange


def main():
    ticker = "btcusdt"
    assert (ticker[len(ticker) - 3:].upper() == "USD") or (ticker[len(ticker) - 4:].upper() == "USDT"), "Coin must trade with USDT or USD"
    if ticker[len(ticker) - 4:].upper() == "USDT":
        if "-" not in ticker:
            ticker = (ticker[:(len(ticker) - 4)] + "-" + ticker[len(ticker) - 4:]).upper()
        else:
            ticker = ticker.upper()
    else:
        if "-" not in ticker:
            ticker = (ticker[:(len(ticker) - 3)] + "-" + ticker[len(ticker) - 3:]).upper()
        else:
            ticker = ticker.upper()
    getGreatestSpread(ticker)
    
    # get all prices for Kucoin
    """
    k = Kucoin()
    r = k.getAllPrices()
    f = open("kucoinPrices.txt","w")
    for line in r:
        f.write(" ".join(line)+"\n")
    f.close()
    """

    

def initialize():
    """
    -create exchange objects
    -read in csv
    -populate exchange objects
    -call first-time price update (?) or don't idc
    
    """

    #create exchange objects
    gemini = Gemini()
    coinbase = Coinbase()
    kraken = Kraken()
    cryptodotcom = CryptoDotCom()
    kucoin = Kucoin()
    
    fv = open("coins1.csv", 'r', encoding="UTF-8")
    fv.readline()
    line = fv.readline()
    while line != "":
        parts = line.strip().split(",")
        ticker = parts[0] #max don't ever say I can't make an intermediary variable.
        if ticker == "XYOUSDT":
            print("STOP!")
        if parts[1] == "1":
            gemini.addCoin(ticker)
        if parts[2] == "1":
            coinbase.addCoin(ticker)
        if parts[3] == "1":
            kraken.addCoin(ticker)
        if parts[4] == "1":
            cryptodotcom.addCoin(ticker)
        if parts[5] == "1":
            kucoin.addCoin(ticker)
        line = fv.readline()
    fv.close()

    print("\n\nAll coins added.\n\n")
    
    for key in gemini.coins:
        print(key + " -> " + str(gemini.coins[key]))
    

    
    

initialize()