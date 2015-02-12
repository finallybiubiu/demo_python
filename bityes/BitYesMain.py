#coding=utf-8

from Util import *
import BitYesService

if __name__ == "__main__":
    print "提交限价单接口"
    print BitYesService.buy(1,"2355","0.01",None,BUY)
    print "提交市价单接口"
    print BitYesService.buyMarket(2,"30",None,BUY_MARKET)
    print "取消订单接口"
    print BitYesService.cancelOrder(1,68278313,CANCEL_ORDER)
    print "获取账号详情"
    print BitYesService.getAccountInfo(ACCOUNT_INFO)
    print "获取所有正在进行的委托"
    print BitYesService.getOrders(1,GET_ORDERS)
    print "获取订单详情"
    print BitYesService.getOrderInfo(1,68278313,ORDER_INFO)
    print "现价卖出"
    print BitYesService.sell(2,"22.1","0.2",None,SELL)
    print "市价卖出"
    print BitYesService.sellMarket(2,"1.3452",None,SELL_MARKET)



