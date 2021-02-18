from machine import Pin
import utime

# Init HC-SR04 pins
trigger_pin = Pin(14, Pin.OUT)
echo_pin = Pin(13, Pin.IN)

def ultra():
    trigger_pin.high()
    utime.sleep_us(10)
    trigger_pin.low()
    signaloff = 0
    signalon = 0
    while echo_pin.value() == 0:
        signaloff = utime.ticks_us()
    while echo_pin.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = timepassed / 58
    return distance

while True:
    distance_cm = ultra()
    print(str(distance_cm) + " cm")
    utime.sleep(1)            
