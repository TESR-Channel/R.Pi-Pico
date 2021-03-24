from machine import WDT
import utime

WatchDogTime_ms = 5000
wdt = WDT(timeout = WatchDogTime_ms)  # enable it with a timeout of 5s
wdt.feed()
print("Start System.")

Button = machine.Pin(2,machine.Pin.IN,machine.Pin.PULL_UP)

def button_interrupt_handler(pin):
    global count
    Button.irq(handler=None) # for the disabled interrupt
    count = int(WatchDogTime_ms/1000);
    wdt.feed()
    print("Continue")
    Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=button_interrupt_handler)

Button.irq(trigger=machine.Pin.IRQ_FALLING,handler=button_interrupt_handler)

count = int(WatchDogTime_ms/1000);
while True:
    print("System will Reboot in " + str(count))
    count = count - 1
    if count == 0:
        while True:
            Button.irq(handler=None) # for the disabled interrupt
            print("Reboot now.")
            utime.sleep(1)
    utime.sleep(1)
    
    