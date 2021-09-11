import pyautogui as pa 
import time as t 
#VARS
if 'n' in input('Você é o mito ? '):
	XT = int(input('Digite a largura da sua resolução : '))
	YT = int(input('Digite a altura da sua resolução : '))
else:
	XT = 2560
	YT = 1080

#FUNCTIONS
def upgrade(a,H):
	if H.upper() == 'L':
		return ((a/1360)*XT)
	else:
		return ((a/768)*YT)

def wait(a,b):
	while True:
		if(t.time()-a)>=b:
			break

def digitar(c,w,z):
	pa.click(w,z);pa.typewrite(c);			

 