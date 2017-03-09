# -*- coding: utf-8 -*-

import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    re_utc = re.compile(r'^\w{3}([+|-])(\d+)\:\d{2}$')
    s = re_utc.match(tz_str)
    #根据正则得出UTC时间
    utc =int(s.group(2)) if s.group(1)=='+' else -int(s.group(2))
    #得毫秒数
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    #创建时间的时区
    utc_tz = timezone(timedelta(hours=utc))
    #返回带有时区的时间
    return dt.replace(tzinfo=utc_tz).timestamp()


t1 = to_timestamp('2017-2-23 10:26:30','UTC+7:00')
assert t1 == 1487820390.0,t1
print(t1)
t2 = to_timestamp('2017-2-23 10:26:30', 'UTC-09:00')
#assert t2 == 1433121030.0, t2
print(t2)
print('pass');