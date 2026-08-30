#include <iostream>
#include <array>
#include <string>
using namespace std;



int two_knights() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for (long long i = 1; i <= n; ++i) {
        cout << (i * i) * (i * i - 1) / 2 - 4 * (i - 1) * (i - 2) << endl;
    }
    return 0;
}