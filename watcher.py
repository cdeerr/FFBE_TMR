from PIL import ImageChops
from PIL import ImageGrab
from PIL import Image
import pyautogui
import time
import threading
import datetime
import sys

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# load images
print("Loading images...")
earth_shrine_label_img = Image.open("esLabel.png")
earth_shrine_ent_img = Image.open("esEntLabel.png")
select_companion_img = Image.open("selectCompanion.png")
depart_img = Image.open("depart.png")
es_done_img = Image.open("esDone.png")
items_obtained_img = Image.open("itemsObtained.png")
add_companion_img = Image.open("addCompanion.png")
print("Images loaded...")

def comp_images(im1, im2):
	return ImageChops.difference(im1, im2).getbbox() is None

def click(location):
	pyautogui.mouseDown(location, button='left')
	time.sleep(1.0)
	pyautogui.mouseUp(location, button='left')

def process():
	print("Starting bot...")
	while True:
		time.sleep(5.0)
		location = pyautogui.locateCenterOnScreen("selectES.png")

		if (location):
			print("ES Label found")
			location = tuple([x/2 for x in location])
			click(location)


thread = threading.Thread(target=process)
thread.daemon = True
thread.start()

try :
	input('Press enter to end the program')
except SyntaxError:
	sys.exit(0)
sys.exit(0)
