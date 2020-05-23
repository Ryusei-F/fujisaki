import pyautogui
import sys
import time


screen_x,screen_y = pyautogui.size()
curmus_x,curmus_y = pyautogui.position()
print (u"printについてる[u]はunicodeにするのuでマルチバイト表記が化けるときにつけるよ")
print (u"画面サイズ [" + str(screen_x) + "]/[" + str(screen_y) + "]")
print (u"現在のマウス位置 [" + str(curmus_x) + "]/[" + str(curmus_y) + "]")
center_x = screen_x / 2
center_y = screen_y / 2
print (u"画面中央 [" + str(center_x) + "]/[" + str(center_y) + "]")
pyautogui.moveRel(100,100)
interval = 0
pyautogui.typewrite('Hello world!\n', interval)  # intervalは文字間の入力待機時間です．
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval) #配列にも対応しています．
#print(pyautogui.KEYBOARD_KEYS)