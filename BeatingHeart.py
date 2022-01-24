# Beating heart animation for the adafruit 8x8 matrix backpack
import time
import board
import busio

# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix


# Create the I2C interface.
i2c = busio.I2C(scl = board.GP9, sda = board.GP8)

# Create the matrix class.
matrix = matrix.Matrix8x8(i2c)
matrix.brightness = 0.2


# Draw a Heart
matrix.fill(0)

while True:
    matrix[1, 1] = 1
    matrix[1, 2] = 1
    matrix[1, 5] = 1
    matrix[1, 6] = 1
    for column in range(0, 8):
        matrix[2, column] = 1
        matrix[3, column] = 1
    for column in range(1, 7):
        matrix[4, column] = 1
    for column in range(2, 6):
        matrix[5, column] = 1
    matrix[6, 3] = 1
    matrix[6, 4] = 1
    
    time.sleep(1)
    
    matrix.fill(0)
    matrix[2, 1] = 1
    matrix[2, 2] = 1
    matrix[2, 5] = 1
    matrix[2, 6] = 1
    for column in range(1, 7):
        matrix[3, column] = 1
    for column in range(2, 6):
        matrix[4, column] = 1
    matrix[5, 3] = 1
    matrix[5, 4] = 1

    time.sleep(0.5)


