from pyfirmata import Arduino
import time

LED = 13
arduino = Arduino("/dev/ttyACM0")

for x in range (10):
    arduino.digital[LED].write(1)
    time.sleep(.500)
    arduino.digital[LED].write(0)
    time.sleep(.500)