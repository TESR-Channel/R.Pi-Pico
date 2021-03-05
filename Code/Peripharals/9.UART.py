from machine import Pin
from machine import UART
import utime

uart = UART(0, 9600, bits=8, parity=None, stop=1) # tx=0, rx=1
print(uart)

Button = Pin(16,Pin.IN,Pin.PULL_UP)
count = 0

def button_interrupt_handler(pin):
    global count
    Button.irq(handler=None) # for the disabled interrupt
    uart.write("Press Button") # Write
    utime.sleep(0.25)
    Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

while True:
    print(uart.read()) # Read as much as possible using


