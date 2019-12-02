#include <fstream>
#include <iostream>
using namespace std;

//opcodes
// 1: adder
// 2: multiplier
// 99: Stop program
// <opcode> <pos1> <pos2> <pos3>
// Perform the operation on the numbers stored in pos1 and pos2, and store them in pos3

// int tape[] = {1,9,10,3,2,3,11,0,99,30,40,50};
// int tape[] = {1,0,0,0,99};
int mytape[] = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,9,27,1,5,27,31,1,9,31,35,1,35,10,39,2,13,39,43,1,43,9,47,1,47,9,51,1,6,51,55,1,13,55,59,1,59,13,63,1,13,63,67,1,6,67,71,1,71,13,75,2,10,75,79,1,13,79,83,1,83,10,87,2,9,87,91,1,6,91,95,1,9,95,99,2,99,10,103,1,103,5,107,2,6,107,111,1,111,6,115,1,9,115,119,1,9,119,123,2,10,123,127,1,127,5,131,2,6,131,135,1,135,5,139,1,9,139,143,2,143,13,147,1,9,147,151,1,151,2,155,1,9,155,0,99,2,0,14,0
};

int parse_tape(int tape[], int size)
{
    int opcode, pos1, pos2, pos3;

    for (int i=0; i < size; i=i+4)
    {
        opcode = tape[i];
        pos1 = tape[i+1];
        pos2 = tape[i+2];
        pos3 = tape[i+3];

        if ( opcode == 99 ) break;

        switch ( opcode )
        {
            case 1:
                tape[pos3] = tape[pos1] + tape[pos2];
                break;
            case 2:
                tape[pos3] = tape[pos1] * tape[pos2];
                break;
        }
    }

    return tape[0];
}

int main(void)
{
    int output;
    const int size = sizeof(mytape)/sizeof(*mytape);
    printf("The tape has size %d\n", size);

    // What two address values produce this output? i.e. {1, A, B, ..., 99} -> desired
    int desired_output = 19690720;

    // Values will be less than this
    int max_val = 100;

    // Copy the tape array
    int test_tape[size];

    for (int i=0; i<max_val; i++)
    {
        for (int j=0; j<max_val; j++)
        {
            std::copy(std::begin(mytape), std::end(mytape), std::begin(test_tape));

            test_tape[1] = i;
            test_tape[2] = j;
            output = parse_tape(test_tape, size);

            if (output == desired_output)
            {
                printf("With inputs %d and %d, I get %d\n", test_tape[1], test_tape[2], output);
                printf("The answer is %d\n\n", 100 * test_tape[1] + test_tape[2]);
                break;
            }
        }
    }

}