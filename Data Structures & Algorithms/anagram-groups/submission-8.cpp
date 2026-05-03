#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::string, std::vector<std::string>> anagrams;
        std::vector<std::vector<std::string>> result;

        for (std::string str: strs) {
            string word = str;
            std::sort(str.begin(), str.end());
            anagrams[str].push_back(word);
        }

        for (auto& pair: anagrams) {
            result.push_back(pair.second);
        }

        return result;


        
    }
};
