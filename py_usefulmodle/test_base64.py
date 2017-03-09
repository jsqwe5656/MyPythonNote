# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(str):
    len1 = len(str)%4
    if len1 == 0:
        return base64.b64decode(str)
    for i in range(4-len1):
        str += b"="
    return base64.b64decode(str)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')