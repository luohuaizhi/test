# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    sl = len(s)
    print "s len: %d" % sl
    if sl % 4 == 0:
        return s
    b = 4-sl % 4
    print "need replenish: %d" % b
    bw = "="*b
    print "replenish: %s " % bw
    s = s+bw
    return s
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')