#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map1;
        unordered_map<char, int> map2;

        for (char &letter : s){
            map1[letter]++;
        }

        for (char &letter : t){
            map2[letter]++;
        }

        return map1 == map2;
        
    }
};
