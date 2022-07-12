from pybit import inverse_perpetual


class Mybybit():
    def __init__(self, key, secret):
        self.endpoint = "https://api.bybit.com"
        self.apiKey = key
        self.secret = secret

    def get_json(self, symbol, interval, from_time):
        session_auth = inverse_perpetual.HTTP(
            endpoint=self.endpoint,
            api_key=self.apiKey,
            api_secret=self.secret
        )

        json_data = session_auth.query_kline(
            symbol=symbol,
            interval=interval,
            from_time=from_time
        )
        return json_data
