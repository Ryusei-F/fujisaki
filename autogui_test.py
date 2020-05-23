import pyautogui
import sys
import time
import re


s = 'DOWN_10'
print(re.match(r'DOWN_.[0-9]*', s))

time_ = re.match(r'DOWN_.*', s)
print(time_)

def cut(arg):
    # time = arg.split('_')[1]
    m = re.findall(r'[0-9]+\.?[0-9]*', arg)
    print(type(m))
    print(m.group())
    ##print(arg.replace('DOWN_', ''))
    
    #return float(res)

#if message.content == 'down' or re.match(r'DOWN_.*', message.content):
#    time = (DOWN_の後が数字) ? DOWNの後 : DEFAULT;

##print(cut(s))
#cut(s)
s2 = 'UP'
result = re.match(r'UP_.*', s2)
print(re.match(r'UP_.*', s2) != None)
print(type(result))


def isNumber(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False

def cutDown(arg):
  DEFAULT = 1.0
  a = arg.replace('DOWN_', '')
  if (isNumber(a)):
      return float(a)
  else:
      return DEFAULT

# print(cutDown('DOWN_123'))
# print(cutDown('DOWN_155.0'))
# print(cutDown('DOWN_BBB'))