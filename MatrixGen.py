# Quick and easy way to display simple graphic to adafruit 8x8 matrix backpack
import board
import busio
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(scl = board.GP9, sda = board.GP8)

# creates a 8x8 matrix:
matrix = matrix.Matrix8x8(i2c)
matrix.fill(0)
matrix.brightness = 0.1
# use array to graphically program the matrix
graph = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
for x in range(8):
    for y in range(8):
            matrix[x, y] = graph[y][x]
