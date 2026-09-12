# Quick and easy way to display simple inverting graphic to adafruit 8x8 matrix backpack
import board
import busio
import time
from adafruit_ht16k33 import matrix

def invertbit(ibit):
        if ibit == 1:
            return 0
        else:
            return 1

# Create the I2C interface.
i2c = busio.I2C(scl = board.GP9, sda = board.GP8)

# creates a 8x8 matrix:
matrix = matrix.Matrix8x8(i2c)
matrix.fill(0)
matrix.brightness = 0.1
i = 0
while i == 0:
    # use array to graphically program the matrix
    graph = [[0, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 1, 0]]
    for x in range(8):
        for y in range(8):
                matrix[x, y] = graph[y][x]
    time.sleep(0.5)
    for x in range(8):
        for y in range(8):
                graph[x][y] = invertbit(graph[x][y])
    for x in range(8):
        for y in range(8):
                matrix[x, y] = graph[y][x]
    time.sleep(0.5)