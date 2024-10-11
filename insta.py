import time
import webbrowser
import pyautogui
import sys
import argparse
 
def getOptions(args=sys.argv[1:]):
    praser = argparse.ArgumentParser(description="Instagram Mass Report")
    praser.add_argument("-u", "--username", type = str,default="eren", required=False) #write the username of the person u want to mass report 
    options = praser.parse_args(args)
    return options
 
args = getOptions()
username = args.username
 
# if it is false then this would work 
 
if username == "":
    username = input("username: ")
 
while True:
    count = 0
    while count < 10: # the number u want its enough ig lmao
 
        webbrowser.open(f'https://www.instagram.com/{username}')
        time.sleep(4.5)
        pyautogui.click(1138,180)
        time.sleep(2)
        pyautogui.click(952,532)
        time.sleep(0.5)
        pyautogui.click(910,656)
        time.sleep(0.8)
        pyautogui.click(990 , 581)
        time.sleep(0.5)
        pyautogui.click(780 , 456)
        time.sleep(0.8)
        pyautogui.click(954 , 794)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        count =+ 1
choice = input("Do you want to continue? (y/n): ")
if choice == "n":
    sys.exit()
