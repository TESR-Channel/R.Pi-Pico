'''
Wiring
    Brown   -> Power(4.5 - 30 V)
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

#Declaration of variables
timeout = 0
tim_ready = 0
max_index = 7
RxData = []
index = 0

#Define callback function for Timer Interrupt
def send(d):
    
    #Using global function to specify the variable that use as global variable
    global max_index
    global timeout
    
    #Check if callback is enable
    if tim_ready == 1:
        
        #Clear data in register if sensor at the beginning and every 10 second
        if timeout == 0 :
            
            #Register-clear command
            txData = b'\x01\x06\x00\x00\x00\x5A\x09\xF1'
            
            #Transmission command
            uart0.write(txData)
            print("Rainfall Reset...")
            
            #Set the max_index in case of sending clear-command
            max_index = 8
        
        #Read data in register
        else :
            
            #Set the max_index to normal
            max_index = 7
            
            #Data-read command
            txData = b'\x01\x03\x00\x00\x00\x01\x84\x0A'
            
            #Transmission command
            uart0.write(txData)
            
        #Check transmitted command
        print("Sent data : " + str(txData))
        
        #Disable callback for a while
        tim_ready == 0
        
        #Counter flag
        timeout = (timeout + 1) % 10

#Define timer trigger every 1 second and use send() as callback function
tim = machine.Timer()
tim.init(period = 1000, callback = send)

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
        
        #Convert received data into rainfall value
        rain = (float)((int.from_bytes(RxData[3], 'big')) << 8) + (int.from_bytes(RxData[4], 'big'))/10

        #Display Rainfall value
        print("Rainfall value : " + str(rain) + " mm")
        
        #Clear buffer
        RxData = []
        
        #Clear index
        index = 0
