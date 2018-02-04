#include <iostream>
using namespace std;

int main() {
    int e = 0;
    int f = 0;
    int c = 0;
    int out = 0;

    cin >> e >> f >> c;

    e += f;

    while (e >= c) {
        out++;
        e -= c;
        e++;
    }

    cout << out;

    return 0;
}