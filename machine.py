import pyautogui as pa 
import time as t 
from aceitar import captar, jogar, parar, checkarTime
import defs
from random import randint
#Const TOTAL RESOLUTION
#First X and Y value 176 736 // 1207 253
x = (0/1360)*defs.XT
y = (768/768)*defs.YT
#Variables to scriptType
lol = 'League of Legends'
pessoa = input('Você sou eu ? ')
password = 'caracamlk2' if 'S' in pessoa.upper() else input('Digite sua senha : ')
user = 'niltonpiroca2' if 'S' in pessoa.upper() else input('Digite seu user : ')
champ = input('Digite o campeão : ')

def open():
	pa.click(x,y);pa.typewrite(lol);pa.keyDown('enter')
open()

x = defs.upgrade(1207,'l')
y = defs.upgrade(253,'h') 

start=t.time()
#Digita a senha
defs.wait(start,13.5) #Espera o lol abrir
print('Valor de x {}, valor de y {}'.format(x,y))
defs.digitar(password,x,y)

x = defs.upgrade(1192,'l')
y = defs.upgrade(198,'h')
pa.click(x,y, clicks=4);pa.keyDown('backspace')
pa.typewrite(user)

start=t.time()
defs.wait(start,1)

x = defs.upgrade(1209,'l')
y = defs.upgrade(560,'h')
pa.click(x,y)
#Carregar o login
start=t.time()
defs.wait(start,18)
#Play
x = defs.upgrade(161,'l')
y = defs.upgrade(46,'h')
pa.click(x,y)

start=t.time()
defs.wait(start,4)
#COOP
x = defs.upgrade(183,'l')
y = defs.upgrade(102,'h')
pa.click(x,y)

start=t.time()
defs.wait(start,3)
#Aceitar
x = defs.upgrade(573,'l')
y = defs.upgrade(690,'h')
pa.click(x,y)

start=t.time()
defs.wait(start,5)

x = defs.upgrade(573,'l')
y = defs.upgrade(690,'h')
pa.click(x,y)

t.sleep(5)
while True:
	#Confirma o ban
	x = defs.upgrade(685,'l')
	y = defs.upgrade(429,'h')
	pa.click(x,y)

	t.sleep(2)
	#Confirma pra ficar na fila
	checkarTime()
	x = defs.upgrade(573,'l')
	y = defs.upgrade(690,'h')
	pa.click(x,y)

	start = t.time()
	defs.wait(start,2)

	x = defs.upgrade(680,'l')
	y = defs.upgrade(566,'h')
	#Aceita a partida
	while True:
		#Aceita
		captar()
		start = t.time()
		defs.wait(start,1.2)
		#Clica no aceita
		pa.click(x,y)
		if captar()==0:
			break
	#ver se já meteu o louco no coop
	t.sleep(14)
	captar()

	start=t.time()
	defs.wait(start,2)

	#Digita o nome do campeão
	x = defs.upgrade(871,'l')
	y = defs.upgrade(106,'h')
	pa.doubleClick(x,y);pa.typewrite(champ)

	start=t.time()
	defs.wait(start,2.5)
	#Clica no quadrado
	x = defs.upgrade(421,'l')
	y = defs.upgrade(169,'h')
	pa.click(x,y)

	start=t.time()
	defs.wait(start,2.5)
	#Confirma
	x = defs.upgrade(672,'l')
	y = defs.upgrade(607,'h')
	pa.doubleClick(x,y)

	start=t.time()
	defs.wait(start,30)

	jogar()
	#Joga
	while True:	
		x = defs.upgrade(randint(10,1000),'l')
		y = defs.upgrade(randint(10,600),'h')
		pa.click(x,y, button='right')
		start=t.time()
		if parar()==0:
			break
		defs.wait(start,1.5)	

	#Depois que acaba a partida
	t.sleep(50)
	x = defs.upgrade(590,'l')
	y = defs.upgrade(692,'h')
	pa.click(x,y)
