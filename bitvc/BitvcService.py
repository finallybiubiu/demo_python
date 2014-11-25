#coding=utf-8

import time

import requests

from Util import *


'''
获取账号详情
'''
def getAccountInfo(url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None

'''
获取所有正在进行的委托
@param coinType
'''
def getOrders(coinType,url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None



'''
获取订单详情
@param coinType
@param id
'''
def getOrderInfo(coinType,id,url):
    url=url+str(id)
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,"id":id}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None


'''
提交市价单接口
@param coinType
@param amount
@param tradePassword
'''
def buyMarket(coinType,amount,tradePassword,url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,"amount":amount}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']
    if tradePassword:
        params['trade_password']=tradePassword

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None



'''
下单接口
@param coinType
@param price
@param amount
@param tradePassword
'''
def buy(coinType,price,amount,tradePassword,url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,
              "amount":amount,"price":price}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    if tradePassword:
        params['trade_password']=tradePassword
    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None


'''
市价卖出
@param coinType
@param amount
@param tradePassword
'''
def sellMarket(coinType,amount,tradePassword,url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,"amount":amount}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']
    if tradePassword:
        params['trade_password']=tradePassword

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None



'''
限价卖出
@param coinType
@param price
@param amount
@param tradePassword
'''
def sell(coinType,price,amount,tradePassword,url):
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,
              "amount":amount,"price":price}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    if tradePassword:
        params['trade_password']=tradePassword
    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None



'''
撤销订单
@param coinType
@param id
'''
def cancelOrder(coinType,id,url):
    url=url+str(id)
    timestamp = long(time.time())
    params = {"access_key": ACCESS_KEY,"secret_key": SECRET_KEY, "created": timestamp,"coin_type":coinType,"id":id}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    r = requests.post(url, params=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        return None



