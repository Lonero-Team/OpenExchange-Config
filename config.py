instruments = ["lnr_btc"]
currencies = {
    "lnr": {
        "daemon": "142.93.171.115:34415@127.0.0.1:34414",
        "multiplier": 100000000,
        "name": "Lonero"},
    "btc": {
        "daemon": "http://bitcoinrpc:94CpFcoCgO@127.0.0.1:8332",
        "multiplier": 100000000,
        "name": "Bitcoin"}}
dbfile = 'test.db'
txlogfile = 'depositor.log'
class config:
    @staticmethod
    def is_valid_instrument(instrument):
        return instrument in instruments
    @staticmethod
    def get_instruments():
        return instruments
    @staticmethod
    def is_valid_currency(currency):
        return currency in currencies
    @staticmethod
    def getRPC(currency):
        return currencies[currency]["daemon"]
    @staticmethod
    def get_currencies():
        return currencies
    @staticmethod
    def get_multiplier(currency):
        return currencies[currency]["multiplier"]
    @staticmethod
    def get_database_file():
        return dbfile
    @staticmethod
    def get_tx_log_file():
return txlogfile
