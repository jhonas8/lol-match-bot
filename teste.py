import defs
from aceitar import captar, jogar, parar
import time as t
import pyautogui as pa
from random import randint
import PIL as p
from numpy import array

while True:	
	x = defs.upgrade(randint(10,1000),'l')
	y = defs.upgrade(randint(10,600),'h')
	pa.click(x,y, button='right')
	start=t.time()
	