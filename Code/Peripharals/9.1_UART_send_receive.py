from machine import UART, Pin
import utime

uart0 = UART(0, baudrate = 115200, bits = 8, parity = None, tx = Pin(0), rx = Pin(1))
print(uart0)

def button_interrupt_handler(pin):
    Button.irq(handler=None) # for the disabled interrupt
    txData = [0x01,0x03,0x00,0x02,0x00,0x01,0x25,0xCA] 
    uart0.write(bytearray(txData)) # Write
    print("Sent data : " + str(txData))
    utime.sleep(0.25)
    Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

RxData = []
while True:
    while(uart0.any()  < 1):
        pass
    while(uart0.any()  > 0): 
        RxData.append(uart0.read(1))
    print(RxData)
    RxData = [] # Clear RxData