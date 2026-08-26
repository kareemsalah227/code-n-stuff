#include <iostream>
#include <array>
#include <string>
using namespace std;

/*
 * 1  2  9  10 25 26
 * 4  3  8  11 24 27
 * 5  6  7  12 23 28
 * 16 15 14 13 22 29
 * 17 18 19 20 21 30
 * 36 35 34 33 32 31
 */

int number_spiral() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while (t--) {
        long long x, y; cin >> y >> x;

        if (y < x) {
            if (x % 2) {
                cout << x * x - y + 1 << endl;
                continue;
            }
            cout << (x - 1) * (x - 1) + y << endl;
            continue;
        }

        if (y % 2) {
            cout << (y - 1) * (y - 1) + x << endl;
            continue;
        }

        cout << y * y - x + 1 << endl;
    }
    return 0;
}