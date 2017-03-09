# -*- coding: utf-8 -*-

import hashlib

db = {}
def register(username,password):
    db[username] = get_md5(password+username+'the-Salt')
    print('register sucess %s,%s' %(username,password))

def login(user,password):
    try:
        db_pwd = db[user]
        if db_pwd ==get_md5(password + user + 'the-Salt'):
            print('login sucess')
        else:
            print('wrong password')
    except KeyError:
        print ('don\'t hava that user')

def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    result = md5.hexdigest()
    print(result)
    return result

register('zbf','123456')
login('zbf','1234567')
login('zbf','123456')