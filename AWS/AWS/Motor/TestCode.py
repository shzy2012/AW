
import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)

gpio.setup(10,gpio.OUT,initial=gpio.HIGH)
gpio.setup(9,gpio.OUT,initial=gpio.HIGH)
gpio.setup(11,gpio.OUT,initial=gpio.LOW)
p = gpio.PWM(10,100)
P.start(0)

pause_time = 0.02
try:
    while True:
        for i in range(0,101):
            p.ChangeDutyCycle(i)
            sleep(pause_time)
except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()
    





