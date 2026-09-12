# Binary counter on the adafruit 8x8 matrix backpack
import time
import board
import busio
import random
from adafruit_ht16k33 import matrix

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
col = 0
row = 0

#infinitely fill each row in turn, counting in binary
j = 0
while j == 0:
    i = 0
    while i < 8:
        for bit8 in range(0,2):
            for bit7 in range(0,2):
                for bit6 in range(0,2):
                   for bit5 in range(0,2):
                        for bit4 in range(0,2):
                            for bit3 in range(0,2):
                                for bit2 in range(0,2):
                                        for bit1 in range(0,2):
                                            matrix[i,0] = bit1
                                            matrix[i,1] = bit2
                                            matrix[i,2] = bit3
                                            matrix[i,3] = bit4
                                            matrix[i,4] = bit5
                                            matrix[i,5] = bit6
                                            matrix[i,6] = bit7
                                            matrix[i,7] = bit8
                                            time.sleep(1)
        i = i+1
    matrix.fill(0)

