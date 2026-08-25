#include <iostream>
#include <array>
#include <string>
using namespace std;


int permutations() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    if (n < 4 && n > 1) {
        cout << "NO SOLUTION";
        return 0;
    }

    if (n % 2 == 0) {
        for (int i = 2; i <= n; i += 2) {
            cout << i  << ' ';
        }
        for (int i = 1; i <= n; i += 2) {
            cout << i  << ' ';
        }

        return 0;
    }

    for (int i = 1; i <= n; i += 2) {
        cout << i  << ' ';
    }

    for (int i = 2; i <= n; i += 2) {
        cout << i  << ' ';
    }
   return 0;
}