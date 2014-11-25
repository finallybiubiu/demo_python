#coding=utf-8

import urllib
import hashlib
import hmac
import base64


ACCESS_KEY="28d3e07f-32c6c6d9-e83328c9-21f6fb65"
SECRET_KEY="97aa8d28-a7b2c39e-1558b11d-8a5254e0"


def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig