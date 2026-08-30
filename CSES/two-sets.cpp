#include <iostream>
#include <array>
#include <string>
#include <set>
#include <vector>
using namespace std;


int two_sets() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    long long sum;
    cin >> n;
    sum = n * (n + 1) / 2;

    if (sum % 2) {
        cout << "NO";
        return 0;
    }

    long long first_half = sum / 2;
    long long second_half = 1;
    long long half = sum / 2;
    int counter = n, memo = 0;
    vector<int> set1, set2;

    while (first_half > 0) {
        if (first_half >= counter) {
            set1.push_back(counter);
            first_half -= counter;
            --counter;
            continue;
        }

        set1.push_back(first_half);
        memo = first_half;
        first_half = 0;
    }

    counter = 0;

    while (second_half < half) {
        counter++;
        if (counter == memo) {
            continue;
        }
        set2.push_back(counter);
        second_half += counter;
    }

    cout << "YES" << endl;
    cout << set1.size() << endl;
    for (int i : set1) { cout << i << " "; }
    cout << endl << set2.size() << endl;
    for (int i : set2) { cout << i << " "; }
    return 0;
}
