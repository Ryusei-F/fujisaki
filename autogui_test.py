import re

# Input Config
UP_BUTTON =    ['1', 'e', 'g', 'up']
LEFT_BUTTON =  ['2', 'left', 'h', '[']
DOWN_BUTTON =  ['3', 't', 'j', 'down']
RIGHT_BUTTON = ['4', 'y', 'k', 'right']
B_BUTTON=      ['5', 'u', 'l', 'backspace']
A_BUTTON=      [';', 'i', 'z', 'enter']
Y_BUTTON=      [':', 'o', 'x', 'space']
X_BUTTON=      ['8', 'p', 'c', 'home']
START_BUTTON=  ['9', 'a', 'v', 'pageup']
SELECT_BUTTON= ['0', 's', 'b', 'pagedown']
L_BUTTON=      ['q', 'd', 'n', 'enter']
R_BUTTON=      ['w', 'f', 'm', 'delete']
SLEEP_TIME=0.0
CORRESP_EMU_BUTTON= {'UP_BUTTON': UP_BUTTON, 'LEFT_BUTTON': LEFT_BUTTON, 'DOWN_BUTTON': DOWN_BUTTON, 'RIGHT_BUTTON': RIGHT_BUTTON,
                     'A_BUTTON': A_BUTTON, 'B_BUTTON': B_BUTTON, 'Y_BUTTON': Y_BUTTON, 'X_BUTTON': X_BUTTON,
                     'START_BUTTON': START_BUTTON, 'SELECT_BUTTON': SELECT_BUTTON, 'L_BUTTON': L_BUTTON, 'R_BUTTON': R_BUTTON}
BUTTON_LIST= {'w': 'UP_BUTTON', 'a': 'LEFT_BUTTON', 's':'DOWN_BUTTON', 'd':'RIGHT_BUTTON',
              'l': 'A_BUTTON', 'k': 'B_BUTTON', 'i': 'X_BUTTON', 'j': 'Y_BUTTON',
              'start': 'START_BUTTON', 'select': 'SELECT', 'u': 'L_BUTTON', 'o': 'R_BUTTON'}

def changekey(aaa):
    global BUTTON_LIST
    if re.match(r'.changekey\s[a-zA-Z]\s[a-zA-Z]' ,aaa):
        print(aaa.split(' ')[2])
        if aaa.split(' ')[1] in BUTTON_LIST and aaa.split(' ')[2] not in BUTTON_LIST:
            BUTTON_LIST= {aaa.split(' ')[1]: aaa.split(' ')[2]}
            print('aaa.split(' ')[1] :' + aaa.split(' ')[1])
            print('aaa.split(' ')[2] :' + aaa.split(' ')[2])
            print('BUTTON_LIST[aaa.split(' ')[1]] :' + BUTTON_LIST[aaa.split(' ')[1]])
        else:
            print('キー変更できないよ')
    else:
        print('マッチエラー')

s1 = '!changekey w a'
s2 = '!changekey l 0'

changekey(s1)
changekey(s2)

print("aaaaaa bbbbb".split(' ')[0])
for aa in list("aavvasaa"):
    print(aa)