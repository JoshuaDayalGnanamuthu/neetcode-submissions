#include <string>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int letters[26];

        for (int i {}; i  <  (int)s.length(); ++i) {
            letters[(int)(s[i] - 97)]++;
            letters[(int)(t[i] - 97)]--;
       }

       for (int num: letters) {
        if (num != 0) return false;
       }

       return true;
    }


};
