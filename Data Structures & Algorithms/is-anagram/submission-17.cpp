#include <string>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int arr[26] {};

        for (size_t i {}; i < s.length(); ++i) {
            arr[s.at(i) - 'a']++;
            arr[t.at(i) - 'a']--;
        }

        for (size_t i {}; i < 26; ++i) {
            if (arr[i] != 0) return false;
        }
        
        return true;
    }
};
