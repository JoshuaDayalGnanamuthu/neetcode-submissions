#include <algorithm>

class Solution {
public:
    string hash(string &word) {
        int count[26] = {0};
        string result = "";
        for (char &c: word) {
            count[c - 97]++;
        }
        for (int counter: count) {
            result += std::to_string(counter) + ',';
        }
        return result;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> counter;
        std::vector<std::vector<std::string>> results;

        for (string &word: strs) {
            string hashed = hash(word);
            counter[hashed].push_back(word);
        }

        for (auto pair: counter) {
            results.push_back(pair.second);
        }

        return results;
    }
};
