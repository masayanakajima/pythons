#!/usr/local/bin/python
# -*- coding: utf-8 -*-
 
import urllib.request, urllib.parse, urllib.error, re, time, warnings
from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor
 
############################
# Variables
############################
__version__  = '1.0'
 
MIXI_BASE_URL = "http://mixi.jp"
 
############################
# Classes
############################
class LoginFailure(Exception):
    """
    ログインに失敗したときに送出される例外クラス
    """
 
class MIXI:
    """
    MIXI クラス
    """
    ############################
    # Internal Class Methods
    ############################
    def __init__(self):
        self.opener = urllib.request.build_opener(HTTPCookieProcessor(CookieJar()))
        self.mixiid = None
 
    def _post_diary(self, mixiid, title, body, submit="main", postkey=""):
        params = urllib.parse.urlencode({"id": mixiid,
                                         "diary_title": title,
                                         "diary_body": body,
                                         "submit": submit,
                                         "post_key": postkey}).encode('utf-8')
        try:
            f = self.opener.open("%s/add_diary.pl" % MIXI_BASE_URL, params)
            data = f.read().decode("euc-jp")
            f.close()
            return data
        except:
            print('url open error')
            return None
 
    def post_diary(self, title, body):
        html = self._post_diary(self.mixiid, title, body)
        if html == None:
            return False
        postkey = re.search('post_key" value="([^"]*)"', html).group(1)
        html = self._post_diary(self.mixiid, title, body, "confirm", postkey)
        if html == None:
            return False
        return True
 
    ############################
    # Class Methods
    ############################
    def login(self, email, passwd):
        """
        mixi にログインするためのメソッド
        BF_SESSION の中に mixiid が含まれているので Cookie 確認
 
<ul><li> email: ログインするための E-mail アドレス</li><li> password: ログインするためのパスワード</li></ul>
<p>        """
        params = urllib.parse.urlencode({"email": email,
                                         "password":passwd,
                                         "next_url":"home.pl"}).encode('utf-8')
        try :
            response = self.opener.open("%s/login.pl" % MIXI_BASE_URL, params)
            c = response.getheader("Set-Cookie")
            # 先頭から";"まで取り出す
            c = c[:c.find(";")]
            if c.find("session=") == 0:
               l = len("session=")
               self.mixiid = c[l:c.find("_", l)]
            response.close()
        except:
            print('url open error')
            raise LoginFailure
 
# 別ファイルにする場合には必要
#from mixi import MIXI
   
m = MIXI()  
m.login("kasayanus@gmail.com", "kasayanuskasaya")  
m.post_diary('python3から自動登録テスト'.encode('euc-jp'), '成功！'.encode('euc-jp')) 