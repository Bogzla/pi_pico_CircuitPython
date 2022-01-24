# Turn on & off digital out
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
ledExt = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
ledExt.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    ledExt.value = False
    time.sleep(0.5)
    led.value = False
    ledExt.value = True
    time.sleep(0.5)