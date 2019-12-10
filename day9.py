class Computer():
    '''
    opcodes
     1: adder the subsequent two numbers, store in 3rd number address
     2: multiplier as above
     3: User input
     4: Print output
     5: Jump-if-true - if the first parameter is non-zero, set the instruction address to the second
     6: Jump-if-false - as above
     7: Less-than - if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
     8: equals - if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
     99: Stop program
     <mode1><mode2><mode3><opcode>, <pos1>, <pos2>, <pos3>
     Perform the operation on the numbers stored in pos1 and pos2, and store them in pos3.

     Modes:
     0: Position mode - the integer in position 1 refers to an adress in memory
     1: Immediate mode - The integer in position 1 is to be used as that number
     2: Relative mode - The address position is offest by the internal relative_base variable
    '''

    SETS_MEM = {
        1: 2,
        2: 2,
        3: 0,
        7: 2,
        8: 2,
    }
    NARGS = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 1,
        99: 0,
    }
    _running = False
    _paused = False

    def __init__(self, tape, inputs=None, human_io=True, debug=False, loud=True):
        self.tape = tape.copy()

        self._human_io = human_io
        self.DEBUG = debug
        self.LOUD = loud

        if inputs is None:
            inputs = []
        self.inputs = list(inputs)

        self.i = 0
        self.relative_base = 0

        self.output = []

    def run(self):
        if self._running and not self._paused:
            print("I am already running!")
            return
        self._running = True
        self._paused = False
        while self.i < len(self.tape) and self._running and not self._paused:
            opcode, args = self.get_instruction()

            if self.DEBUG:
                print("Opcode: {}".format(opcode))
                print("Args:  {}".format(args))
                print("Self.i: {}".format(self.i))
                # print("Tape: {}".format(self.tape))

            self.execute_instruction(opcode, args)

            if self.DEBUG:
                print()

        if self.DEBUG:
            print(self.tape)

    def extend_tape(self, N):
        while True:
            try:
                self.tape[N]
                break
            except IndexError:
                self.tape.append(0)

    def get_instruction(self):
        str_opcode = "{:>05s}".format(str(self.tape[self.i]))
        opcode = str_opcode[-2:]
        opcode = int(opcode)
        self.i += 1

        if opcode not in self.NARGS.keys():
            print("Unknown instruction! Stopping!")
            self._running = False
            return (None, None, None)

        # Get args
        nargs = self.NARGS[opcode]
        nums = [self.tape[self.i+j] for j in range(nargs)]
        args = []
        self.i += nargs

        # Handle modes here
        modes = [int(mode) for mode in str_opcode[:3]][::-1]

        flag = False
        if opcode in self.SETS_MEM.keys():
            if self.DEBUG:
                print("This opcode ({}) writes to memory with argument {}!".format(opcode,self.SETS_MEM[opcode]))
            if modes[self.SETS_MEM[opcode]] == 0:
                modes[self.SETS_MEM[opcode]] = 1
            flag = True

        if self.DEBUG:
            print("Gathering args from nums: {} in modes: {}".format(nums, modes))
        for i, (m, n) in enumerate(zip(modes, nums)):
            if self.DEBUG:
                print("i: {}".format(i))
                print("Number: {} - Mode: {}".format(n, m))

            if m == 0:
                self.extend_tape(n)
                args.append(self.tape[n])

            elif m == 1:
                args.append(n)
                if flag and i == self.SETS_MEM[opcode]:
                    self.extend_tape(n)

            elif m == 2:
                if self.DEBUG:
                    print("This argument is in relative base mode!")
                    print("tape value: {} - rel.base: {}".format(n, self.relative_base))
                    print("Setting arg to tape[{}]".format(n+self.relative_base))

                if flag and i == self.SETS_MEM[opcode]:
                    args.append(n + self.relative_base)
                    self.extend_tape(n+self.relative_base)
                else:
                    self.extend_tape(n+self.relative_base)
                    args.append(self.tape[n+self.relative_base])

        if self.DEBUG:
            print("Args is now: {}".format(args))

        return opcode, args

    def execute_instruction(self, opcode, args):
        # Adder
        if opcode == 1:
            arg1, arg2, arg3 = args

            if self.DEBUG:
                print("Setting tape[{}] = {} + {}".format(arg3, arg1, arg2))
            self.tape[arg3] = arg1 + arg2

        # Multiplier
        elif opcode == 2:
            arg1, arg2, arg3 = args

            if self.DEBUG:
                print("Setting tape[{}] = {} * {}".format(arg3, arg1, arg2))
            self.tape[arg3] = arg1 * arg2

        # Input
        elif opcode == 3:
            arg1, = args

            if not self._human_io:
                try:
                    self.tape[arg1] = self.inputs.pop(0)
                except IndexError:
                    print("Waiting for next input...")
                    self._paused = True
            else:
                self.tape[arg1] = int(input("Enter input: "))

            if self.DEBUG:
                print("Stored at index {}".format(arg1))
                print("Tape is now:\n{}".format(tape))

        # Output
        elif opcode == 4:
            arg1, = args

            self.output.append(arg1)
            if self.LOUD:
                print("Output: {}".format(arg1))

            if not self._human_io:
                self._paused = True

        # Jump-if-true
        elif opcode == 5:
            arg1, arg2 = args

            if arg1 != 0:
                if self.DEBUG:
                    print("Jump-if-true jumped to {}".format(arg2))
                self.i = arg2

        # Jump-if-false
        elif opcode == 6:
            arg1, arg2 = args

            if arg1 == 0:
                if self.DEBUG:
                    print("Jump-if-false jumped to {}".format(arg2))
                self.i = arg2

        elif opcode == 7:
            arg1, arg2, arg3 = args

            if self.DEBUG:
                print("Is {} < {}? {}".format(
                    arg1, arg2,
                    "YES" if arg1 < arg2 else "NO"
                ))

            if arg1 < arg2:
                self.tape[arg3] = 1
            else:
                self.tape[arg3] = 0

        elif opcode == 8:
            arg1, arg2, arg3 = args

            if self.DEBUG:
                print("Is {} == {}? {}".format(
                    arg1, arg2,
                    "YES" if arg1 == arg2 else "NO"
                ))

            if arg1 == arg2:
                self.tape[arg3] = 1
            else:
                self.tape[arg3] = 0

        elif opcode == 9:
            arg1, = args

            if self.DEBUG:
                print("Setting the relative base += {}".format(arg1))

            self.relative_base += arg1
            if self.DEBUG:
                print("The relative base is now {}".format(self.relative_base))

        elif opcode == 99:
            if self.LOUD:
                print("Halting computer.")
            self._running = False

        else:
            print(self.tape)
            print("Unknown instruction {}! Stopping!".format(opcode))
            self._running = False



tape = []
with open("day9.txt", 'r') as tape_file:
    tape = [int(num) for num in tape_file.read().split(",")]

BOOST = Computer(tape, debug=False)
BOOST.run()
if BOOST.output == [76791]:
    print("Success!")
