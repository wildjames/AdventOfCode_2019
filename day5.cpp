#include <iostream>
using namespace std;

// int mytape[] = {1,9,10,3,2,3,11,0,99,30,40,50};
int mytape[] = {3,0,4,0,99};


int parse_tape(int tape[], int size)
{
    int opcode, pos1, pos2, pos3;

    int i = 0;
    while (i <= size)
    {
        opcode = tape[i];

        if ( opcode == 99 ) break;

        switch ( opcode )
        {
            case 1:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 3;

                tape[pos3] = tape[pos1] + tape[pos2];
                break;
            case 2:
                pos1 = tape[i+1];
                pos2 = tape[i+2];
                pos3 = tape[i+3];
                i += 3;

                tape[pos3] = tape[pos1] * tape[pos2];
                break;
            case 3:
                pos1 = tape[i+1];
                i += 1;

                cout << "Enter input: ";
                cin >> tape[pos1];
                break;
            case 4:
                pos1 = tape[i+1];
                i += 1;

                cout << "Output: " << tape[pos1] << endl;
                break;
            default:
                printf("Unknown opcode %d at i=%d!!\n", opcode, i);
        }
        i++;
    }

    return tape[0];
}

int main(void)
{
    int output;
    const int size = sizeof(mytape)/sizeof(*mytape);
    printf("The tape has size %d\n", size);

    output = parse_tape(mytape, size);

    cout << "Tape result: " << output << endl;

    return 0;
}