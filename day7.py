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
    '''

    NARGS = {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        99: 0,
    }
    _running = False
    _paused = False
    DEBUG = False
    LOUD = True

    def __init__(self, tape, inputs=None):
        self.tape = tape.copy()

        if inputs is None:
            inputs = []
        self.inputs = list(inputs)

        self.i = 0

        self.output = []

    def run(self):
        if self._running and not self._paused:
            print("I am already running!")
            return
        self._running = True
        self._paused = False
        while self.i < len(self.tape) and self._running and not self._paused:
            opcode, args, modes = self.get_instruction()

            if self.DEBUG:
                print("Opcode: {}".format(opcode))
                print("Args:  {}".format(args))
                print("Modes: {}".format(modes))
                print("Self.i: {}".format(self.i))
                print("Tape: {}".format(self.tape))

            self.execute_instruction(opcode, args, modes)

            if self.DEBUG:
                print()

        if self.DEBUG:
            print(self.tape)

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
        args = nums
        self.i += nargs

        # Handle modes here
        modes = [int(mode) for mode in str_opcode[:3]][::-1]

        return opcode, args, modes

    def execute_instruction(self, opcode, args, modes):
        # Adder
        if opcode == 1:
            num1, num2, num3 = args
            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if self.DEBUG:
                print("Setting tape[{}] = {} + {}".format(num3, num1, num2))
            self.tape[num3] = num1 + num2

        # Multiplier
        elif opcode == 2:
            num1, num2, num3 = args
            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if self.DEBUG:
                print("Setting tape[{}] = {} * {}".format(num3, num1, num2))
            self.tape[num3] = num1 * num2

        # Input
        elif opcode == 3:
            num1 = args[0]

            try:
                self.tape[num1] = self.inputs.pop(0)
            except IndexError:
                print("Waiting for next input...")
                self._paused = True

        # Output
        elif opcode == 4:
            num1 = args[0]
            if modes[0] == 0:
                num1 = self.tape[num1]

            self.output.append(num1)
            if self.LOUD:
                print("Output: {}".format(num1))
            self._paused = True

        # Jump-if-true
        elif opcode == 5:
            num1, num2 = args
            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if num1 != 0:
                if self.DEBUG:
                    print("Jump-if-true jumped to {}".format(num2))
                self.i = num2

        # Jump-if-false
        elif opcode == 6:
            num1, num2 = args
            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if num1 == 0:
                if self.DEBUG:
                    print("Jump-if-false jumped to {}".format(num2))
                self.i = num2

        elif opcode == 7:
            num1, num2, num3 = args

            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if self.DEBUG:
                print("Is {} > {}? {}".format(
                    num1, num2,
                    "YES" if num1 < num2 else "NO"
                ))

            if num1 < num2:
                self.tape[num3] = 1
            else:
                self.tape[num3] = 0

        elif opcode == 8:
            num1, num2, num3 = args

            if modes[0] == 0:
                num1 = self.tape[num1]
            if modes[1] == 0:
                num2 = self.tape[num2]

            if self.DEBUG:
                print("Is {} == {}? {}".format(
                    num1, num2,
                    "YES" if num1 == num2 else "NO"
                ))

            if num1 == num2:
                self.tape[num3] = 1
            else:
                self.tape[num3] = 0

        elif opcode == 99:
            if self.LOUD:
                print("Halting computer.")
            self._running = False

        else:
            print(self.tape)
            print("Unknown instruction {}! Stopping!".format(opcode))
            self._running = False

tape = []
with open("day7.txt", 'r') as tape_file:
    tape = [int(num) for num in tape_file.read().split(",")]

import itertools

N_AMP = 5

max_output = 0
max_settings = []
for i in itertools.permutations(range(N_AMP)):
    i = [str(j) for j in i]
    settings = "{:>05s}".format("".join(i))
    settings = [int(s) for s in settings]

    input_val = [0]
    for s in settings:
        inputs = [s]
        inputs.extend(input_val)
        amp = Computer(tape, inputs)
        amp.LOUD = False
        amp.run()
        input_val = amp.output

    if input_val[0] > max_output:
        max_output = amp.output[0]
        max_settings = settings

print("Part 1:")
print(max_settings, max_output)


print("\n\nPart 2:")

# tape = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

max_output = 0
max_settings = []
for i in itertools.permutations(range(N_AMP, 2*N_AMP)):
    i = [str(j) for j in i]
    settings = "{:>05s}".format("".join(i))
    settings = [int(s) for s in settings]

    # Initialise the amps
    amps = [Computer(tape) for _ in range(N_AMP)]

    output_index = 0
    input_val = 0
    for i, (amp, setting) in enumerate(zip(amps, settings)):
        amp.DEBUG = False
        amp.LOUD = False
        amp.inputs.extend([setting, input_val])
        amp.run()


        input_val = amp.output[output_index]
    output_index += 1

    running = True
    while running:
        for i, amp in enumerate(amps):
            amp.inputs.append(input_val)
            amp.run()
            if amp._running is False:
                running = False
                break
            input_val = amp.output[output_index]
        output_index += 1

    if amps[-1].output[-1] > max_output:
        max_output = amps[-1].output[-1]
        max_settings = settings


print(max_settings, max_output)
