'''
Wiring
    Brown   -> Power(10 - 30 VDC)
    Black   -> GND
    Yellow  -> A
    Blue    -> B
'''

#Import module
from machine import UART, Pin

#Declare UART object
uart0 = UART(0, baudrate = 4800, bits=8, parity=None, stop=1) # tx=0, rx=1

#Check UART object
print(uart0)

#Declare GPIO(Button Switch) object
Button = Pin(16,Pin.IN) #In case of using resistor

#Define callback function for external switch
def button_interrupt_handler(pin):
    Button.irq(handler=None) # To disable interrupt
    
    #CO2 request command
    txData = [0x01,0x03,0x00,0x02,0x00,0x01,0x25,0xCA] #b'\x01\x03\x00\x02\x00\x01\x25\xCA'
    
    #Convert list into bytes data
    txBytes = bytearray(txData)
    
    #Transmit data
    uart0.write(txBytes) # Write
    
    #Check transmitted data
    print("Sent data : " + str(txBytes))
    Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

#Declare ISR for external switch
Button.irq(trigger=Pin.IRQ_FALLING,handler=button_interrupt_handler)

RxData = []
index = 0
data = 0
while True:
    
    #Waiting for data to be received
    while(uart0.any()  < 1):
        pass
    
    #When Data received
    while(uart0.any()  > 0): 
        
        #Add received data to RxData list
        RxData.append(uart0.read(1))
        
        #Check if buffer is empty
        index += 1
    
    #Each sensor has maximum data buffer, edit here
    if index == 7:
        
        #Check received data
        print("Received data : " + str(RxData))
        print(RxData)
        
        #Convert received data into CO2 ppm value
        data = ((int.from_bytes(RxData[3], 'big')) << 8) + (int.from_bytes(RxData[4], 'big'))
        
        #Display CO2 ppm data
        print(data)
        
        #Clear buffer
        RxData = []
        
        #Clear index
        index = 0
        