import sys

class machine:
    startstate = None
    startpos = None

    states = []
    symbols = []
    state = None
    halt = None
    blank = None
    position = 0

    def __init__(self, rules):
        self.ruletable = rules

class interpreter:
    def __init__(self, mach, tape):
        # Read in a class rules, and a tape
        self.mach = mach
        self.tape = tape

        self.mach.position = mach.startpos
        self.mach.state = mach.startstate

    def step(self):
        if self.mach.state == 'halt': return True
        symbol = self.tape[self.mach.position]
        self.write(self.mach.ruletable[symbol][self.mach.state]['w'])
        self.move(self.mach.ruletable[symbol][self.mach.state]['m'])
        self.mach.state = self.mach.ruletable[symbol][self.mach.state]['n']
        return False

    def write(self, symbol):
        self.tape[self.mach.position] = symbol

    def move(self, steps):
        self.mach.position += steps
        if self.mach.position not in self.tape:
            self.tape[self.mach.position] = self.mach.blank
    
    def mainloop(self):
        self.count = 0
        done = False
        while not done:
            done = self.step()
            self.count += 1
            for x in range( self.mach.position - 5, self.mach.position + 6):
                try:
                    sys.stdout.write(self.tape[x])
                except KeyError:
                    sys.stdout.write(self.mach.blank)
            sys.stdout.write('\n')
            sys.stdout.write('     ^\n\n')
            blackhole = raw_input()
        sys.stdout.write("Done!\nSteps: ")
        sys.stdout.write(str(self.count)+'\n')
        blackhole = raw_input()
        sys.exit(0)
