import PIL as p
import defs
from numpy import array
#Imagem de aceitar 

x1 = [defs.upgrade(587,'l'),defs.upgrade(784,'l')]
y1 = [defs.upgrade(530,'h'),defs.upgrade(579,'h')]

def captar():
	box = (x1[0],y1[0],x1[1],y1[1])
	while True:
		image = p.ImageGrab.grab(box)
		grayI = p.ImageOps.grayscale(image)	
		pixels = array(grayI.getcolors())
		print(pixels.sum())
		if pixels.sum()>=25000 and pixels.sum()<=27500:
			break
		if pixels.sum()>=40000 and pixels.sum()<=42500:
			return 0
			break	
		if pixels.sum()>=9680 and pixels.sum()<=9700:
			return 0
			break	
 
def jogar():
	while True:
		bbox = (1191,643,1227,690)
		bbgameImage = p.ImageGrab.grab(bbox)
		bbgrayGame = p.ImageOps.grayscale(bbgameImage)
		bbpixelGame = array(bbgrayGame.getcolors())
		print(bbpixelGame.sum())
		if bbpixelGame.sum()>=6800 and bbpixelGame.sum()<=7100:
			break

def escolher():
	bbbox = (384,93,576,113)
	while True:
		bimage = p.ImageGrab.grab(bbbox)
		bgrayI = p.ImageOps.grayscale(bimage)	
		bpixels = array(bgrayI.getcolors())
		print(bpixels.sum())
		if bpixels.sum()>=7960 and bpixels.sum()<=7961:
			break

def parar():
	bbbox = (488,122,566,201)
	bbbgameImage = p.ImageGrab.grab(bbbox)
	bbbgrayGame = p.ImageOps.grayscale(bbbgameImage)
	bbbpixelGame = array(bbbgrayGame.getcolors())
	print(bbbpixelGame.sum())
	if bbbpixelGame.sum()>=20749 and bbbpixelGame.sum()<=21620:
		return 0

def checkarTime():
	while True:	
		block = (467,666,673,711)
		blockgameImage = p.ImageGrab.grab(block)
		blockgrayGame = p.ImageOps.grayscale(blockgameImage)
		blockpixelGame = array(blockgrayGame.getcolors())
		print(blockpixelGame.sum())
		if blockpixelGame.sum()>=25968 and blockpixelGame.sum()<=25970:
			break