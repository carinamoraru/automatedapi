import my_kucoin

api_key = "62c7f299686bb40001c17f11"
secret_key = "87ecfc58-8a0b-4693-a007-5ff3d25fd10a"
passphrase = "greentrees1111"

myKucoin = my_kucoin.Mykucoin(api_key, secret_key, passphrase)


print('coin: {0}'.format(myKucoin.printit()[0]))
print('buy: {0}'.format(myKucoin.printit()[1]))
