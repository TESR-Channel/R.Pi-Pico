'''
Wiring
    Brown   -> Power(5 - 30 VDC)
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

#Define callback function for Timer Interrupt
def send(d):
    
    #Check if callback is enable
    if tim_ready == 1:
        
        #Data-read command
        txData = b'\x01\x03\x00\x00\x00\x01\x84\x0A'
        
        #Transmission command
        uart0.write(txData)
        
        #Check transmitted command
        print("Sent data : " + str(txData))
        
        #Disable callback for a while
        tim_ready == 0

#Define timer trigger every 1 second and use send() as callback function
tim = machine.Timer()
tim.init(period = 1000, callback = send)

#Declaration of variable objects
#Each sensor has maximum data buffer, edit the max_index as your desire
RxData = []
index = 0
max_index = 7
tim_ready = 0

#The main loop start here
while True:
    
    #Enable callback
    tim_ready = 1
    
    #Waiting for data to be received
    while(uart0.any()  < 1):
        pass
    
    #When Data received
    while(uart0.any()  > 0): 
        
        #Add received data to RxData list
        RxData.append(uart0.read(1))
        
        #Check if buffer is empty
        index += 1
    
    #When all data has been received
    if index == max_index:
        
        #Check received data
        print("Received data : " + str(RxData))
        
        #Convert received data into ph value
        ph = (float)((int.from_bytes(RxData[3], 'big')) << 8) + (int.from_bytes(RxData[4], 'big'))/10
        
        #Display ph value
        print("PH : " + str(ph))
        
        #Clear buffer
        RxData = []
        
        #Clear index
        index = 0
        