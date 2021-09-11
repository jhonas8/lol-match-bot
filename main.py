from aceitar import captar,escolher
import defs
import pyautogui as pa
import time as t
champ = input('Ban : ')
champ2 = input('Champ : ')
escolha = input('Deseja banir e selecionar algum champ ? ')

x = defs.upgrade(680,'l')
y = defs.upgrade(566,'h')
while True:
	#Aceita
	captar()
	start = t.time()
	defs.wait(start,1.2)
	pa.click(x,y)
	if captar()==0:
		break
if 'S'in escolha.upper():
	start=t.time()
	defs.wait(start,1)	

	x = defs.upgrade(227,'l')
	y = defs.upgrade(691,'h')
	pa.click(x,y);pa.typewrite('N bane {}'.format(champ2))
	pa.keyDown('enter')



	start=t.time()
	defs.wait(start,16)

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

	escolher()
	#banir
	start=t.time()
	defs.wait(start,2)

	#Digita o nome do campeão
	x = defs.upgrade(871,'l')
	y = defs.upgrade(106,'h')
	pa.doubleClick(x,y);pa.typewrite(champ2)

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
