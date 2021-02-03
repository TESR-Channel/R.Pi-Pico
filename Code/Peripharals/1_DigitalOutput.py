import machine
import utime

ledOnboard_pin = 25
ledOnboard = machine.Pin(ledOnboard_pin,machine.Pin.OUT)
ON = 1
OFF = 0

while True:
    ledOnboard.value(ON)
    utime.sleep(1) # delay 1 sec
    ledOnboard.value(OFF)
    utime.sleep(1) # delay 1 sec