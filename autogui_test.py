import time
import threading

def boil_udon():
  print('  うどんを茹でます。')
  time.sleep(3)
  print('  うどんが茹であがりました。')

def make_tuyu(msg):
  print('  ツユをつくります。')
  print('  ツユができました。' + msg)

print('うどんを作ります。')
thread1 = threading.Thread(target=boil_udon)
threading.Thread(target=make_tuyu, args=("aaa", )).start()
thread1.start()

#thread1.join()
#thread2.join()
print('盛り付けます。')
