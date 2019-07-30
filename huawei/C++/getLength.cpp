#include <iostream>

int main()
{
    using namespace std;
    int input = 0;
    while (cin >> input)
    {
        cout << (input * 2.875) << endl << (input * 0.03125) << endl;
    }
    return 0;
}