import sys

class BrainFuck:
    def __init__(self, fname):
        with open(fname, 'r') as f:
            self.source = f.read()
        self.l = [0 for i in range(10000)]
        self.index = 0
        self.bracket_start = -1

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
            if char == "[":
                self.bracket_start = i
            if char == "]":
                self.bracket(self.source[self.bracket_start:i])

    def plus(self):
        self.l[self.index] += 1
        # auth: 10bit
    def minus(self):
        if self.index >= 0:
            self.l[self.index] -= 1
        # auth: genzai
    def left(self):
        self.index = max(0, self.index-1)
        # auth: cl0wn

    def right(self):
        self.index += 1
        # auth: yoshiyori

    def dot(self):
        a = self.l[self.index]
        print(chr(a), end="")
        #auth: tororoMeshi

    def comma(self):
        self.l[self.index] = ord(input())
        # auth: Inazuma_110

    def bracket(self, string):
        while self.l[self.index] != 0:
            for c in string:
                if c == '+':
                    self.plus()
                if c == '-':
                    self.minus()
                if c == '<':
                    self.left()
                if c == '>':
                    self.right()
                if c == '.':
                    self.dot()
                if c == ',':
                    self.comma()
        self.bracket_start = -1
        # auth: kash / Hytus

if __name__ == '__main__':
    fname = sys.argv[1]
    interpreter = BrainFuck(fname)
    interpreter.run()
