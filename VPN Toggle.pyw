#! python3
from PIL.ImageOps import grayscale
import pyautogui
import time
import os

#Used to Determine Click Points and Offsets during setup
#pyautogui.displayMousePosition()

search_region = 1500,1000,300,200
pw = 'yourpasswordhere'
disconnected_path = 'path to collection of disconnected images'
connected_path = 'path to collection of connected images'

#Find All Images, depending on which monitor is being used, the images will be different
connected_images = os.listdir(connected_path)
disconnected_images = os.listdir(disconnected_path)

def connect(point):
    print('disconnected image found: ' + disconnected_path + image + ', connecting')
    pyautogui.rightClick(point)
    pyautogui.leftClick(point.x - 110, point.y - 83)
    time.sleep(1)
    pyautogui.write(pw)
    pyautogui.press('enter')
    exit()

def disconnect(point):
    print('connected image found: ' + connected_path + image + ', disconnecting')
    pyautogui.rightClick(point.x, point.y)
    pyautogui.leftClick(point.x - 100, point.y - 66)
    time.sleep(0.3)
    pyautogui.press('enter')
    exit()

def find_image(image):
    return pyautogui.locateCenterOnScreen(image, grayscale= False, region= search_region)

#Iterate Through Connected Images
for image in connected_images:
    connected_found = find_image(connected_path + image)
    #Connected Icon Detected
    if connected_found != None:
        disconnect(connected_found)

#Iterate Through Disconnected Images
for image in disconnected_images:
    disconnected_found = find_image(disconnected_path + image)
    #Disconnected Icon Deteced
    if disconnected_found != None:
        connect(disconnected_found)
    
#Neither Image Detected
print('Neither Image Found')
pyautogui.alert('No images found', 'Error - VPN Toggle')
exit()
