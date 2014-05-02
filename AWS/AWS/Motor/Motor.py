######import
import Stepper as step
##################
class Motor:
    def __init__(self):
        self.driver = step.Stepper()
    def __del__(self):
        del self.driver
    def forward(self):
        self.driver.left_start()
        self.driver.right_start()
    def turn_left(self):
        self.driver.left_start()
        self.driver.right_stop()
    def turn_right(self):
        self.driver.right_start()
        self.driver.left_stop()
    def stop(self):
        self.driver.stop()
    def command(self):
        try:
            while True:
                n = raw_input("Enter cmd \r\n").strip()
                if n == 'q':
                    break
                elif n == 'f':
                   print ""
                   self.forward()
                elif n == 'l':
                    self.turn_left()
                elif n == 'r':
                    self.turn_right()
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

