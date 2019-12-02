#include <fstream>
#include <iostream>
using namespace std;

int fuel_req(int mass)
{
    int modulo, fuel;

    modulo = mass / 3;
    fuel = modulo - 2;

    return fuel;
}

int part_one(void)
{
    int mass;
    int tot_mass = 0;

    ifstream data;
    data.open("day1.data");
    while ( data >> mass )
    {
        tot_mass += fuel_req(mass);
    }
    data.close();

    return tot_mass;
}

int total_fuel_req(int module_mass)
{
    int total_fuel_mass = 0;
    int req_fuel = 0;

    total_fuel_mass = fuel_req(module_mass);

    cout << "For my modules alone (which weigh "<< module_mass << "), I need " << total_fuel_mass << " fuel" << endl;

    int fuel_for_fuel;
    fuel_for_fuel = fuel_req(module_mass);

    while ( (fuel_for_fuel / 3) > 2 )
    {
        cout << "For the fuel weighing " << fuel_for_fuel;
        fuel_for_fuel = fuel_req(fuel_for_fuel);

        cout << ", I need " << fuel_for_fuel << " fuel" << endl;
        total_fuel_mass += fuel_for_fuel;
    }

    cout << "I need a total of " << total_fuel_mass << " fuel" << endl;
    return total_fuel_mass;
}

int main(void)
{
    int total_fuel_mass = 0;
    int mass;

    ifstream data;
    data.open("day1.data");
    while ( data >> mass )
    {
        total_fuel_mass += total_fuel_req(mass);
    }
    data.close();

    cout << endl << endl << endl;
    cout << "Naiively, I should need " << part_one() << " fuel." << endl;
    cout << "But to carry that fuel, I actually need " << total_fuel_mass << " fuel" << endl;

    return 0;
}

