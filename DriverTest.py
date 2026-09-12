# Alternate outputs and count
import time
import board
import digitalio
import busio
from adafruit_ht16k33 import matrix

#led = digitalio.DigitalInOut(board.LED)
ledExt15 = digitalio.DigitalInOut(board.GP15)#
ledExt12 = digitalio.DigitalInOut(board.GP12)
#led.direction = digitalio.Direction.OUTPUT
ledExt15.direction = digitalio.Direction.OUTPUT
ledExt12.direction = digitalio.Direction.OUTPUT

# Create the I2C interface.
i2c = busio.I2C(scl = board.GP9, sda = board.GP8)

# creates a 8x8 matrix:
matrix = matrix.Matrix8x8(i2c)

matrix.brightness = 0.1
# edges of an 8x8 matrix
col_max = 8
row_max = 8

# Clear the matrix.
matrix.fill(0)

#set variables
inject_time = 8
aspirate_time = 7
hundreds = 2 #maximum = 8
    
#counting 100's
for bit6 in range(4,5):
    for bit5 in range(0,hundreds):
        #counting 10's
        for bit4 in range(2,4):
            for bit3 in range(0,5):
                #counting digits
                for bit2 in range(0,2):                                  
                    for bit1 in range(0,5):
                        matrix[bit2,bit1] = 1
                        ledExt15.value = True
                        ledExt12.value = False
                        time.sleep(inject_time)
                        ledExt15.value = False
                        ledExt12.value = True
                        time.sleep(aspirate_time)
                #roll the 10
                matrix[bit4,bit3] = 1
                #clear digits
                for column in range(0,2):
                    for row in range(0,5):
                        matrix[column,row] = 0
        #roll the 100
        matrix[bit6,bit5] = 1
        #clear 10's
        for column in range(2,4):
            for row in range(0,5):
                matrix[column,row] = 0