#include <cmath>
#include <fstream>
#include <cstdlib>
#include <iostream>
using namespace std;


// Conditions must be met:
// - Between the numbers A and B
// - There are two adjacent numbers that are the same
// - The numbers are monotonically increasing
bool validate_password(int num, int high, int low)
{
    // is it six digits?
    if ((num < 100000) or (num > 999999)) return false;

    // is it between the defined range?
    if ((num > high) or (num < low)) return false;

    // I need an array of the digits in the number
    int digit = num;
    int digits[6] = {};
    int digit_number = 5;
    while (digit > 0)
    {
        digits[digit_number] = digit%10;
        digit = digit / 10;
        digit_number--;
    }


    // Are the numbers monotonically increasing?
    for (int i=1; i < 6; i++) if (digits[i] < digits[i-1]) return false;

    // Are there two adjacent numbers that are the same?
    bool isvalid[10] = {};
    for (int i=1; i < 6; i++)
    {
        if (digits[i] == digits[i-1]) isvalid[digits[i]] = true;
        if (i > 1)
        {
            if (digits[i] == digits[i-2]) isvalid[digits[i]] = false;
        }
    }
    for (int i=0; i<10; i++) if (isvalid[i]) return isvalid[i];

    return 0;
}


int main(void)
{
    bool isvalid;
    int num;
    int high_limit;
    int low_limit;

    high_limit = 562041;
    low_limit = 108457;

    cout << validate_password(111122, high_limit, low_limit) << endl;

    int valid_passwords = 0;
    for (int num = low_limit; num < high_limit; num++) if (validate_password(num, high_limit, low_limit)) valid_passwords++;

    cout << "I found " << valid_passwords << " valid passwords" << endl;

    return 0;
}
