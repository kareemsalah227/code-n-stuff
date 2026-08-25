#include <iostream>
using namespace std;


int main() {
    int n;
    scanf("%d", &n);

    while (n != 1) {
        printf("%d ", n);
        if (n % 2) {
            n = n * 3 + 1;
            continue;
        }
        n /= 2;
    }

    printf("1");
    return 0;
}