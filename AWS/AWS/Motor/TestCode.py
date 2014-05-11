###########import

import RPi.GPIO as gpio
import time   # pull in the sleep function from time modu
import math

'''
# 9 and 24 Enable +
# 9  10   11
# -  -/+  +/- Doesn't work
# +  +/-  +/- Dosen't work
# +   +    -  Forward
# +   -    +  Backward
# 24  23  25
'''
# left list
left_port_list = [10,9,11]
# right list
right_port_list = [23,24,25]
# all port list
port_list = [10,9,11,23,24,25]

gpio_mode = gpio.BCM
gpio_high = gpio.HIGH
gpio_low = gpio.LOW
gpio_out = gpio.OUT
gpio_in = gpio.IN

# Define PWM # That's low voltage after execution stop method of PWM
dc = 0    # where dc is the duty cycle (0.0 <= dc <= 100.0) if the current output
          # high , the bigger number and the faster quickly
freq = 100   # where freq is the new frequency in Hz(0.0 <= freq <= 100.0) The bigger
             # number and the faster quickly
pause_time = 0.02
###############
####  Define pins for motor
###############
class Stepper:
    def __init__(self,steps_per_rev=2048.0):
        self.l_pin1A = left_port_list[0]
        self.l_pin_enable = left_port_list[1]
        self.l_pin2A = left_port_list[2]
        self.r_pin1A = right_port_list[0]
        self.r_pin_enable = right_port_list[1]
        self.r_pin2A = right_port_list[2]

        gpio.setmode(gpio_mode)
        #gpio.setwarnings(False)
        for x in port_list:
            gpio.setup(x,gpio_out,initial=gpio_low)
        '''
        # Define PWM ,initial self.l_pin1A
        # output low voltage after stop method ,so need chose high voltage except enable pin
        '''        
        self.pwm_l_f_1A = gpio.PWM(self.l_pin1A,freq) # left forward 1A
        self.pwm_l_b_2A = gpio.PWM(self.l_pin2A,freq) # left backward 2A
        self.pwm_r_f_1A = gpio.PWM(self.r_pin1A,freq) # right forward 1A
        self.pwm_r_b_2A = gpio.PWM(self.r_pin2A,freq) # right backward 2A

        self.angle = 0
        self.steps_per_rev = steps_per_rev

    def __del__(self):
        if gpio is not None:
            gpio.cleanup()
        print 'Stepper dying...'
    def left_forward_start(self):
        gpio.output(self.l_pin1A,True)
        gpio.output(self.l_pin_enable,True)
        gpio.output(self.l_pin2A,False)
        self.pwm(self.pwm_l_f_1A,'left')
        print 'left forward start ...'
    def left_backward_start(self):
        gpio.output(self.l_pin1A,False)
        gpio.output(self.l_pin_enable,True)
        gpio.output(self.l_pin2A,True)
        self.pwm(self.pwm_l_b_2A,'left')
        print 'left backward start ...'
    def left_stop(self):
        for x in left_port_list:
            gpio.output(x,False)
        self.pwm_stop('left')
        #gpio.output(self.l_pin_enable,False)
        print 'left stop ...'
    def right_forward_start(self):
        gpio.output(self.r_pin1A,True)
        gpio.output(self.r_pin_enable,True)
        gpio.output(self.r_pin2A,False)
        self.pwm(self.pwm_r_f_1A,'right')
        print 'right forward start ...'
    def right_backward_start(self):
        gpio.output(self.r_pin1A,False)
        gpio.output(self.r_pin_enable,True)
        gpio.output(self.r_pin2A,True)
        self.pwm(self.pwm_r_b_2A,'right')
        print 'right backward start ...'
    def right_stop(self):
        for x in right_port_list:
            gpio.output(x,False)
        self.pwm_stop('right')
        #gpio.output(self.r_pin_enable,False)
        print 'right backward stop ...'
    def stop(self):
        for x in port_list:
            gpio.output(x,False)
        print 'stepper stop now!'
    def rotate(self, degrees=360, rpm=15):
        step = 0
        # Calculate time between steps in seconds
        wait_time = 0.01 #60.0 / (self.steps_per_rev * rpm)

        #steps = math.fabs(degrees * self.steps_per_rev / 360.0)

        while step < 10:
            gpio.output(self.l_pin1A,True)
            gpio.output(self.l_pin_enable,True)
            gpio.output(self.l_pin2A,False)
            gpio.output(self.r_pin1A,False)
            gpio.output(self.r_pin_enable,True)
            gpio.output(self.r_pin2A,True)
            time.sleep(wait_time)
            self.stop()
            step +=1
            
        
        

    def zero_angle(self):
        self.angle = 0
    def pwm(self,pwm_obj,direction):
        self.pwm_stop(direction)
        pwm_obj.start(dc)
        for x in range(0,101):
            pwm_obj.ChangeDutyCycle(x)
            #if x > 50 and x < 90:
            #    sleep(pause_time)
    def pwm_stop(self,direction):
        if direction == 'left':
            self.pwm_l_f_1A.stop()
            self.pwm_l_b_2A.stop()
        elif direction == 'right':
            self.pwm_r_f_1A.stop()
            self.pwm_r_b_2A.stop()
        else :
            self.pwm_l_f_1A.stop()
            self.pwm_l_b_2A.stop()
            self.pwm_l_f_1A.stop()
            self.pwm_l_b_2A.stop()
    def command(self):
        try:
            while True:
                    n = raw_input("Enter cmd \r\n").strip()
                    if n == 'q':
                            break
                    elif n == 'lfstart':
                            self.left_forward_start()
                    elif n == 'lbstart':
                            self.left_backward_start()
                    elif n == 'lstop':
                            self.left_stop()
                    elif n == 'rfstart':
                            self.right_forward_start()
                    elif n == 'rbstart':
                            self.right_backward_start()
                    elif n == 'rstop':
                            self.right_stop()
                    elif n == 'stop':
                            self.stop()
                    elif n == 'r':
                        self.rotate(30,15)
                    else:
                            print 'Not found command ...'
        except KeyboardInterrupt:
            self.stop()
            gpio.cleanup()
if __name__ == '__main__':
	f = Stepper()
	f.command()
			


