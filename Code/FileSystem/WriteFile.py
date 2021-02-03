import random
import utime

file = open("SaveData.txt","w")
for count in range(0,5):
    num = random.randint(0,100)
    print("Save data = " + str(num))
    file.write(str(num) + " \r\n")
    utime.sleep(0.1)
file.close()
print("Write File Done.")
    