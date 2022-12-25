# To run this script you'll have to install the following dependencies:
# $ pip3 install pyautogui
#
# Note: it may also ask you to install:
# $ sudo apt-get install python3-tk python3-dev
# $ sudo apt-get install scrot
#
# This program is intendeed to work on a FullHD screen
#

import time
import os
import pyautogui

# Put the ratios (in pixels it must be a ratio between 4/3 and 16/9) here that you want
ratios = [[539, 403], [809, 601], [1330, 792], [1378, 950], [1797, 1209], [1910, 1420], [2267, 1638], [2763, 1817], [2888, 1971], [3775, 2124]]

# Indicate the number of generatios you want for each ratio
n = 10

def open_gimp():
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write('gimp', interval=0.25)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)

def changes():
    pix = pyautogui.pixel()

def main():
    print("Starting...")
    #Pixel that we'll take to check if the processing has finished
    temp_x = 560
    temp_y = 388
    ratios.sort(key=lambda y: y[0]*y[1])
    #ratios = ratios[8:]
    print(ratios)
    pyautogui.moveTo(temp_x, temp_y, duration=1)
    time.sleep(5)
    open_gimp()
    pyautogui.click()
    #print('Please make sure Gimp is open and click its windows before 5 seconds')
    path = os.getcwd()
    with open(path+'/'+'resultats.txt', 'a') as f:
        for [x, y] in ratios:
            n_pixels = x*y
            f.write("Result for ratio (" + str(x) + " " + str(y) + " ("+ str(n_pixels) +")) : ")
            for i in range (0, n):
                ### Creating new file with size x y
                pyautogui.hotkey('ctrl', 'n')
                time.sleep(0.2)
                print('New file with size', x, y)
                pyautogui.press('tab')
                time.sleep(0.2)
                pyautogui.write(str(y), interval=0.2)
                pyautogui.hotkey('shift', 'tab')
                pyautogui.write(str(x), interval=0.2)
                pyautogui.press('enter')
                ### Fit image
                time.sleep(0.2)
                pyautogui.hotkey('shift', 'ctrl', 'j')
                time.sleep(0.2)
                ### Obtain a pixels to later compare its content
                pixels = (pyautogui.pixel(temp_x, temp_y))#, pyautogui.pixel(880,800), pyautogui.pixel(920, 830),pyautogui.pixel(520, 400), pyautogui.pixel(588, 420))
                pixels_new = pixels
                ### Generate a IFS Fractal
                time.sleep(0.3)
                pyautogui.hotkey('alt', 'r')
                time.sleep(0.2)
                pyautogui.press('r')
                time.sleep(0.2)
                pyautogui.press('f')
                time.sleep(0.2)
                pyautogui.press('i')
                time.sleep(1)
                pyautogui.hotkey('alt', 'r')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press(['right'])
                time.sleep(1)
                pyautogui.press('enter')
                t_before = time.perf_counter()
                while(pixels == pixels_new):
                    #print(pixels)
                    pixels = (pyautogui.pixel(temp_x, temp_y))#, pyautogui.pixel(880,800), pyautogui.pixel(920, 830),pyautogui.pixel(520, 400),pyautogui.pixel(588, 420))
                t_total = time.perf_counter() - t_before
                print("Time to generate:", t_total)
                time.sleep(2)
                f.write(str(t_total))
                if(i != n-1): f.write(', ')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(1)
                pyautogui.hotkey('alt', 'd')
                time.sleep(0.5)
            f.write('\n')
        pyautogui.hotkey('alt'+'f4')


if __name__ == "__main__":
	main()
