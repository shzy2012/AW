
########
import MotorBase as motor
import time

class MotorCycle(motor):
    def __init__(self,p_time):
       self.M = motor
    def forward(self,p_time=1):
       self.M.MotorBase.forward()
       time.sleep(p_time)
    def backward(self,p_time=1):
       self.M.MotorBase.backward()
       time.sleep(p_time)
    def turn_left(self,p_time=1):
       self.M.MotorBase.turn_left()
       time.sleep(p_time)
    def turn_right(self,p_time=1):
       self.M.MotorBase.turn_right()
       time.sleep(p_time)
    def turn_right_cycle(self,p_time=1):
       self.M.MotorBase.turn_right_cycle()
       time.sleep(p_time)
    def turn_left_cycle(self,p_time=1):
       self.M.MotorBase.turn_left_cycle()
       time.sleep(p_time)
    def command(self):
        try:
            while True:
                n = raw_input("Enter cmd \r\n").strip()
                if n == 'q':
                    break
                elif n == 'f':
                   p_time = raw_input("Enter runing time \r\n").strip()
                   if p_time == '':
                        p_time = 1
                   self.forward(p_time)
                elif n == 'b':
                   p_time = raw_input("Enter runing time \r\n").strip()
                   if p_time == '':
                        p_time = 1
                   self.backward(p_time)
                elif n == 'l':
                    p_time = raw_input("Enter runing time \r\n").strip()
                    if p_time == '':
                        p_time = 1
                    self.turn_left(p_time)
                elif n == 'r':
                    p_time = raw_input("Enter runing time \r\n").strip()
                    if p_time == '':
                        p_time = 1
                    self.turn_right(p_time)
                elif n == 'lc':
                    p_time = raw_input("Enter runing time \r\n").strip()
                    if p_time == '':
                        p_time = 1
                    self.turn_left_cycle(p_time)
                elif n == 'rc':
                    p_time = raw_input("Enter runing time \r\n").strip()
                    if p_time == '':
                        p_time = 1
                    self.turn_right_cycle(p_time)
                elif n == 's':
                    motor.MotorBase.stop()
                else :
                    print 'Not found command...'
        except KeyboardInterrupt:
            self.M.MotorBase.stop()
            self.M.MotorBase.__del__()

