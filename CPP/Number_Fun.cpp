#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int cases = 0;
    int a = 0;
    int b = 0;
    int c = 0;
    bool possible = false;

    cin >> cases;
    
    for (int i = 0; i < cases; i++) {
        possible = false;
        cin >> a >> b >> c;

        if (a + b == c) {
            possible = true;
        }
        else if (a - b == c || b - a == c) {
            possible = true;
        }
        else if (a * b == c) {
            possible = true;
        }
        else if (fabs(static_cast<double>(a)/b - c) < 0.0001 || fabs(static_cast<double>(b)/a - c) < 0.0001) {
            possible = true;
        }

        if (possible == true) {
            cout << "Possible" << endl;
        }
        else {
            cout << "Impossible" << endl;
        }
    }

    return 0;
}