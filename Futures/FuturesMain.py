#coding=utf-8

from FuturesService import  *


FUTURES_BALANCE_INFO = "https://api.bitvc.com/futures/balance"
FUTURES_HOLD_ORDER_LIST = "https://api.bitvc.com/futures/holdOrder/list"
FUTURES_HOLD_ORDER_SUM = "https://api.bitvc.com/futures/holdOrder"
FUTURES_ORDERS_LIST="https://api.bitvc.com/futures/order/list"
FUTURES_ORDER_INFO = "https://api.bitvc.com/futures/order"
FUTURES_ORDER_SAVE="https://api.bitvc.com/futures/order/save"
FUTURES_CANCEL_ORDER = "https://api.bitvc.com/futures/order/cancel"


if __name__ == "__main__":
    print "获取期货资产信息"
    print getBalanceInfo(1,FUTURES_BALANCE_INFO)
    print "获取用户持仓记录，week 周 quarter 季"
    print getHoldOrderList(1,"week",FUTURES_HOLD_ORDER_LIST)
    print "获取用户持仓记录，汇总"
    print getHoldOrderSum(1,"week",FUTURES_HOLD_ORDER_SUM)
    print "获取所有正在进行的委托"
    print getOrderList(1,"week",FUTURES_ORDERS_LIST)
    print "委托单详情"
    print getOrderInfo(3757870,1,"week",FUTURES_ORDER_INFO)
    print "下委托单"
    price=2470
    money=100
    #1开2平，1买2卖
    print saveOrder(1,"week",1,1,price,money,10,FUTURES_ORDER_SAVE)
    print "取消订单接口"
    print cancelOrder(1,"week",3757870,FUTURES_CANCEL_ORDER)

