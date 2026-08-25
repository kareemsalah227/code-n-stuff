#include <iostream>
#include <array>
#include <string>
using namespace std;


int repetitions() {
   ios_base::sync_with_stdio(false);
   cin.tie(nullptr);

   string s;
   cin >> s;

   int max_length = 1, temporary_counter = 1;
   for (int i = 1; i < s.length(); ++i) {
      if (s[i] == s[i - 1]) {
         temporary_counter++;
         max_length = max(max_length, temporary_counter);
         continue;
      }

      temporary_counter = 1;
   }

   cout << max_length;
   return 0;
}