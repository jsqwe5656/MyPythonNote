# -*- coding: utf-8 -*-

import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
#返回密码的md5码
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
#登录方法
def login(user,password):
    try:
        db_pwd = db[user]
        if db_pwd ==calc_md5(password):
            print('login sucess')
        else:
            print('wrong password')
    except KeyError:
        print ('don\'t hava that user')

login('zbf','123456')
login('michael','123456')