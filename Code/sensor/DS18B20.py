import machine
import onewire, ds18x20
import utime
 
DS18B20_pin = machine.Pin(15)
DS18B20_sensor = ds18x20.DS18X20(onewire.OneWire(DS18B20_pin))
 
ROMS_Address = DS18B20_sensor.scan()
print("Found a DS18B20 device")
print(len(ROMS_Address))
print(ROMS_Address)
print(hex(ROMS_Address[0][0]) + ":" + hex(ROMS_Address[0][1]) + ":" + hex(ROMS_Address[0][2]) + ":" + hex(ROMS_Address[0][3])
      + ":" + hex(ROMS_Address[0][4]) + ":" + hex(ROMS_Address[0][5]) + ":" + hex(ROMS_Address[0][6])
      + ":" + hex(ROMS_Address[0][7]))
 
while True:
  DS18B20_sensor.convert_temp()
  utime.sleep(0.75)
  for Address in ROMS_Address:
    print(str(DS18B20_sensor.read_temp(Address)) + " °C")
  utime.sleep(1)