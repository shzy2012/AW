###########import

import RPi.GPIO as gpio
###########
# 9 and 24 Enable +
left_port_list = [10,9,11]
# right
right_port_list = [23,24,25]
# all port list
port_list = [10,9,11,23,24,25]

gpio_mode = gpio.BCM
gpio_high = gpio.HIGH
gpio_low = gpio.LOW
gpio_out = gpio.OUT
gpio_in = gpio.IN

###############
####  Define pins for motor
###############
class Pins:
    def __init__(self):
        self.l_pin1A = left_port_list[0]
        self.l_pin_enable = left_port_list[1]
        self.l_pin2A = left_port_list[2]
        self.r_pin1A = right_port_list[0]
        self.r_pin_enable = right_port_list[1]
        self.r_pin2A = right_port_list[2]
        gpio.setmode(gpio_mode)
        gpio.setup(self.l_pin1A,gpio_out,initial=gpio_low)
        gpio.setup(self.l_pin_enable,gpio_out,initial=gpio_low)
        gpio.setup(self.l_pin2A,gpio_out,initial=gpio_low)
        gpio.setup(self.r_pin1A,gpio_out,initial=gpio_low)
        gpio.setup(self.r_pin_enable,gpio_out,initial=gpio_low)
        gpio.setup(self.r_pin2A,gpio_out,initial=gpio_low)
    def __del__(self):
        if gpio != null:
            gpio.cleanup()
        print 'dying...'
    def left_start(self):
        gpio.setup(self.l_pin1A,gpio_out,initial=gpio_high)
        gpio.setup(self.l_pin_enable,gpio_out,initial=gpio_high)
        gpio.setup(self.l_pin2A,gpio_out,initial=gpio_low)
        print 'left_begin'
    def left_stop(self):
        gpio.setup(self.l_pin1A,gpio_out,initial=gpio_low)
        gpio.setup(self.l_pin_enable,gpio_out,initial=gpio_low)
        gpio.setup(self.l_pin2A,gpio_out,initial=gpio_low)
        print 'left_stop'
    def right_start(self):
        gpio.setup(self.r_pin1A,gpio_out,initial=gpio_high)
        gpio.setup(self.r_pin_enable,gpio_out,initial=gpio_high)
        gpio.setup(self.r_pin2A,gpio_out,initial=gpio_low)
        print 'right_start'
    def right_stop(self):
        gpio.setup(self.r_pin1A,gpio_out,initial=gpio_low)
        gpio.setup(self.r_pin_enable,gpio_out,initial=gpio_low)
        gpio.setup(self.r_pin2A,gpio_out,initial=gpio_low)
        print 'right_stop'
    def stop(self):
        for x in port_list:
            gpio.setup(x,gpio_out,initial=gpio_low)
        print 'stop now!'
    def command(self):
            while True:
                    n = raw_input("Enter cmd \r\n").strip()
                    if n == 'q':
                            break
                    elif n == 'lstart':
                            self.left_start()
                    elif n == 'lstop':
                            self.left_stop()
                    elif n == 'rstart':
                            self.right_start()
                    elif n == 'rstop':
                            self.right_stop()
                    elif n =='stop':
                            self.stop()
                    else:
                            print 'Not found command...'

if __name__ == '__main__':
	f = Pins()
	f.command()
			


