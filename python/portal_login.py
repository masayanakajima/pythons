from selenium import webdriver
from selenium.webdriver.firefox.options import Options

USER="17M38006"
PASS="M0rn1ng-1812"

matrix={'A':{},'B':{},'C':{},'D':{},'E':{},'F':{},'G':{},'H':{},'I':{},'J':{}}
matrix['A']=('B','V','C','P','T','U','U')
matrix['B']=('M','S','R','V','B','N','R')
matrix['C']=('M','E','A','C','K','Z','A')
matrix['D']=('K','L','V','E','L','V','S')
matrix['E']=('W','H','S','S','Z','M','M')
matrix['F']=('H','L','M','S','O','H','N')
matrix['G']=('F','V','Q','V','N','U','U')
matrix['H']=('G','E','B','P','C','K','U')
matrix['I']=('D','X','Z','P','I','J','V')
matrix['J']=('Y','Y','E','N','D','C','I')

def send_matrix_key(i):
	text=browser.find_element_by_css_selector("body > center:nth-child(5) > form > table > tbody > tr > td > table > tbody > tr:nth-child("+i+") > th:nth-child(1)").text
	key_alphabet=text[1]
	key_number=text[3]
	e=browser.find_element_by_css_selector("body > center:nth-child(5) > form > table > tbody > tr > td > table > tbody > tr:nth-child("+i+") > td > div > div > input")
	e.send_keys(matrix[key_alphabet][int(key_number)-1])


browser=webdriver.Chrome()
#browser.implicitly_wait(3)

url_login="https://portal.titech.ac.jp/"
browser.get(url_login)

e=browser.find_element_by_css_selector("input[value='同意（マトリクス/OTP認証）']")
e.click()

e=browser.find_element_by_css_selector("input[name='usr_name']")
e.send_keys(USER)

e=browser.find_element_by_css_selector("input[name='usr_password']")
e.send_keys(PASS)

e=browser.find_element_by_css_selector("input[name='OK']")
e.click()

send_matrix_key("5")
send_matrix_key("6")
send_matrix_key("7")

e=browser.find_element_by_css_selector("input[name='OK']")
e.click()


"""e.clear()
e.send_keys(USER)
e=browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)

frm=browser.find_element_by_css_selector("#loginForm form")
frm.submit()

a=browser.find_element_by_css_selector(".islogin a")
url_mypage=a.get_attribute("href")

browser.get(url_mypage)

links=browser.find_elements_by_css_selector("#favlist li > a")

for a in links:
	href=a.get_attribute("href")
	title=a.text
	print(title,href)"""
