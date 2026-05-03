#include <string>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        std::map<char, int> counter;

        for (size_t i {}; i < t.length(); ++i) {
            counter[t.at(i)]++;
            counter[s.at(i)]--;
        }

        for (auto& item: counter) {
            if (item.second != 0) return false;
        }

        return true;
        
    }
};
