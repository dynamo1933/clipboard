import time
import sys
import os
from datetime import datetime


sys.path.append(os.path.abspath("SO_site-packages"))

def writeintofile(value):
    with open('c:/Users/91800/Desktop/clipboard.txt','a') as file:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file.write(dt_string+'\n'+value+'\n')
        
    pass



import pyperclip

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        writeintofile(str(recent_value))
        print("Value changed: %s" % str(recent_value))
    time.sleep(0.5)