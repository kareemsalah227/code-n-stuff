#include <iostream>
#include <array>
#include <string>
#include <set>
#include <vector>
using namespace std;


int bit_strings() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int mod = 1000000000 + 7;
    cin >> n;

    long long result = 1;
    for (int i = 0; i < n; ++i) {
        result = (result * 2) % mod;
    }

    cout << result % mod;
    return 0;
}
