#include <array>
array<int, 26> sketch (string s){
    array<int, 26> array1 {};
    for (int i {0}; i < s.size(); i++){
        array1[s[i] - 'a']++;
    }
    return array1;
}

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map <array<int, 26>, vector<string>> map1;
        vector<vector<string>> MyVector;

        for (string &i: strs){
            map1[sketch(i)].push_back(i);
        }

        for (auto &pair: map1){
            MyVector.push_back(pair.second);
        }
        return MyVector;
    }
};
