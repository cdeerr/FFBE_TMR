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
earth_shrine_label_Caleb_img = Image.open("esLabel_Caleb.png")
earth_shrine_ent_img = Image.open("esEntLabel.png")
select_companion_img = Image.open("selectCompanion.png")
companion_rank_label_img = Image.open("companionRankLabel.png")
depart_img = Image.open("depart.png")
auto_label_img = Image.open("AutoLabel.png")
es_done_img = Image.open("esDone.png")
unit_exp_label_img = Image.open("unitExpLabel.png")
items_obtained_img = Image.open("itemsObtained.png")
add_companion_img = Image.open("addCompanion.png")

next_button_label_img = Image.open("nextButtonLabel.png")
dont_request_button_label_img = Image.open("dontRequestButtonLabel.png")
close_quest_button_label_img = Image.open("closeButtonLabel.png")
print("Images loaded...")

def comp_images(im1, im2):
	return ImageChops.difference(im1, im2).getbbox() is None

def click(location):
	pyautogui.mouseDown(location, button='left')
	time.sleep(0.5)
	pyautogui.mouseUp(location, button='left')

def process():
	print("Starting bot... \n")
	#pattern: selectES -> esEntLabel (click next) -> selectCompanion.png (click top option) -> 
	#             Depart (click bottom of screen) -> click AUTO -> 
	#             esDone (click next) -> RESULTS unit exp screen (click anywhere) -> itemsObtained (click next)
	#             addCompanion (click either option)
	while True:
		time.sleep(5.0)
		selectESLocation = pyautogui.locateCenterOnScreen("selectES.png")
		print(selectESLocation)
		esLabelCalebLocation = pyautogui.locateCenterOnScreen("esLabel_Caleb.png")
		print(esLabelCalebLocation)
	   	esEntLabelLocation = pyautogui.locateCenterOnScreen("esEntLabel.png")
		selectCompanionLocation = pyautogui.locateCenterOnScreen("selectCompanion.png")
		companionRankLabelLocation = pyautogui.locateCenterOnScreen("companionRankLabel.png")
		departLocation = pyautogui.locateCenterOnScreen("depart.png")
		autoLocation = pyautogui.locateCenterOnScreen("AutoLabel.png")
		esDoneLocation = pyautogui.locateCenterOnScreen("esDone.png")
		unitExpLocation = pyautogui.locateCenterOnScreen("unitExpLabel.png")
		itemsObtainedLocation = pyautogui.locateCenterOnScreen("itemsObtained.png")
		addCompanionLocation = pyautogui.locateCenterOnScreen("addCompanion.png")
		nextButtonLabelLocation = pyautogui.locateCenterOnScreen("nextButtonLabel.png")
		dontRequestLabelLocation = pyautogui.locateCenterOnScreen("dontRequestButtonLabel.png")
		closeButtonLabelLocation = pyautogui.locateCenterOnScreen("closeButtonLabel.png")
		print("Checking images... \n")
		if (esLabelCalebLocation):
			print("Earth Shrine Label found \n")
			esLabelCalebLocation = tuple([x/2 for x in esLabelCalebLocation])
			click(esLabelCalebLocation)
		if(esEntLabelLocation and nextButtonLabelLocation):
			print("Earth Shrine Entrance Label found \n")
			nextButtonLabelLocation = tuple([x/2 for x in nextButtonLabelLocation])
			click(nextButtonLabelLocation)
		if(selectCompanionLocation and companionRankLabelLocation):
			print("Select Companion found \n")
			companionRankLabelLocation = tuple([x/2 for x in companionRankLabelLocation])
			click(companionRankLabelLocation)
		if(departLocation):
			print("Depart found \n")
			departLocation = tuple([x/2 for x in departLocation])
			click(departLocation)
		if(autoLocation):
			print("AUTO Label found \n")
			autoLocation = tuple([x/2 for x in autoLocation])
			click(autoLocation)
			#click AUTO then wait for battle to play out
			time.sleep(10.0)
		if(esDoneLocation and nextButtonLabelLocation):
			print("Earth Shrine Done found \n")
			nextButtonLabelLocation = tuple([x/2 for x in nextButtonLabelLocation])
			click(nextButtonLabelLocation)
		if(unitExpLocation):
			print("Unit Experience found \n")
			unitExpLocation = tuple([x/2 for x in unitExpLocation])
			click(unitExpLocation)
		if(itemsObtainedLocation and nextButtonLabelLocation):
			print("Items Obtained found \n")
			nextButtonLabelLocation = tuple([x/2 for x in nextButtonLabelLocation])
			click(nextButtonLabelLocation)
		if(addCompanionLocation and dontRequestLabelLocation):
			print("Add Companion found \n")
			dontRequestLabelLocation = tuple([x/2 for x in dontRequestLabelLocation])
			click(dontRequestLabelLocation)

thread = threading.Thread(target=process)
thread.daemon = True
thread.start()

try :
	input('Press enter to end the program \n')
except SyntaxError:
	sys.exit(0)
sys.exit(0)
