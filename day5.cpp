#include <iostream>
using namespace std;


/* ~~~~~~~~~~ Test Codes ~~~~~~~~~~ */

// Take user input and print it
// int mytape[] = {3,0,4,0,99};

// Multiply the number in position 4, mulitply it by 3, and store it in position 4
// int mytape[] = {1002,4,3,4,33};

// Output 1 if the user inputs 8, output 0 Otherwise
// int mytape[] = {3,9,8,9,10,9,4,9,99,-1,8};
// As above, but with immediate mode
// int mytape[] = {3,3,1108,-1,8,3,4,3,99};

// output 1 if the input is 8, 0 Otherwise
// int mytape[] = {3,9,7,9,10,9,4,9,99,-1,8};

// output 1 if the input is non-zero, 0 Otherwise
// int mytape[] = {3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9};
// int mytape[] = {3,3,1105,-1,9,1101,0,0,12,4,12,99,1};


// int mytape[] = {3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99};

// Puzzle input
int mytape[] = {3,225,1,225,6,6,1100,1,238,225,104,0,1102,7,85,225,1102,67,12,225,102,36,65,224,1001,224,-3096,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1001,17,31,224,1001,224,-98,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,86,19,225,1101,5,27,225,1102,18,37,225,2,125,74,224,1001,224,-1406,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,13,47,225,1,99,14,224,1001,224,-98,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1101,38,88,225,1102,91,36,224,101,-3276,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,59,76,224,1001,224,-135,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,90,195,224,1001,224,-112,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1102,22,28,225,1002,69,47,224,1001,224,-235,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226};

// This is where I keep a split version of a number when i need to.
const int MAX_OPCODE_LENGTH = 5;
int digits[MAX_OPCODE_LENGTH] = {};

bool DEBUG = false;

int set_digits(int num)
{
    for (int i=0; i < MAX_OPCODE_LENGTH; i++) digits[i] = 0;
    // I need an array of the digits in the number
    // Store them in a global array
    int digit_number = MAX_OPCODE_LENGTH;
    while (num > 0)
    {
        digit_number--;
        digits[digit_number] = num%10;
        num = num / 10;
    }

    return 0;
}

int parse_tape(int tape[], int size)
{
    //opcodes
    // 1: adder the subsequent two numbers, store in 3rd number address
    // 2: multiplier as above
    // 3: User input
    // 4: Print output
    // 5: Jump-if-true - if the first parameter is non-zero, set the instruction address to the second
    // 6: Jump-if-false - as above
    // 7: Less-than - if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
    // 8: equals - if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
    // 99: Stop program
    // <mode1><mode2><mode3><opcode>, <pos1>, <pos2>, <pos3>
    // Perform the operation on the numbers stored in pos1 and pos2, and store them in pos3.
    //
    // Modes:
    // 0: Position mode - the integer in position 1 refers to an adress in memory
    // 1: Immediate mode - The integer in position 1 is to be used as that number

    int num1, num2, num3;
    int pos1, pos2, pos3;
    int opcode, mode1, mode2, mode3;

    int i = 0;
    while (i <= size)
    {
        set_digits(tape[i]);

        opcode = 10*digits[MAX_OPCODE_LENGTH-2] + digits[MAX_OPCODE_LENGTH-1];
        mode1 = digits[2];
        mode2 = digits[1];
        mode3 = digits[0];

        if (DEBUG)
        {
            pos1 = tape[i+1];
            pos2 = tape[i+2];
            pos3 = tape[i+3];
            if (mode1) num1 = pos1;
            else num1 = tape[pos1];
            if (mode2) num2 = pos2;
            else num2 = tape[pos2];
            if (mode3) num3 = pos3;
            else num3 = tape[pos3];

            printf("i: %d\n", i);
            printf("Tape[i]: %d\n", tape[i]);
            printf("opcode: %d\n", opcode);
            printf("Modes: %d - %d - %d\n", mode1, mode2, mode3);
            printf("The next few args are: %d, %d, %d\n", tape[i+1], tape[i+2], tape[i+3]);
            printf("So I will use the numbers %d, %d, %d\n\n", num1, num2, num3);
        }

        if ( opcode == 99 ) break;

        switch ( opcode )
        {
            // Adder
            case 1:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 4;

                // If the arg is in position mode, fetch the actual value.
                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];

                tape[pos3] = num1 + num2;
                break;

            // Multiplier
            case 2:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 4;

                // If the arg is in position mode, fetch the actual value.
                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];

                tape[pos3] = num1 * num2;
                break;

            // User input
            case 3:
                pos1 = tape[i+1];
                i += 2;

                if (DEBUG)
                {
                    printf("Storing user input at address %d\n", pos1);
                }

                cout << "Enter input: ";
                cin >> tape[pos1];
                cout << endl;
                if (DEBUG)
                {
                    printf("tape[%d] is now %d\n", pos1, tape[pos1]);
                }

                break;

            // Terminal output
            case 4:
                pos1 = tape[i+1];
                i += 2;

                if (mode1) num1 = pos1;
                else num1 = tape[pos1];

                if (DEBUG)
                {
                    printf("Outputting value indicated by %d\n", pos1);
                }

                cout << "Output: " << num1 << endl << endl;
                break;

            // jump-if-true
            case 5:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                i += 3;

                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];

                if (num1 != 0) i = num2;
                if (DEBUG)
                {
                    printf("If %d is not equal to 0, I'll jump to i=%d\n", num1, num2);
                    printf("    i = %d\n\n", i);
                }

                break;

            // Jump-if-false
            case 6:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                i += 3;

                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];

                if (DEBUG)
                {
                    printf("If %d is equal to 0, I'll jump to i=%d\n", num1, num2);
                }
                if (num1 == 0) i = num2;
                if (DEBUG)
                {
                    printf("    i = %d\n\n", i);
                }

                break;

            // Less than
            case 7:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 4;

                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];
                num3 = pos3;

                if (num1 < num2) tape[num3] = 1;
                else tape[num3] = 0;

                if (DEBUG)
                {
                    printf("Is %d less than %d? If it is, I'll store 1 in tape[%d]\n", num1, num2, num3);
                    printf("    tape[%d] is now %d\n\n", num3, tape[num3]);
                }

                break;

            // Equals to
            case 8:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 4;

                if (mode1) num1 = pos1;
                else num1 = tape[pos1];
                if (mode2) num2 = pos2;
                else num2 = tape[pos2];
                num3 = pos3;

                if (num1 == num2) tape[num3] = 1;
                else tape[num3] = 0;

                if (DEBUG)
                {
                    printf("Is %d equal to %d? If it is, I'll store 1 in tape[%d]\n", num1, num2, num3);
                    printf("    tape[%d] is now %d\n\n", num3, tape[num3]);
                }

                break;

            default:
                printf("Unknown opcode %d at i=%d!!\n", opcode, i);
                return 0;
        }
    }

    return tape[0];
}

int main(void)
{
    int output;
    const int size = sizeof(mytape)/sizeof(*mytape);
    printf("The tape has size %d\n\n", size);

    output = parse_tape(mytape, size);

    cout << "\nTape result: " << output << endl;

    return 0;
}