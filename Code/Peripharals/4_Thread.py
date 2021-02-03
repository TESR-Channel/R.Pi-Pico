import machine
import utime
import _thread

ledOnboard = machine.Pin(25,machine.Pin.OUT)
ON = 1
OFF = 0

Button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)
Press = 0
Relese = 1
count = 0

def Button_Check_thread():
    global count
    print("Thread Start.")
    while True:
        if Button.value() == Press:
            count = count + 1
            print("Button Press : " + str(count))
        utime.sleep(0.25)
        
_thread.start_new_thread(Button_Check_thread,()) # for Starting new thread

while True:
    ledOnboard.value(ON)
    utime.sleep(1) # delay 1 sec
    ledOnboard.value(OFF)
    utime.sleep(1) # delay 1 sec