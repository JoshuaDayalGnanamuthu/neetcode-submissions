#include<stack>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if (tokens.size() == 1) return stoi(tokens[0]);
        stack<int> stack1;
        for (string character: tokens){
            if (character == "+"){
                int int1 = stack1.top(); stack1.pop();
                int int2 = stack1.top(); stack1.pop();
                stack1.push(int2 + int1);
            }
            else if (character == "-"){
                int int1 = stack1.top(); stack1.pop();
                int int2 = stack1.top(); stack1.pop();
                stack1.push(int2 - int1);
            }
            else if (character == "*"){
                int int1 = stack1.top(); stack1.pop();
                int int2 = stack1.top(); stack1.pop();
                stack1.push(int2 * int1);
            }
            else if (character == "/"){
                int int1 = stack1.top(); stack1.pop();
                int int2 = stack1.top(); stack1.pop();
                stack1.push(int2 / int1);
            }
            else {
                stack1.push(stoi(character));
            }
        }
        return stack1.top();
        
    }
};
