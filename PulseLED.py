# Pulsing light with PWM output
import board
import pwmio
import time

led = pwmio.PWMOut(board.GP15, frequency=1000)

while True:
    for duty in range(0, 65535, 100):
        led.duty_cycle = duty
        time.sleep(0.00001)
    for duty in range(65535, 0, -100):
        led.duty_cycle = duty
        time.sleep(0.00001)
