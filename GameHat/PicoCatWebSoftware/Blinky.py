from machine import Pin
import time

led1 = Pin("LED",Pin.OUT)

print("Running")
for x in range(10):
    led1.on()
    time.sleep(.50)
    
    led1.off()
    time.sleep(.50)


