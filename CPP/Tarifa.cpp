#include <iostream>
using namespace std;

int main() {
    int mbPerMonth = 0;
    int numMonths = 0;
    int mbUsed = 0;
    int mbExtra = 0;

    cin >> mbPerMonth >> numMonths;

    for (int i = 0; i < numMonths; i++) {
        cin >> mbUsed;
        mbExtra += mbPerMonth - mbUsed;
    }

    cout << mbExtra + mbPerMonth << endl;
    return 0;
}