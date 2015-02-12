#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此输入您的Key
ACCESS_KEY=""
SECRET_KEY=""

BITYES_SERVICE_API="https://api.bityes.com/apiv2"

BUY = "buy"
BUY_MARKET = "buy_market"
SELL = "sell"
SELL_MARKET = "sell_market"
CANCEL_ORDER = "cancel_order"
ACCOUNT_INFO = "get_account_info"
GET_ORDERS = "get_orders"
ORDER_INFO = "order_info"

def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig

