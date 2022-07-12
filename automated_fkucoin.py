import my_kucoin

api_key = ""
secret_key = ""
passphrase = "greentrees1111"

myKucoin = my_kucoin.Mykucoin(api_key, secret_key, passphrase)


print('coin: {0}'.format(myKucoin.printit()[0]))
print('buy: {0}'.format(myKucoin.printit()[1]))
