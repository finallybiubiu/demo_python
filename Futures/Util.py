#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此添加您的key
ACCESS_KEY=""
SECRET_KEY=""


def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig
