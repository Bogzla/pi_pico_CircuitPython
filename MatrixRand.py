# random pattern of appearing and disappearing pixels on the adafruit 8x8 matrix backpack
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

while True:
    col = random.randrange(0,9)
    row = random.randrange(0,9)
    if matrix[row, col] == 1:
        matrix[row, col] = 0
    else:
        matrix[row, col] = 1

    time.sleep(.01)