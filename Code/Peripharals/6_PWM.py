import machine
import utime

ledOnboard_pin = 25
ledOnboard = machine.PWM(machine.Pin(ledOnboard_pin))
ledOnboard.freq(1000)
while True:
    for duty in range(0,65536):
        ledOnboard.duty_u16(duty)
    for duty in range(65535,-1,-1):
        ledOnboard.duty_u16(duty)
