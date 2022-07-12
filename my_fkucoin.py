import json
import os
import threading
import fclient

class Myfkucoin():
    def __init__(self, key, secret, passphrase):
        self.client = fclient.Fclient(key, secret, passphrase)
        self.apiKey = key
        self.secret = secret
        self.passphrase = passphrase

    def printit(self):
        # threading.Timer(3000.0, printit).start()
        pull = self.client.get_ticker()
        coinType = pull['ticker'][0]["buy"]
        buyPrice = pull['ticker'][0]["sell"]

        return format(coinType), format(buyPrice)
