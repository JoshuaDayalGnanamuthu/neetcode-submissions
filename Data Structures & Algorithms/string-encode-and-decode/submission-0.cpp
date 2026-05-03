#include <string>
class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        for (string str: strs){
            encoded += to_string(str.length()) + "#" + str;
        }
        printf("%s", encoded);
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        string index;

        for (int i {0}; i < s.size(); i++){
            if (s[i]!='#'){
                index += s[i];
            }
            else if (s[i] == '#') {
                int offset = stoi(index);
                strs.push_back(s.substr(i+1, offset));
                i += offset;
                index = "";
            }
        }
        return strs;

    }
};
