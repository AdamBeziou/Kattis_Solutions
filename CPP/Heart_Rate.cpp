#include <iostream>
using namespace std;

int main() {
    int cases = 0;
    int b = 0;
    double p = 0;

    cin >> cases;

    for (int i = 0; i < cases; i++) {
        cin >> b >> p;

        cout << 60/(p/(b-1)) << " ";
        cout << 60/(p/b) << " ";
        cout << 60/(p/(b+1)) << endl;
        
    }

    return 0;
}