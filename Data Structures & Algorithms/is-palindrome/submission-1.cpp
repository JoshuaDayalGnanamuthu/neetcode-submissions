class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() <= 1) return true;
        string word = "";

        for (char i : s) {
            if (isalnum(i)) word += tolower(i); 
        }

        const char *pointer1 = &word[0];
        const char *pointer2 = &word[0] + word.size() - 1;

        while (pointer1 < pointer2) {
            if (*pointer1 != *pointer2) return false;
            ++pointer1; --pointer2;
        } return true;
    }
};
