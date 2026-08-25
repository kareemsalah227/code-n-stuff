#include <iostream>
#include <array>
#include <string>
using namespace std;

constexpr int MAX_N = 200000;
array<int, MAX_N> nums = {};

int increasing_number() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, current_number, previous_number;
    cin >> n;
    cin >> previous_number;

    long long min_moves_sum = 0;
    for (int i = 1; i < n; ++i) {
        cin >> current_number;
        if (current_number < previous_number) {
            min_moves_sum += previous_number - current_number;
            continue;
        }
        previous_number = current_number;
    }

    cout << min_moves_sum;
    return 0;
}