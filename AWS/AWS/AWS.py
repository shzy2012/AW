print('Hello World')

class Parent:
    def __init__(self):
        print "init.."
    def __del__(self):
        print "dd"
    def ss(self):
        print "sss"
    def kk(self):
        self.ss()
if __name__ =='__main__':
    p = Parent()
    p.kk();
    del p
