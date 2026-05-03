class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int array1[26] = {0};

        for (size_t i {0}; i < s.size(); i++){
            array1[s[i] - 'a']++;
            array1[t[i] - 'a']--;
        }

        for (int &i: array1){
            if (i != 0) return false;
        }

        return true;


        


        
    }
};
