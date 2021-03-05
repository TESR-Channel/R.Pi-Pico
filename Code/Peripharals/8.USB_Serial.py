from machine import Pin
import utime

Button = Pin(16,Pin.IN,Pin.PULL_UP)
count = 0

def button_interrupt_handler(pin):
    global count
    Button.irq(handler=None) # for the disabled interrupt
    count = count + 1
    print("Press count: " + str(count))
    utime.sleep(0.25)
    Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

while True:
    Data = input("Enter your input:")
    print(Data)

