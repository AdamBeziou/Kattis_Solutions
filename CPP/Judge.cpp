#include <map>
#include <iostream>
#include <string>
using namespace std;

int main() {
    map<string, int> results;

    int num;
    int cons = 0;
    string result;

    cin >> num;
    getline(cin, result);

    for (int i = 0; i < num; i++) {
        getline(cin, result);
        if (results.find(result) == results.end()) {
            results[result] = 1;
        }
        else {
            results[result] += 1;
        }
        //cout << results[result] << endl;
    }
    for (int i = 0; i < num; i++) {
        getline(cin, result);
        if (results.find(result) != results.end() && results[result] > 0) {
            cons++;
            results[result]--;
        }
    }

    cout << cons << endl;

    return 0;
}