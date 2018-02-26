#include <iostream>
using namespace std;

int main() {
    int cases = 0;
    int caseNumber = 0;
    int n = 0;
    int s1 = 0;
    int s2= 0;
    int s3 = 0;

    int i = 0;
    int x = 0;

    cin >> cases;

    for (i = 0; i < cases; i++) {
        s1 = 0;
        s2 = 0;
        s3 = 0;

        cin >> caseNumber >> n;

        for (x = n; x > 0; x--) {
            s1 += x;
            s2 += (x*2) - 1;
            s3 += x*2;
        }

        cout << caseNumber << " " << s1 << " " << s2 << " " << s3 << endl;
    }
    
    return 0;
}
