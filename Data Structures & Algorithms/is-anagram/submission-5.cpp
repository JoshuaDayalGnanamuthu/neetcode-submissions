class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> dict1;
        std::unordered_map<char, int> dict2;

        for (char &i: s) dict1[i]++;
        for (char &i: t) dict2[i]++;

        return dict1 == dict2;

        
    }
};
