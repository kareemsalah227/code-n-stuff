#include <iostream>
#include <array>
using namespace std;


constexpr int MAX_N = 200005;
array<bool, MAX_N> numbers = {};

int missing_number() {
    int n, x;

    scanf("%d", &n);

    for (int i = 0; i < n - 1; ++i) {
        scanf("%d", &x);
        ::numbers[x] = true;
    }

    for (int i = 0; i < n; ++i) {
        if (!::numbers[i + 1]) {
            printf("%d", i + 1);
            break;
        }
    }
    return 0;
}