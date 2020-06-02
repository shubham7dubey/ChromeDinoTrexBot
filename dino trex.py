import time
import pyautogui
import numpy as np
from PIL import Image,ImageOps,ImageGrab
import matplotlib.pyplot as plt
print("starting")
time.sleep(2)
pyautogui.keyDown('space')
l=0
thresh = "day"
st = time.time()
while(1):
    img = ImageGrab.grab().convert('L')
    image_array = img.load()
    print(thresh)
    if image_array[100,100] > 125:
        thresh = "day"
    else:
        thresh = "night"
    flag = False
    tm = (int)(time.time() - st)
    tm /= 6
    for i in range(50,100): 
        if thresh == "night":
            if image_array[470+i+tm,640] >50 or image_array[470+i,620]>50 or image_array[470,640-i+70]>50:
                flag = True
                break
        else:
            if image_array[470+i + tm,640]  < 200  or image_array[470+i,620] < 200 or image_array[470,640-i+70] < 200:
                flag = True
                break 
    dn = False
    cnt = 0
    cnt1 = 0
    for i in range(50,100):
        if thresh == "night":
            if image_array[400+i,610] > 50:
                cnt+=1
            if image_array[400+i,650] > 50:
                cnt1 += 1
        else:
            if image_array[400+i,610] <200 :
                cnt+=1
            if image_array[400+i,650] <300:
                cnt1 += 1
    if cnt > 0 and cnt1 == 0:
        dn = True
    else:
        dn = False

    l+=1
    print((int)(time.time() - st))
    
    if flag:
        print("button pressed")
        pyautogui.keyDown('up')
    elif dn:
        print("down button pressed")
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyDown('up')
print(time.time() - st)
print("done")