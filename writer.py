import voice
import keyboard
import time

now = time.time()

def writer():
    while True:
        v = voice.speech()
        if not v == None and not v == '':
            keyboard.send("enter")
            keyboard.write(v,0.05)
            keyboard.send("enter")
print(f'{str(now - time.time()).split(".")[0]} sec ')
print('''=================================
===---- Started listening ----===
=================================''')
writer()

