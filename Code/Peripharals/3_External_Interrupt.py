import machine
import utime

Button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)
count = 0

def button_interrupt_handler(pin):
    global count
    Button.irq(handler=None) # for the disabled interrupt
    count = count + 1
    print("Press count: " + str(count))
    utime.sleep(0.25)
    Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=button_interrupt_handler)

Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=button_interrupt_handler)

while True:
    pass

