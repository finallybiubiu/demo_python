#coding=utf-8

from BitvcService import *

BITVC_ACCOUNT_INFO = "https://api.bitvc.com/api/accountInfo/get"
BITVC_GET_ORDERS = "https://api.bitvc.com/api/order/list"
BITVC_ORDER_INFO = "https://api.bitvc.com/api/order/"
BITVC_BUY_MARKET = "https://api.bitvc.com/api/order/buy_market"
BITVC_BUY = "https://api.bitvc.com/api/order/buy"
BITVC_SELL_MARKET = "https://api.bitvc.com/api/order/sell_market"
BITVC_SELL = "https://api.bitvc.com/api/order/sell"
BITVC_CANCEL_ORDER = "https://api.bitvc.com/api/order/cancel/"

if __name__ == "__main__":
    print "获取账号详情"
    print getAccountInfo(BITVC_ACCOUNT_INFO)
    print "获取所有正在进行的委托"
    print getOrders(1,BITVC_GET_ORDERS)
    print "获取委托单详情"
    print getOrderInfo(1,"1749809",BITVC_ORDER_INFO)
    print "市价买入接口"
    print buyMarket(1,"20",None,BITVC_BUY_MARKET)
    print "限价买入接口"
    print  buy(1,"2370","0.01",None,BITVC_BUY)
    print "市价卖出"
    print sellMarket(1,"0.01",None,BITVC_SELL_MARKET)
    print "限价卖出"
    print sell(1,"2380","0.009",None,BITVC_SELL)
    print "取消订单接口"
    print cancelOrder(1,"1749809",BITVC_CANCEL_ORDER)
