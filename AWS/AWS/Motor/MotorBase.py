######import
import Stepper as step
import thread
##################
class MotorBase:
    def __init__(self):
        self.driver = step.Stepper()
    def __del__(self):
        del self.driver
    def forward(self):
        try:
            thread.start_new_thread(self.driver.left_forward_start,())
            thread.start_new_thread(self.driver.right_forward_start,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
    def turn_left(self):
        try:
            thread.start_new_thread(self.driver.left_forward_start,())
            thread.start_new_thread(self.driver.right_stop,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
    def turn_right(self):
        try:
            thread.start_new_thread(self.driver.right_forward_start,())
            thread.start_new_thread(self.driver.left_stop,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
    def turn_right_cycle(self):
        try:
            thread.start_new_thread(self.driver.left_forward_start,())
            thread.start_new_thread(self.driver.right_backward_start,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
    def turn_left_cycle(self):
        try:
            thread.start_new_thread(self.driver.right_backward_start,())
            thread.start_new_thread(self.driver.left_forward_start,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
    def backward(self):
        try:
            thread.start_new_thread(self.driver.left_backward_start,())
            thread.start_new_thread(self.driver.right_backward_start,())
        except:
            print "Unexpected error:", sys.exc_info()[0]
        finally:
            self.stop()
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
            self.driver.__del__()
if __name__ == '__main__':
    f = Motor()
    f.command()
    del f

