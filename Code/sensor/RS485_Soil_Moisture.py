'''
Wiring
    This manual using sensor that has a weird wire color.
    Please check your datasheet to ensure the color of wire.
    
    Brown       ->  Power(5 - 30 VDC (Recommend : Up to 12 VDC))
    Blue        ->  GND
    Black       ->  A
    Grey        ->  B
    No shield   ->  No connect
'''

#Import module
from machine import UART, Pin

#Declaration of variable objects
#Each sensor has maximum data buffer, edit the max_index as your desire
RxData = []
index = 0
tim_ready = 0
max_index = 9

#Declare UART object (TX = PIN0, RX = PIN1)
uart0 = UART(0, baudrate = 4800, bits=8, parity=None, stop=1)

#Check UART object
print(uart0)

#Define callback function for Timer Interrupt
def send(d):
    
    #Check if callback is enable
    if tim_ready == 1:
        
        #Data-read command
        txData = b'\x01\x03\x00\x00\x00\x02\xC4\x0B'
        
        #Transmission command
        uart0.write(txData)
        
        #Check transmitted command
        print("Sent data : " + str(txData))
        
        #Disable callback for a while
        tim_ready == 0

#Define timer trigger every 1 second and use send() as callback function
tim = machine.Timer()
tim.init(period = 1000, callback = send)

#Define convertion function
def to_moisture(d1, d2):
    return (float)(((int.from_bytes(d1, 'big')) << 8) + (int.from_bytes(d2, 'big')))/10

def to_temp(d1, d2):
    return (float)(((int.from_bytes(d1, 'big')) << 8) + (int.from_bytes(d2, 'big')))/10

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
        
        #Convert data using function
        moisture = to_mois(RxData[3], RxData[4])
        temperature = to_temp(RxData[5], RxData[6])
        
        #Display moisture and temperature values
        print("Moisture : " + str(moisture) + " %")
        print("Temperature : " + str(temperature) + " °C")
        
        #Clear buffer
        RxData = []
        
        #Clear index
        index = 0
        