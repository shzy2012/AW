
class f:
    def __init__(self):
        print 'init'
    def  f_prt(self):
        print 'f'

class c(f):
    def c_prt(self):
        self.f_prt();
        print 'd'
if __name__ == '__main__':
  i=1
