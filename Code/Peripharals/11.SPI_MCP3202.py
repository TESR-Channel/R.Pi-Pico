import machine
import utime

spi = machine.SPI(0, baudrate = 1000000, sck = machine.Pin(2), mosi = machine.Pin(3), miso = machine.Pin(4))
print(spi)

cs_pin = 5
cs = machine.Pin(cs_pin,machine.Pin.OUT)

#cs = machine.Pin(5) # Active Low
ready_flag = 0

def get_adc(channel):
    if channel == 0x00:
        channel = 0xD0 # Select Channel 0
    else:
        channel = 0xF0 # Select Channel 1
        
    cs.value(0)# Enable MCP3202
    utime.sleep(0.05)

    raw = bytearray(3)
    #spi.write_readinto(bytes([0xD0, 0x00, 0x00]), raw) # send a receive 3 bytes
    spi.write_readinto(bytes([channel, 0x00, 0x00]), raw) # send a receive 3 bytes
    
    print(raw)
    utime.sleep(0.05)
    cs.value(1)# Disable MCP3202
    
    #Convert bytes array into list
    cal = list(raw)
    ADC = ((cal[0]&0x07)<<9) + (cal[1]<<1) + ((cal[2]&0x80)>>7)

    #Debug
    print("Voltage : " + str(ADC * 5 / 4096) + " v")
    
    #Return Digital value
    return ADC
        

while True:
    ADC = get_adc(0)
    print("Digital : " + str(ADC))
    utime.sleep(0.5)
    