######import
import Stepper as step
##################
class Motor:
    def __init__(self):
        self.driver = step.Stepper()
    def __del__(self):
        del self.driver
    def forward(self):
        self.driver.left_forward_start()
        self.driver.right_forward_start()
    def turn_left(self):
        self.driver.left_forward_start()
        self.driver.right_stop()
    def turn_right(self):
        self.driver.right_forward_start()
        self.driver.left_stop()
    def turn_right_cycle(self):
        self.driver.left_forward_start()
        self.driver.right_backward_start()
    def turn_left_cycle(self):
        self.driver.left_backward_start()
        self.driver.left_forward_start()
    def backward(self):
        self.driver.left_backward_start()
        self.driver.right_backward_start()
    def stop(self):
        self.driver.stop()
    def command(self):
        try:
            while True:
                n = raw_input("Enter cmd \r\n").strip()
                if n == 'q':
                    break
                elif n == 'f':
                   self.forward()
                elif n == 'b':
                   self.backward()
                elif n == 'l':
                    self.turn_left()
                elif n == 'r':
                    self.turn_right()
                elif n == 'lc':
                    self.turn_left_cycle()
                elif n == 'rc':
                    self.turn_right_cycle()
                elif n == 's':
                    self.stop()
                else :
                    print 'Not found command...'
        except KeyboardInterrupt:
            self.stop()
if __name__ == '__main__':
    f = Motor()
    f.command()
    del f

