class Solution {
public:
    bool isValid(string s) {
        if (s.size() == 0) return false; 

        vector<char> stack;

        for (char c: s) {
            if (c == '[' || c == '{' || c == '(') {
                stack.push_back(c);
            }
            else if (c == ']') {
                if (!stack.empty() && stack.back() == '[') stack.pop_back();
                else return false;
            }
            else if (c == '}') {
                if (!stack.empty() && stack.back() == '{') stack.pop_back();
                else return false;
            }
            else if (c == ')') {
                if (!stack.empty() && stack.back() == '(') stack.pop_back();
                else return false;
            }
        }

        return stack.empty(); 
    }
};
