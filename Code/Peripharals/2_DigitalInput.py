import machine
import utime

Button_pin = 2 # Connect a switch to GPIO2 and no need a resistor.
Button = machine.Pin(Button_pin,machine.Pin.IN,machine.Pin.PULL_UP)
Press = 0
Relese = 1

count = 0

while True:
    if Button.value() == Press:
        count = count + 1
        print("Press Button:" + str(count))
    else:
        pass
    utime.sleep(0.25)
