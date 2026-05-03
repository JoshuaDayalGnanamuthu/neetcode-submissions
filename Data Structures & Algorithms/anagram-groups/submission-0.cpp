bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
            int array1[26] = {0};
            for (int i {0}; i < s.size(); i++){
                array1[s[i] - 'a']++;
                array1[t[i] - 'a']--;
            }
            for (int i: array1){
                if (i != 0) return false;
            } return true;
}

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        

        vector<vector<string>> Myvector;

        for (int i {0}; i < strs.size(); i++) {
            vector<string> AddVector = {strs[i]};
            for (int j {i+1}; j < strs.size(); j++){
                if (isAnagram(strs[i], strs[j])){
                    AddVector.push_back(strs[j]);
                    strs.erase(strs.begin() + j);
                    j--;
                }
            }
            Myvector.push_back(AddVector);
        }

        return Myvector;








    }
};
