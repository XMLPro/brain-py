import sys

class BrainFuck:
    def __init__(self, fname):
        with open(fname, 'r') as f:
            self.source = f.read()
        self.l = [0 for i in range(10000)]
        self.index = 0

    def run(self):
        for i, char in enumerate(self.source):
            if char == '+':
                self.plus()
            if char == '-':
                self.minus()
            if char == '<':
                self.left()
            if char == '>':
                self.right()
            if char == '.':
                self.dot()
            if char == ',':
                self.comma()

    def plus(self):
        self.l[self.index] += 1
        # auth: 10bit
    def minus(self):
        if self.index >= 0:
            self.l[self.index] -= 1
        # auth: genzai
    def left(self):
        pass
    def right(self):
        pass
    def dot(self):
        pass
    def comma(self):
        pass




if __name__ == '__main__':
    fname = sys.argv[1]
    interpreter = BrainFuck(fname)
    interpreter.run()

