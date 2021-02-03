import machine
import utime

internal_Temp_sensor_pin = 4
sensor_temp = machine.ADC(internal_Temp_sensor_pin)

while True:
    ADC_Temp = sensor_temp.read_u16()
    Voltage_Temp = (ADC_Temp * 3.3)/65535
    Temp = 27 - (Voltage_Temp - 0.706)/0.001721
    print("===============================")
    print("ADC = " + str(ADC_Temp))
    print("Voltage = " + str(Voltage_Temp) + " v")
    print("Temperature = " + str(Temp) + " °C")
    print("===============================")
    utime.sleep(1) # delay 1 sec