import machine
import utime

ledOnboard_pin = 25
ledOnboard = machine.Pin(ledOnboard_pin,machine.Pin.OUT)
output_state = True

delay_ms = 1000
time_now = utime.ticks_ms()
time_previous = utime.ticks_ms()

while True:
    time_now = utime.ticks_ms()
    if time_now - time_previous >= delay_ms:
        output_state = 1 - output_state
        ledOnboard.value(output_state)
        time_previous = time_now
    
